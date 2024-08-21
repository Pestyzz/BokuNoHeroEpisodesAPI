from fastapi import FastAPI, Query, HTTPException
from models import Season, Episode, List
import es_seasons, en_seasons

app = FastAPI()

data = {
    "es": es_seasons.getSeasons(),
    "en": en_seasons.getSeasons()
}

@app.get("/seasons", response_model=List[Season])
def get_seasons(language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        raise HTTPException(status_code=400, detail="Language not supported")
    return data[language]

@app.get("/seasons/{season_id}", response_model=Season)
def get_season(season_id: int, language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        raise HTTPException(status_code=400, detail="Language not supported")
    season = next((s for s in data[language] if s.id == season_id), None)
    if season:
        return season
    raise HTTPException(status_code=404, detail="Season not found")

@app.get("/episode/{episode_number}", response_model=Episode)
def get_episode(episode_number: float, language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        raise HTTPException(status_code=400, detail="Language not supported")
    for season in data[language]:
        episode = next((e for e in season.episodes if e.episode_number == episode_number), None)
        if episode:
            return episode
    raise HTTPException(status_code=404, detail="Episode not found")

@app.get("/episodes_by_season/{season_id}", response_model=List[Episode])
def get_episodes_by_season(season_id: int, language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        raise HTTPException(status_code=400, detail="Language not supported")
    season = next((s for s in data[language] if s.id == season_id), None)
    if season:
        return season.episodes
    raise HTTPException(status_code=404, detail="Season not found")
