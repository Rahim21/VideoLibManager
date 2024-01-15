# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# services/movie_service.py
import json
import os
from models.movie_model import Movie
from flask import jsonify

class MovieService:

    @staticmethod
    def get_movies():
        pass

    @staticmethod
    def get_movie_by_id(movie_id):
        pass

    @staticmethod
    def create_movie(movie_data):
        pass

    @staticmethod
    def update_movie(movie_id, updated_data):
        pass

    @staticmethod
    def delete_movie(movie_id):
        pass

    @staticmethod
    def search_movie(query):
        pass

    @staticmethod
    def add_comment(movie_id, comment_data):
        pass

    @staticmethod
    def add_rating(movie_id, rating_data):
        pass

    @staticmethod
    def get_videos(movie_id):
        pass

    @staticmethod
    def get_images(movie_id):
        pass

    @staticmethod
    def get_watch_providers(movie_id):
        pass
