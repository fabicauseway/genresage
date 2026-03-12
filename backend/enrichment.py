import asyncio
import logging
import os
import sqlite3

import pylast

from backend.library_cache import upsert_tags
from backend.genre_mapper import expand_tags

logger = logging.getLogger(__name__)

RATE_LIMIT_SEMAPHORE = asyncio.Semaphore(1)


async def run_enrichment_worker(db_conn: sqlite3.Connection, lastfm_network: pylast.Network):
    """
    Run continuous background worker to enrich untagged tracks via Last.fm.
    Uses Database-as-a-Queue polling on tracks WHERE last_fm_checked IS NULL.
    """
    logger.info("Starting Last.fm enrichment worker...")
    
    consecutive_db_errors = 0

    while True:
        try:
            cursor = db_conn.execute(
                "SELECT rating_key, title, artist FROM tracks WHERE last_fm_checked IS NULL LIMIT 50;"
            )
            tracks = cursor.fetchall()
            
            consecutive_db_errors = 0
            
            if not tracks:
                await asyncio.sleep(60.0)
                continue
                
            batch_enriched = 0
            batch_not_found = 0
            batch_errors = 0

            for track in tracks:
                track_id = None
                try:
                    if isinstance(track, sqlite3.Row):
                        track_id = track["rating_key"]
                        title = track["title"]
                        artist = track["artist"]
                    else:
                        track_id = track[0]
                        title = track[1]
                        artist = track[2]
                        
                    async with RATE_LIMIT_SEMAPHORE:
                        track_obj = pylast.Track(artist=artist, title=title, network=lastfm_network)
                        top_tags = await asyncio.to_thread(track_obj.get_top_tags)
                        
                    surviving_tags = []
                    for tag in top_tags:
                        try:
                            weight = int(tag.weight)
                        except (ValueError, TypeError):
                            continue
                            
                        # Extract tag name safely from TopItem -> Tag object
                        tag_name = tag.item.get_name() if hasattr(tag.item, 'get_name') else tag.item.name
                        
                        if weight < 30:
                            logger.debug(f"Discarded low-weight tag: {tag_name} ({weight})")
                            continue
                            
                        surviving_tags.append(tag_name)
                        
                    if surviving_tags:
                        expanded_tags = expand_tags(surviving_tags)
                        upsert_tags(db_conn, track_id, 'track', expanded_tags['specific'], 'genre')
                        upsert_tags(db_conn, track_id, 'track', expanded_tags['parents'], 'parent_genre')
                        batch_enriched += 1
                        
                except pylast.WSError as e:
                    batch_not_found += 1
                    logger.debug(f"Last.fm WSError for track '{title}': {e}")
                except pylast.NetworkError as e:
                    batch_errors += 1
                    logger.warning(f"Last.fm NetworkError for track '{title}': {e}")
                except Exception as e:
                    batch_errors += 1
                    logger.error(f"Error enriching track '{title}': {e}", exc_info=True)
                finally:
                    if track_id:
                        db_conn.execute(
                            "UPDATE tracks SET last_fm_checked = CURRENT_TIMESTAMP WHERE rating_key = ?", 
                            (track_id,)
                        )
                        db_conn.commit()
                        
                    await asyncio.sleep(1.2)
                    
            logger.info(f"Enrichment batch complete | Enriched: {batch_enriched} | Not Found: {batch_not_found} | Errors: {batch_errors}")

        except Exception as e:
            consecutive_db_errors += 1
            if consecutive_db_errors >= 5:
                logger.critical("Database/Worker strictly failing for 5+ consecutive cycles! Manual intervention required.")
            logger.error(f"Enrichment worker outer loop error: {e}", exc_info=True)
            await asyncio.sleep(60.0)
