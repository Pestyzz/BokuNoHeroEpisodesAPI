from models import Episode, Season

seasons = [
    Season(
        id=1,
        title="Temporada 1",
        season_number=1,
        episodes=[
            Episode(id="GRMGQX55R", title=f"E1 - Midoriya Izuku: Origen", season=1, episode_number=1, synopsis="Midoriya Izuku es un joven que tuvo la desgracia de nacer sin Don, un poder que poseen actualmente el 80 % de los humanos y que él querría usar para convertirse en un héroe como su adorado All Might. Su falta de Don no impide que su objetivo siga siendo acudir a la mejor academia de héroes del país.", image="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/25d40698c5c58c5f0ba0d2daf1974516.jpg"),
            Episode(id="H7MZ1N4GQ", title=f"E2 - Lo que necesita un héroe", season=1, episode_number=2, synopsis="Izuku está destrozado tras las palabras de All Might, pero el involucrarse en un incidente con el villano que se escapó a All Might, hará que este cambie de opinión sobre él y sobre sí mismo.", image="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/e795b22bccecb71e36152fc858083e07.jpg"),
            # Añade más episodios con sus propios IDs y títulos únicos...
        ]
    ),
    Season(
        id=2,
        title="Temporada 2",
        season_number=2,
        episodes=[
            Episode(id="GRDQ8WKWY", title=f"E13.5 - Libreta de heroes", season=2, episode_number=13.5, synopsis="Izuku nos resume la primera temporada del anime en un episodio especial de cara al inicio de la segunda temporada.", image="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/ed131cb64be6f1b678f3e000550c8ca3.jpg"),
            Episode(id="H7MZ1N4GQ", title=f"E14 - ¡Es la idea, Ochaco!", season=2, episode_number=14, synopsis="Tras el ataque de los villanos en la U.A. se preparan para celebrar el evento más famoso de Japón: el festival deportivo.", image="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/3194cf61c6735eff46c80a42f25f76d4.jpg"),
            # Añade más episodios...
        ]
    ),
# Añade más temporadas...
]

def getSeasons():
    return seasons