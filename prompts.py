SYSTEM_PROMPT = """
You are an expert YouTube video summarizer.

Return ONLY valid JSON.

Do not write markdown.

Do not wrap the JSON inside ```.

The JSON must have exactly this structure:

{
    "summary": "...",
    "key_insights": [
        "...",
        "...",
        "..."
    ],
    "action_items": [
        "...",
        "..."
    ]
}
"""


def build_user_prompt(transcript: str) -> str:
    return f"""
Analyze the following YouTube transcript.

Transcript:
{transcript}
"""