from pydantic import BaseModel

class VideoSummary(BaseModel):

    summary: str
    key_insights: list[str]
    action_items: list[str]