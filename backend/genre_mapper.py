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
    "Alternative/Indie Rock": ["Rock", "Alternative"],
    "Pop/Rock": ["Rock", "Pop"],
    
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
    "Club Dance": ["Electronic", "Dance"],
    "Club/Dance": ["Electronic", "Dance"],
    "Deep House": ["Electronic", "Dance"],
    "Detroit Techno": ["Electronic", "Dance"],
    "Downtempo": ["Electronic"],
    "Drum And Bass": ["Electronic", "Dance"],
    "Dub Techno": ["Electronic", "Dance"],
    "Dubstep": ["Electronic", "Dance"],
    "Edm": ["Electronic", "Dance"],
    "Electro": ["Electronic", "Dance"],
    "Electro-Techno": ["Electronic", "Dance"],
    "Electronica": ["Electronic"],
    "Experimental Electronic": ["Electronic", "Experimental"],
    "Experimental Techno": ["Electronic", "Experimental"],
    "Garage": ["Electronic", "Dance"],
    "Glitch": ["Electronic", "Experimental"],
    "House": ["Electronic", "Dance"],
    "Idm": ["Electronic", "Experimental"],
    "Indie Electronic": ["Electronic", "Alternative"],
    "Industrial": ["Electronic", "Experimental"],
    "Jungle": ["Electronic", "Dance"],
    "Jungle/Drum'N'Bass": ["Electronic", "Dance"],
    "Left-Field House": ["Electronic", "Dance"],
    "Minimal Techno": ["Electronic", "Dance"],
    "Nu Disco": ["Electronic", "Dance", "Disco"],
    "Synthpop": ["Electronic", "Pop"],
    "Tech House": ["Electronic", "Dance"],
    "Tech House, Minimal": ["Electronic", "Dance"],
    "Tech-House": ["Electronic", "Dance"],
    "Tech-House, Minimal": ["Electronic", "Dance"],
    "Techno": ["Electronic", "Dance"],
    "Techno House": ["Electronic", "Dance"],
    "Techno/House": ["Electronic", "Dance"],
    "Trance": ["Electronic", "Dance"],
    "Trip-Hop": ["Electronic", "Hip-Hop", "Downtempo"],
    
    # Jazz
    "Bebop": ["Jazz"],
    "Hard Bop": ["Jazz"],
    "Post-Bop": ["Jazz"],
    "Free Jazz": ["Jazz", "Experimental"],
    "Cool Jazz": ["Jazz"],
    "Smooth Jazz": ["Jazz"],
    "Jazz Fusion": ["Jazz", "Rock"],
    "Jazz-House": ["Jazz", "Electronic", "Dance"],
    "Vocal Jazz": ["Jazz"],
    "Gypsy Jazz": ["Jazz", "Folk"],
    "Avant-Garde Jazz": ["Jazz", "Experimental"],
    "Latin Jazz": ["Jazz", "World"],
    "Contemporary Jazz": ["Jazz"],
    
    # Hip-Hop
    "Abstract Hip-Hop": ["Hip-Hop", "Experimental"],
    "Alternative Hip-Hop": ["Hip-Hop", "Alternative"],
    "Boom Bap": ["Hip-Hop"],
    "Conscious Hip-Hop": ["Hip-Hop"],
    "Drill": ["Hip-Hop"],
    "East Coast Hip-Hop": ["Hip-Hop"],
    "Gangsta Rap": ["Hip-Hop"],
    "Grime": ["Hip-Hop", "Electronic"],
    "Hip Hop": ["Hip-Hop"],
    "Lo-Fi Hip-Hop": ["Hip-Hop", "Electronic"],
    "Rap": ["Hip-Hop"],
    "Southern Hip-Hop": ["Hip-Hop"],
    "Trap": ["Hip-Hop"],
    "Turntablism": ["Hip-Hop"],
    "West Coast Hip-Hop": ["Hip-Hop"],
    
    # R&B / Soul
    "Contemporary R&B": ["R&B", "Pop"],
    "Disco": ["R&B", "Soul", "Dance"],
    "Function": ["R&B", "Soul", "Dance"],
    "Funk": ["R&B", "Soul", "Dance"],
    "Italo Disco": ["R&B", "Soul", "Dance"],
    "Italo-Disco": ["R&B", "Soul", "Dance"],
    "Motown": ["R&B", "Soul"],
    "Neo Soul": ["R&B", "Soul"],
    "Neo-Soul": ["R&B", "Soul"],
    "New Jack Swing": ["R&B", "Hip-Hop", "Pop"],
    "Quiet Storm": ["R&B", "Soul"],
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
    "Dance-Pop": ["Pop", "Dance"],
    "Dream Pop": ["Pop", "Alternative"],
    "Electropop": ["Pop", "Electronic"],
    "Indie Pop": ["Pop", "Alternative"],
    "K-Pop": ["Pop", "World"],
    "Synth Pop": ["Pop", "Electronic"],
    "Synth-Pop": ["Pop", "Electronic"],
    "Teen Pop": ["Pop"],
    "Britpop": ["Pop", "Rock"],
    
    # World / Global
    "Reggae": ["Reggae"],
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
    "International": ["World"],
    "Klezmer": ["World", "Folk"],
    
    # Experimental / Avant-Garde
    "Avant-Garde": ["Experimental"],
    "Noise": ["Experimental"],
    "Musique Concrete": ["Experimental", "Electronic"],
    "Sound Collage": ["Experimental"],
    "Drone": ["Experimental", "Ambient"],
    "Dark Ambient": ["Experimental", "Electronic", "Ambient"]
}

MOOD_HIERARCHY = {
    "Energy": ["Energetic", "Intense", "Rousing", "Lively", "Urgent", "Aggressive", "Fiery", "Visceral", "Volatile", "Rebellious", "Boisterous", "Exuberant", "Exciting", "Pulsing", "Brash", "Swaggering", "Strong", "Rollicking", "Confident"],
    "Dark": ["Nocturnal", "Eerie", "Ominous", "Brooding", "Menacing", "Gloomy", "Somber", "Bleak", "Paranoid", "Tense/Anxious", "Wintry", "Cold", "Austere", "Uncompromising"],
    "Vibey": ["Hypnotic", "Trippy", "Dreamy", "Atmospheric", "Ethereal", "Spacey", "Druggy", "Lush", "Flowing", "Meandering", "Sprawling"],
    "Emotional": ["Melancholy", "Yearning", "Passionate", "Wistful", "Bittersweet", "Poignant", "Sentimental", "Plaintive", "Romantic", "Intimate", "Sensual", "Cathartic", "Searching", "Earnest", "Sexy"],
    "Uplifting": ["Happy", "Joyous", "Celebratory", "Carefree", "Fun", "Playful", "Whimsical", "Quirky", "Bright", "Sweet", "Summery", "Cheerful", "Sparkling", "Light", "Warm", "Gentle", "Amiable/Good-Natured"],
    "Cool": ["Stylish", "Sophisticated", "Elegant", "Refined", "Slick", "Smooth", "Detached", "Clinical", "Cerebral", "Complex", "Literate", "Witty", "Enigmatic", "Eccentric", "Ambitious", "Theatrical", "Provocative", "Earthy"],
    "Chill": ["Laid-Back/Mellow", "Relaxed", "Calm/Peaceful", "Soothing", "Soft/Quiet", "Delicate", "Reserved", "Reflective", "Restrained", "Dramatic", "Freewheeling"],
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
