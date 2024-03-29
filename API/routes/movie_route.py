# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.movie_controller import MovieController

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movies')

@movie_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_movies():
    return MovieController.get_movies()

@movie_blueprint.route('/<int:movie_id>', methods=['GET'])
@jwt_required()
def get_movie(movie_id):
    return MovieController.get_movie(movie_id)

@movie_blueprint.route('/add', methods=['POST'])
@jwt_required()
def add_movie():
    user_id = get_jwt_identity()
    return MovieController.add_movie(request.json, user_id)

@movie_blueprint.route('/<int:movie_id>/edit', methods=['PUT'])
@jwt_required()
def edit_movie(movie_id):
    return MovieController.edit_movie(movie_id, request.json)

@movie_blueprint.route('/<int:movie_id>/delete', methods=['DELETE'])
@jwt_required()
def delete_movie(movie_id):
    return MovieController.delete_movie(movie_id)

@movie_blueprint.route('/search/<string:query>', methods=['POST'])
@jwt_required()
def search_movie(query):
    fields = request.json.get('fields', [])
    return MovieController.search_movie(query, fields)

@movie_blueprint.route('/<int:movie_id>/comment', methods=['POST'])
@jwt_required()
def add_comment(movie_id):
    user_id = get_jwt_identity()
    return MovieController.add_comment(movie_id, user_id, request.json)

@movie_blueprint.route('/<int:movie_id>/rating', methods=['POST'])
@jwt_required()
def add_rating(movie_id):
    user_id = get_jwt_identity()
    return MovieController.add_rating(movie_id, user_id, request.json)

@movie_blueprint.route('/<int:movie_id>/images', methods=['GET'])
@jwt_required()
def get_images(movie_id):
    return MovieController.get_images(movie_id)

# Pour TMDB
# @movie_blueprint.route('/<int:movie_id>/videos', methods=['GET'])
# @jwt_required()
# def get_videos(movie_id):
#     return MovieController.get_videos(movie_id)

# Pour TMDB
# @movie_blueprint.route('/<int:movie_id>/watch/providers', methods=['GET'])
# @jwt_required()
# def get_watch_providers(movie_id):
#     return MovieController.get_watch_providers(movie_id)
