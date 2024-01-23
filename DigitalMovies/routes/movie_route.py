# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request, render_template, make_response, g
import requests
from controllers.movie_controller import MovieController

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movies')

@movie_blueprint.route('/', methods=['GET'])
def get_movies():
    return MovieController.get_movies()

@movie_blueprint.route('/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    return MovieController.get_movie(movie_id)

@movie_blueprint.route('/add', methods=['POST'])
def add_movie():
    return MovieController.add_movie(request.json)

@movie_blueprint.route('/<int:movie_id>/edit', methods=['POST'])
def edit_movie(movie_id):
    return MovieController.edit_movie(movie_id, request.json)

@movie_blueprint.route('/<int:movie_id>/delete', methods=['DELETE'])
def delete_movie(movie_id):
    return MovieController.delete_movie(movie_id)

@movie_blueprint.route('/search/<string:query>', methods=['GET'])
def search_movie(query):
    return MovieController.search_movie(query)

@movie_blueprint.route('/<int:movie_id>/comments', methods=['POST'])
def add_comment(movie_id):
    return MovieController.add_comment(movie_id, request.json)

@movie_blueprint.route('/<int:movie_id>/rating', methods=['POST'])
def add_rating(movie_id):
    return MovieController.add_rating(movie_id, request.json)

@movie_blueprint.route('/<int:movie_id>/videos', methods=['GET'])
def get_videos(movie_id):
    return MovieController.get_videos(movie_id)

@movie_blueprint.route('/<int:movie_id>/images', methods=['GET'])
def get_images(movie_id):
    return MovieController.get_images(movie_id)

@movie_blueprint.route('/<int:movie_id>/watch/providers', methods=['GET'])
def get_watch_providers(movie_id):
    return MovieController.get_watch_providers(movie_id)
