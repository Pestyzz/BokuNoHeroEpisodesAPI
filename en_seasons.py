from models import Episode, Season

seasons = [
    Season(
        id=1,
        title="Season 1",
        season_number=1,
        episodes=[
            Episode(id="GRMGQX55R", title=f"E1 - Midoriya Izuku: Origin", season=1, episode_number=1, synopsis="Midoriya Izuku is a young man who had the misfortune of being born without a Gift, a power currently possessed by 80% of humans and which he would like to use to become a hero like his adored All Might. His lack of Gift does not prevent him from continuing his goal of attending the best hero academy in the country."),
            Episode(id="H7MZ1N4GQ", title=f"E2 - What a hero needs", season=1, episode_number=2, synopsis="Izuku is devastated after All Might's words, but getting involved in an incident with the villain that got away from All Might will make All Might change his mind about him and himself."),
            # Añade más episodios con sus propios IDs y títulos únicos...
        ]
    ),
    Season(
        id=2,
        title="Season 2",
        season_number=2,
        episodes=[
            Episode(id="GRDQ8WKWY", title=f"E13.5 - Heroes Notebook", season=2, episode_number=13.5, synopsis="Izuku recaps the first season of the anime in a special episode ahead of the start of the second season."),
            Episode(id="H7MZ1N4GQ", title=f"E14 - That's the idea, Ochaco!", season=2, episode_number=14, synopsis="After the attack of the villains in the U.A. they are preparing to celebrate the most famous event in Japan: the sports festival."),
            # Añade más episodios...
        ]
    ),
    # Añade más temporadas...
]

def getSeasons():
    return seasons