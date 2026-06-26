from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    """
    Extract the YouTube video ID from a standard YouTube URL.
    Example:
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
                        ↓
                  dQw4w9WgXcQ
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if "v" not in query_params:
        raise ValueError("Invalid YouTube URL")

    return query_params["v"][0]


def get_transcript(url: str) -> str:
    """
    Fetch the transcript of a YouTube video and return it
    as a single string.
    """

    video_id = extract_video_id(url)
    
    transcript = YouTubeTranscriptApi().fetch(video_id)

    transcript_text = " ".join(
        chunk.text for chunk in transcript
    )

    return transcript_text
