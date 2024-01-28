# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/page_route.py
from flask import Blueprint, request, render_template, make_response, g , jsonify, url_for
import requests
import jwt
from .rule_route import require_token
from controllers.user_controller import UserController
from controllers.movie_controller import MovieController

page_blueprint = Blueprint('page', __name__)

# ----- Home -----

@page_blueprint.route('/', methods=['GET'])
@require_token
def index():
    token = g.token  
    url = "https://api.themoviedb.org/3/discover/movie?api_key=8770fea03d8b0d550c4b50be1656d5cb&sort_by=popularity.desc"

    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        film_populaire = data.get('results', [])
        return render_template('index.html', cookie=token, movies=film_populaire)
    else:
        print("Erreur lors de la requête")
        return None

# ----- Authentification -----

@page_blueprint.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@page_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# ----- Movie -----

@page_blueprint.route('/movie/add', methods=['GET'])
@require_token
def add_movie():
    token = g.token
    return render_template('add_movie.html', cookie=token)

@page_blueprint.route('/movie/list', methods=['GET'])
@require_token
def my_movie():
    token = g.token
    datas =  MovieController.get_movies()
    return render_template('my_movie.html', cookie=token , datas=datas)


@page_blueprint.route('/movie_detail/<int:movie_id>', methods=['GET'])
@require_token
def search_id(movie_id):
    url = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key=8770fea03d8b0d550c4b50be1656d5cb&language=en-US"
    reponse = requests.get(url)
    if reponse.status_code == 200:

        data = reponse.json()
        

        url_video = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"/videos?api_key=8770fea03d8b0d550c4b50be1656d5cb&language=en-US"
        reponse_video = requests.get(url_video)
        data_video = reponse_video.json()
        ma_video = data_video.get('results', [])
        ma_video = ma_video[0].get('key', [])
       
        token = g.token
        return render_template('movie_detail.html', cookie=token, movie=data , data_video=ma_video)
    else:
        print("Erreur lors de la requête")
        return None

# ----- User -----

@page_blueprint.route('/profile', methods=['GET'])
@require_token
def show_profile():
    token = g.token
    decoded_token = jwt.decode(token, options={'verify_signature': False})
    user_id = decoded_token.get('sub')
    user_data = UserController.get_user(user_id, f'/{str(user_id)}', 'GET')
    return render_template('profile.html', cookie=token, data=user_data)

@page_blueprint.route('/profile/dashboard', methods=['GET'])
@require_token
def show_dashboard():
    token = g.token
    users_data = UserController.get_users('GET')
    return render_template('dashboard.html', cookie=token , data=users_data)

@page_blueprint.route('/edit_page/<int:movie_id>', methods=['GET'])
@require_token
def show_edit(movie_id):
    token = g.token
    decoded_token = jwt.decode(token, options={'verify_signature': False})
    user_id = decoded_token.get('sub')

    data = MovieController.get_movie(movie_id)
    reponse = data.json
    movie = reponse['data']['movie']
    # Note utilisateur
    user_rating = None
    if movie.get('ratings'):
        for rating in movie['ratings']:
            if rating['user_id'] == user_id:
                user_rating = rating['rating']
                break

    # Moynne de notation du film
    if movie.get('ratings'):
        total_ratings = sum(int(rating['rating']) for rating in movie['ratings'])
        average_rating = total_ratings / len(movie['ratings'])
    else:
        average_rating = None
    return render_template('update_movie.html', cookie=token, data=data, average_rating=average_rating, user_rating=user_rating)