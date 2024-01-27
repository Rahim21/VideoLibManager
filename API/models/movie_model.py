# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# models/movie_model.py
class Movie:
    def __init__(self, id, title, user_id, overview=None, release_date=None, genres=None, poster_path=None, countries=None, vote_average=None, vote_count=None, images=None, comments=None, ratings=None):
        self.id = id
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.genres = genres
        self.poster_path = poster_path
        self.countries = countries
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.images = images if images is not None else []
        self.comments = comments if comments is not None else []
        self.ratings = ratings if ratings is not None else []
        self.user_id = user_id
