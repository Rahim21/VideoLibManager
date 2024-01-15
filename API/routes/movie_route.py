# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.movie_controller import MovieController

movie_blueprint = Blueprint('movie', __name__)

@movie_blueprint.route('/movie', methods=['GET'])
@jwt_required()
def get_movies():
    return MovieController.get_movies()

@movie_blueprint.route('/movie/<int:movie_id>', methods=['GET'])
@jwt_required()
def get_movie(movie_id):
    return MovieController.get_movie(movie_id)

@movie_blueprint.route('/movie/add', methods=['POST'])
@jwt_required()
def add_movie():
    return MovieController.add_movie(request.json)

@movie_blueprint.route('/movie/<int:movie_id>/edit', methods=['PUT'])
@jwt_required()
def edit_movie(movie_id):
    return MovieController.edit_movie(movie_id, request.json)

@movie_blueprint.route('/movie/<int:movie_id>', methods=['DELETE'])
@jwt_required()
def delete_movie(movie_id):
    return MovieController.delete_movie(movie_id)

@movie_blueprint.route('/search/movie/<string:query>', methods=['GET'])
@jwt_required()
def search_movie(query):
    return MovieController.search_movie(query)

@movie_blueprint.route('/movie/<int:movie_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(movie_id):
    return MovieController.add_comment(movie_id, request.json)

@movie_blueprint.route('/movie/<int:movie_id>/rating', methods=['POST'])
@jwt_required()
def add_rating(movie_id):
    return MovieController.add_rating(movie_id, request.json)

@movie_blueprint.route('/movie/<int:movie_id>/videos', methods=['GET'])
@jwt_required()
def get_videos(movie_id):
    return MovieController.get_videos(movie_id)

@movie_blueprint.route('/movie/<int:movie_id>/images', methods=['GET'])
@jwt_required()
def get_images(movie_id):
    return MovieController.get_images(movie_id)

@movie_blueprint.route('/movie/<int:movie_id>/watch/providers', methods=['GET'])
@jwt_required()
def get_watch_providers(movie_id):
    return MovieController.get_watch_providers(movie_id)
