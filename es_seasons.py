from models import Episode, Season

seasons = [
    Season(
        id=1,
        title="Temporada 1",
        season_number=1,
        episodes=[
            Episode(id="GRMGQX55R", title=f"E1 - Midoriya Izuku: Origen", season=1, episode_number=1, synopsis="Midoriya Izuku es un joven que tuvo la desgracia de nacer sin Don, un poder que poseen actualmente el 80 % de los humanos y que él querría usar para convertirse en un héroe como su adorado All Might. Su falta de Don no impide que su objetivo siga siendo acudir a la mejor academia de héroes del país."),
            Episode(id="H7MZ1N4GQ", title=f"E2 - Lo que necesita un héroe", season=1, episode_number=2, synopsis="Izuku está destrozado tras las palabras de All Might, pero el involucrarse en un incidente con el villano que se escapó a All Might, hará que este cambie de opinión sobre él y sobre sí mismo."),
            # Añade más episodios con sus propios IDs y títulos únicos...
        ]
    ),
    Season(
        id=2,
        title="Temporada 2",
        season_number=2,
        episodes=[
            Episode(id="GRDQ8WKWY", title=f"E13.5 - Libreta de heroes", season=2, episode_number=13.5, synopsis="Izuku nos resume la primera temporada del anime en un episodio especial de cara al inicio de la segunda temporada."),
            Episode(id="H7MZ1N4GQ", title=f"E14 - ¡Es la idea, Ochaco!", season=2, episode_number=14, synopsis="Tras el ataque de los villanos en la U.A. se preparan para celebrar el evento más famoso de Japón: el festival deportivo."),
            # Añade más episodios...
        ]
    ),
# Añade más temporadas...
]

def getSeasons():
    return seasons