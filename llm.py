import json
from groq import Groq
from prompts import SYSTEM_PROMPT, build_user_prompt
from models import VideoSummary
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def summarize_video(transcript: str) -> VideoSummary:

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages= [
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content": build_user_prompt(transcript)
            },
        ],
        temperature=0.5
    )

    response_text = response.choices[0].message.content

    response_json = json.loads(response_text)
    return VideoSummary(**response_json)

