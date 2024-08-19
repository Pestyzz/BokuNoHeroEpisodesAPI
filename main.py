from fastapi import FastAPI, Query
from typing import List, Dict
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()
translator = Translator()

class Episode(BaseModel):
    id: int
    title: str
    season: int
    episode_number: int
    synopsis: str
    crunchyroll_id: str

class Season(BaseModel):
    id: int
    title: str
    episodes: List[Episode]

# Define your data structure
data: List[Season] = [
    Season(
        id=1,
        title="Temporada 1",
        episodes=[
            Episode(id=1, title="E1 - El Comienzo", season=1, episode_number=1, synopsis="Izuku comienza su viaje para convertirse en el héroe número uno.", crunchyroll_id="GRMGQX55R"),
            Episode(id=2, title="E2 - Lo que un héroe necesita", season=1, episode_number=2, synopsis="Izuku está devastado por las palabras de All Might, pero involucrarse en un incidente con el villano que escapó de All Might hará que cambie su opinión sobre él y sobre sí mismo.", crunchyroll_id="GR3VP39N6"),
            # Agrega más episodios...
        ]
    ),
    # Agrega más temporadas...
]

@app.get("/seasons", response_model=List[Season])
def get_seasons(language: str = Query("es", enum=["es", "en"])):
    """
    Get all seasons for a given language.
    
    - **language**: Language code (es for Spanish, en for English)
    """
    if language not in ["es", "en"]:
        return {"error": "Language not supported"}
    
    if language == "es":
        return data
    
    translated_data = []
    for season in data:
        translated_episodes = []
        for episode in season.episodes:
            translated_title = translator.translate(episode.title, src='es', dest='en').text
            translated_synopsis = translator.translate(episode.synopsis, src='es', dest='en').text
            translated_episodes.append(Episode(
                id=episode.id,
                title=translated_title,
                season=episode.season,
                episode_number=episode.episode_number,
                synopsis=translated_synopsis,
                crunchyroll_id=episode.crunchyroll_id
            ))
        translated_data.append(Season(
            id=season.id,
            title=translator.translate(season.title, src='es', dest='en').text,
            episodes=translated_episodes
        ))
    
    return translated_data

@app.get("/seasons/{season_id}", response_model=Season)
def get_season(season_id: int, language: str = Query("es", enum=["es", "en"])):
    """
    Get a specific season by ID for a given language.
    
    - **season_id**: ID of the season
    - **language**: Language code (es for Spanish, en for English)
    """
    if language not in ["es", "en"]:
        return {"error": "Language not supported"}
    
    season = next((s for s in data if s.id == season_id), None)
    if not season:
        return {"error": "Season not found"}
    
    if language == "es":
        return season
    
    translated_episodes = []
    for episode in season.episodes:
        translated_title = translator.translate(episode.title, src='es', dest='en').text
        translated_synopsis = translator.translate(episode.synopsis, src='es', dest='en').text
        translated_episodes.append(Episode(
            id=episode.id,
            title=translated_title,
            season=episode.season,
            episode_number=episode.episode_number,
            synopsis=translated_synopsis,
            crunchyroll_id=episode.crunchyroll_id
        ))
    
    translated_season = Season(
        id=season.id,
        title=translator.translate(season.title, src='es', dest='en').text,
        episodes=translated_episodes
    )
    
    return translated_season

@app.get("/episodes/{episode_id}", response_model=Episode)
def get_episode(episode_id: int, language: str = Query("es", enum=["es", "en"])):
    """
    Get a specific episode by ID for a given language.
    
    - **episode_id**: ID of the episode
    - **language**: Language code (es for Spanish, en for English)
    """
    if language not in ["es", "en"]:
        return {"error": "Language not supported"}
    
    for season in data:
        episode = next((e for e in season.episodes if e.id == episode_id), None)
        if episode:
            if language == "es":
                return episode
            
            translated_title = translator.translate(episode.title, src='es', dest='en').text
            translated_synopsis = translator.translate(episode.synopsis, src='es', dest='en').text
            translated_episode = Episode(
                id=episode.id,
                title=translated_title,
                season=episode.season,
                episode_number=episode.episode_number,
                synopsis=translated_synopsis,
                crunchyroll_id=episode.crunchyroll_id
            )
            return translated_episode
    
    return {"error": "Episode not found"}