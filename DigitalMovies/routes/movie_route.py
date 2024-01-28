# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/movie_route.py
from flask import Blueprint, request, render_template, make_response, g, url_for
import requests
import jwt
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
    decoded_token = jwt.decode(token, options={'verify_signature': False})
    user_id = decoded_token.get('sub')
    MovieController.add_movie(user_id, request, '/add', request.method)
    datas =  MovieController.get_movies()
    return render_template('my_movie.html', datas=datas, cookie=token)

# ---------------------------------------- A TESTER ----------------------------------------
@movie_blueprint.route('/<int:movie_id>/edit', methods=['POST'])
@require_token
def edit_movie(movie_id):
    token = g.token
    data = MovieController.edit_movie(request, f'/{movie_id}/edit', request.method) # request.json ou request
    datas =  MovieController.get_movies()
    return render_template('my_movie.html', data=data, datas=datas, cookie=token)

@movie_blueprint.route('/<int:movie_id>/delete', methods=['POST'])
@require_token
def delete_movie(movie_id):
    token = g.token
    MovieController.delete_movie(f'/{movie_id}/delete', 'DELETE')
    datas =  MovieController.get_movies()
    return render_template('my_movie.html',datas=datas, cookie=token)

@movie_blueprint.route('/search', methods=['POST'])
@require_token
def search_movie():
    token = g.token
    query = request.form.get('query')
    if not query:
        query = '='
    fields = request.form.getlist('filters[]')
    if not fields:
        fields = ['title', 'overview', 'release_date', 'genres', 'poster_path', 'countries', 'vote_average', 'vote_count']
    data = MovieController.search_movie(query, fields, f'/search/{query}', request.method)
    return render_template('my_movie.html', datas=data, cookie=token)

@movie_blueprint.route('/<int:movie_id>/comments', methods=['POST'])
def add_comment(movie_id):
    return MovieController.add_comment(request.json, f'/{movie_id}/comments', request.method) # request.json ou request

@movie_blueprint.route('/<int:movie_id>/rating', methods=['POST'])
def add_rating(movie_id):
    return MovieController.add_rating(request.json, f'/{movie_id}/rating', request.method)

@movie_blueprint.route('/<int:movie_id>/images', methods=['GET'])
def get_images(movie_id):
    return MovieController.get_images(f'/{movie_id}/images', request.method)

# @movie_blueprint.route('/<int:movie_id>/videos', methods=['GET'])
# def get_videos(movie_id):
#     return MovieController.get_videos(f'/{movie_id}/videos', request.method)

# @movie_blueprint.route('/<int:movie_id>/watch/providers', methods=['GET'])
# def get_watch_providers(movie_id):
#     return MovieController.get_watch_providers(movie_id)
