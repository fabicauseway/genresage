GENRE_HIERARCHY = {
    # Rock
    "Alternative Rock": ["Rock", "Alternative"],
    "Indie Rock": ["Rock", "Alternative"],
    "Psychedelic Rock": ["Rock"],
    "Progressive Rock": ["Rock"],
    "Hard Rock": ["Rock"],
    "Punk Rock": ["Rock", "Punk"],
    "Post-Punk": ["Rock", "Alternative", "Punk"],
    "Math Rock": ["Rock", "Alternative"],
    "Shoegaze": ["Rock", "Alternative"],
    "Grunge": ["Rock", "Alternative"],
    "Classic Rock": ["Rock"],
    "Folk Rock": ["Rock", "Folk"],
    "Soft Rock": ["Rock", "Pop"],
    "Art Rock": ["Rock", "Experimental"],
    "Krautrock": ["Rock", "Electronic", "Experimental"],
    "Alternative": ["Rock", "Alternative"],
    
    # Metal
    "Heavy Metal": ["Metal", "Rock"],
    "Thrash Metal": ["Metal"],
    "Death Metal": ["Metal"],
    "Black Metal": ["Metal"],
    "Doom Metal": ["Metal"],
    "Sludge Metal": ["Metal"],
    "Post-Metal": ["Metal", "Experimental"],
    "Progressive Metal": ["Metal"],
    "Nu Metal": ["Metal", "Rock"],
    "Metalcore": ["Metal", "Punk"],
    "Symphonic Metal": ["Metal"],
    
    # Electronic
    "Techno": ["Electronic", "Dance"],
    "House": ["Electronic", "Dance"],
    "Tech House": ["Electronic", "Dance"],
    "Deep House": ["Electronic", "Dance"],
    "Trance": ["Electronic", "Dance"],
    "Dubstep": ["Electronic", "Dance"],
    "Drum And Bass": ["Electronic", "Dance"],
    "Jungle": ["Electronic", "Dance"],
    "Ambient": ["Electronic"],
    "Idm": ["Electronic", "Experimental"],
    "Synthpop": ["Electronic", "Pop"],
    "Electro": ["Electronic", "Dance"],
    "Downtempo": ["Electronic"],
    "Trip-Hop": ["Electronic", "Hip-Hop", "Downtempo"],
    "Industrial": ["Electronic", "Experimental"],
    "Breakbeat": ["Electronic", "Dance"],
    "Edm": ["Electronic", "Dance"],
    "Nu Disco": ["Electronic", "Dance", "Disco"],
    "Glitch": ["Electronic", "Experimental"],
    
    # Jazz
    "Bebop": ["Jazz"],
    "Hard Bop": ["Jazz"],
    "Post-Bop": ["Jazz"],
    "Free Jazz": ["Jazz", "Experimental"],
    "Cool Jazz": ["Jazz"],
    "Smooth Jazz": ["Jazz"],
    "Jazz Fusion": ["Jazz", "Rock"],
    "Vocal Jazz": ["Jazz"],
    "Gypsy Jazz": ["Jazz", "Folk"],
    "Avant-Garde Jazz": ["Jazz", "Experimental"],
    "Latin Jazz": ["Jazz", "World"],
    "Contemporary Jazz": ["Jazz"],
    
    # Hip-Hop
    "Boom Bap": ["Hip-Hop"],
    "Trap": ["Hip-Hop"],
    "Lo-Fi Hip-Hop": ["Hip-Hop", "Electronic"],
    "Conscious Hip-Hop": ["Hip-Hop"],
    "Gangsta Rap": ["Hip-Hop"],
    "Alternative Hip-Hop": ["Hip-Hop", "Alternative"],
    "Turntablism": ["Hip-Hop"],
    "Southern Hip-Hop": ["Hip-Hop"],
    "East Coast Hip-Hop": ["Hip-Hop"],
    "West Coast Hip-Hop": ["Hip-Hop"],
    "Drill": ["Hip-Hop"],
    "Grime": ["Hip-Hop", "Electronic"],
    "Abstract Hip-Hop": ["Hip-Hop", "Experimental"],
    
    # R&B / Soul
    "Neo-Soul": ["R&B", "Soul"],
    "Contemporary R&B": ["R&B", "Pop"],
    "Motown": ["R&B", "Soul"],
    "Funk": ["R&B", "Soul", "Dance"],
    "Disco": ["R&B", "Soul", "Dance"],
    "Quiet Storm": ["R&B", "Soul"],
    "New Jack Swing": ["R&B", "Hip-Hop", "Pop"],
    "Alternative R&B": ["R&B", "Alternative"],
    
    # Folk / Country
    "Bluegrass": ["Country", "Folk"],
    "Americana": ["Country", "Folk", "Rock"],
    "Traditional Country": ["Country"],
    "Outlaw Country": ["Country"],
    "Contemporary Folk": ["Folk"],
    "Indie Folk": ["Folk", "Alternative"],
    "Freak Folk": ["Folk", "Experimental"],
    "Anti-Folk": ["Folk", "Punk"],
    "Country-Pop": ["Country", "Pop"],
    "Singer-Songwriter": ["Folk", "Pop"],
    
    # Classical
    "Baroque": ["Classical"],
    "Romantic": ["Classical"],
    "Classical Period": ["Classical"],
    "Contemporary Classical": ["Classical", "Experimental"],
    "Minimalism": ["Classical", "Experimental"],
    "Choral": ["Classical", "Vocal"],
    "Orchestral": ["Classical"],
    "Chamber Music": ["Classical"],
    "Opera": ["Classical", "Vocal"],
    
    # Pop
    "Indie Pop": ["Pop", "Alternative"],
    "Electropop": ["Pop", "Electronic"],
    "Dream Pop": ["Pop", "Alternative"],
    "K-Pop": ["Pop", "World"],
    "J-Pop": ["Pop", "World"],
    "Art Pop": ["Pop", "Experimental"],
    "Chamber Pop": ["Pop"],
    "Dance-Pop": ["Pop", "Dance"],
    "Synth-Pop": ["Pop", "Electronic"],
    "Teen Pop": ["Pop"],
    "Britpop": ["Pop", "Rock"],
    
    # World / Global
    "Reggae": ["World", "Reggae"],
    "Ska": ["Reggae"],
    "Dub": ["Reggae", "Electronic"],
    "Dancehall": ["Reggae", "Dance"],
    "Afrobeat": ["World", "Funk"],
    "Afrobeats": ["World", "Pop", "Dance"],
    "Bossa Nova": ["World", "Jazz"],
    "Samba": ["World"],
    "Flamenco": ["World"],
    "Salsa": ["World", "Dance"],
    "Cumbia": ["World"],
    "Bhangra": ["World", "Dance"],
    "Highlife": ["World"],
    "Klezmer": ["World", "Folk"],
    
    # Experimental / Avant-Garde
    "Avant-Garde": ["Experimental"],
    "Noise": ["Experimental"],
    "Musique Concrete": ["Experimental", "Electronic"],
    "Sound Collage": ["Experimental"],
    "Drone": ["Experimental", "Ambient"],
    "Dark Ambient": ["Experimental", "Electronic", "Ambient"]
}

def get_parent_genres(tags: list[str]) -> set[str]:
    parents = set()
    for tag in tags:
        if tag in GENRE_HIERARCHY:
            parents.update(GENRE_HIERARCHY[tag])
    return parents

def expand_tags(tags: list[str]) -> dict[str, list[str]]:
    """Expand specific tags into grouped parents.

    Guarantees that all incoming tags are automatically sanitized (empty strings 
    stripped, and mapped using `.strip().title()` normalization) prior to 
    expansion, preventing overlap between specific tags and parent categories.

    Args:
        tags: List of raw genre strings.

    Returns:
        Dict mapped to strictly sorted lists of 'specific' tags and 'parents'.
    """
    normalized_tags = [t.strip().title() for t in tags if t and t.strip()]
    specific_set = set(normalized_tags)
    parents_set = get_parent_genres(normalized_tags)
    
    parents_set = parents_set - specific_set
    
    return {
        "specific": sorted(list(specific_set)),
        "parents": sorted(list(parents_set))
    }

def get_all_parent_categories() -> list[str]:
    parents = set()
    for p_list in GENRE_HIERARCHY.values():
        parents.update(p_list)
    return sorted(list(parents))

def get_genre_hierarchy() -> dict[str, list[str]]:
    return GENRE_HIERARCHY
