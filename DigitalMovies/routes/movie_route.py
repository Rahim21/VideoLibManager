# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request, render_template, make_response, g
import requests
from controllers.movie_controller import MovieController
from .rule_route import require_token

movie_blueprint = Blueprint('movie', __name__, url_prefix='/movies')

@movie_blueprint.route('/', methods=['GET'])
def get_movies():
    return MovieController.get_movies()

@movie_blueprint.route('/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    return MovieController.get_movie(movie_id)

@movie_blueprint.route('/add', methods=['POST'])
@require_token
def add_movie():
    token = g.token
    data =  MovieController.add_movie(request, '/add', request.method)
    return render_template('my_movie.html', data=data, cookie=token)

# ---------------------------------------- A TESTER ----------------------------------------
@movie_blueprint.route('/<int:movie_id>/edit', methods=['POST'])
def edit_movie(movie_id):
    token = g.token
    data = MovieController.edit_movie(request.json, f'/{movie_id}/edit', request.method) # request.json ou request
    return render_template('my_movie.html', data=data, cookie=token)

@movie_blueprint.route('/<int:movie_id>/delete', methods=['DELETE'])
def delete_movie(movie_id):
    return MovieController.delete_movie(f'/{movie_id}/delete', request.method)

@movie_blueprint.route('/search/<string:query>', methods=['GET'])
def search_movie(query):
    return MovieController.search_movie(query, f'/search/{query}', request.method)

@movie_blueprint.route('/<int:movie_id>/comments', methods=['POST'])
def add_comment(movie_id):
    return MovieController.add_comment(request.json, f'/{movie_id}/comments', request.method) # request.json ou request

@movie_blueprint.route('/<int:movie_id>/rating', methods=['POST'])
def add_rating(movie_id):
    return MovieController.add_rating(request.json, f'/{movie_id}/rating', request.method) # request.json ou request

@movie_blueprint.route('/<int:movie_id>/images', methods=['GET'])
def get_images(movie_id):
    return MovieController.get_images(f'/{movie_id}/images', request.method)

# @movie_blueprint.route('/<int:movie_id>/videos', methods=['GET'])
# def get_videos(movie_id):
#     return MovieController.get_videos(f'/{movie_id}/videos', request.method)

# @movie_blueprint.route('/<int:movie_id>/watch/providers', methods=['GET'])
# def get_watch_providers(movie_id):
#     return MovieController.get_watch_providers(movie_id)
