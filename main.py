from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Episode(BaseModel):
    id: float
    title: str
    season: int
    episode_number: int
    synopsis: str = "N/A"
    crunchyroll_id: str

class Season(BaseModel):
    id: int
    title: str
    season_number: int
    episodes: List[Episode]

data = {
    "es": [
        Season(
            id=1,
            title="Temporada 1",
            season_number=1,
            episodes=[
                Episode(id=1, title=f"E1 - Midoriya Izuku: Origen", season=1, episode_number=1, synopsis="Midoriya Izuku es un joven que tuvo la desgracia de nacer sin Don, un poder que poseen actualmente el 80 % de los humanos y que él querría usar para convertirse en un héroe como su adorado All Might. Su falta de Don no impide que su objetivo siga siendo acudir a la mejor academia de héroes del país.", crunchyroll_id="GRMGQX55R"),
                Episode(id=2, title=f"E2 - Lo que necesita un héroe", season=1, episode_number=2, synopsis="Izuku está destrozado tras las palabras de All Might, pero el involucrarse en un incidente con el villano que se escapó a All Might, hará que este cambie de opinión sobre él y sobre sí mismo.", crunchyroll_id="GR3VP39N6"),
                # Añade más episodios con sus propios IDs y títulos únicos...
            ]
        ),
        Season(
            id=2,
            title="Temporada 2",
            season_number=2,
            episodes=[
                Episode(id=14, title="That's the Idea, Ochaco", season=2, episode_number=14, synopsis="Ochaco Uraraka reveals her motivation.", crunchyroll_id="F9KJ8D0TQ"),
                Episode(id=15, title="Roaring Sports Festival", season=2, episode_number=15, synopsis="UA's annual sports festival begins.", crunchyroll_id="H7MZ1N4GQ"),
                # Añade más episodios...
            ]
        ),
        # Añade más temporadas...
    ],
    "en": [
        Season(
            id=1,
            title="Season 1",
            season_number=1,
            episodes=[
                Episode(id=1, title=f"E1 - Midoriya Izuku: Origin", season=1, episode_number=1, synopsis="Midoriya Izuku is a young man who had the misfortune of being born without a Gift, a power currently possessed by 80% of humans and which he would like to use to become a hero like his adored All Might. His lack of Gift does not prevent him from continuing his goal of attending the best hero academy in the country.", crunchyroll_id="GRMGQX55R"),
                Episode(id=2, title=f"E2 - What a hero needs", season=1, episode_number=2, synopsis="Izuku is devastated after All Might's words, but getting involved in an incident with the villain that got away from All Might will make All Might change his mind about him and himself.", crunchyroll_id="GR3VP39N6"),
                # Añade más episodios con sus propios IDs y títulos únicos...
            ]
        ),
        Season(
            id=2,
            title="Season 2",
            season_number=2,
            episodes=[
                Episode(id=14, title="That's the Idea, Ochaco", season=2, episode_number=14, synopsis="Ochaco Uraraka reveals her motivation.", crunchyroll_id="F9KJ8D0TQ"),
                Episode(id=15, title="Roaring Sports Festival", season=2, episode_number=15, synopsis="UA's annual sports festival begins.", crunchyroll_id="H7MZ1N4GQ"),
                # Añade más episodios...
            ]
        ),
        # Añade más temporadas...
    ]
}

@app.get("/seasons", response_model=List[Season])
def get_seasons(language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        return {"error": "Language not supported"}
    return data[language]

@app.get("/seasons/{season_id}", response_model=Season)
def get_season(season_id: int, language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        return {"error": "Language not supported"}
    season = next((s for s in data[language] if s.id == season_id), None)
    if season:
        return season
    return {"error": "Season not found"}

@app.get("/episodes/{episode_id}", response_model=Episode)
def get_episode(episode_id: int, language: str = Query("es", enum=["es", "en"])):
    if language not in data:
        return {"error": "Language not supported"}
    for season in data[language]:
        episode = next((e for e in season.episodes if e.id == episode_id), None)
        if episode:
            return episode
    return {"error": "Episode not found"}
