# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# models/movie_model.py
class Movie:
    def __init__(self, id, title, overview, release_date, genres, poster_path,
                 production_companies, production_countries, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.genres = genres
        self.poster_path = poster_path
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.vote_average = vote_average
        self.vote_count = vote_count
