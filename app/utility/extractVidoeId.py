import re

def extract_videoid(url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.
    Returns None if no video ID is found.
    """
    # Match common YouTube URL patterns
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",                    # standard watch?v=...
        r"youtu\.be\/([0-9A-Za-z_-]{11})",                    # shortened youtu.be/...
        r"youtube\.com\/embed\/([0-9A-Za-z_-]{11})",          # embedded
        r"youtube\.com\/shorts\/([0-9A-Za-z_-]{11})"          # shorts
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None
