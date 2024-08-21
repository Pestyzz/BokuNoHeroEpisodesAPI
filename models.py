from pydantic import BaseModel
from typing import List

class Episode(BaseModel):
    id: str
    episode_number: float
    title: str
    season: int
    synopsis: str = "N/A"
    image: str
    watch_url: str

class Season(BaseModel):
    id: int
    title: str
    season_number: int
    episodes: List[Episode]

def getWatchUrl(episode_id: str):
    return f"https://www.crunchyroll.com/es/watch/{episode_id}"