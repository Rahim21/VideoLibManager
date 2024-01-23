# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/page_route.py
from flask import Blueprint, request, render_template, make_response, g , jsonify
import requests
from .rule_route import require_token

page_blueprint = Blueprint('page', __name__)

# ----- Home -----

@page_blueprint.route('/', methods=['GET'])
@require_token
def index():
    token = g.token

    # url = "https://api.themoviedb.org/3/person/popular?language=fr-FR&page=1"
    # headers = {
    # "accept": "application/json",
    # "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MmI2M2ZmMDI1YTllN2JiNGRlODU0ZTZhNjViOWJlOSIsInN1YiI6IjY1YTdmYWQyMTEzODZjMDEyMmU2MjllYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Hl7k89A1p-8TVcOIhga1RLpxaFPdqTu7_HgZNkhnW5o"
    # }
    # response = requests.get(url, headers=headers)


    # id_films = response.json()["results"]
    # params = { 'api_key': '42b63ff025a9e7bb4de854e6a65b9be9' , 'language': 'fr-FR' , 'page': 1 , 'sort_by': 'popularity.desc' , 'include_adult': 'false' , 'include_video': 'false' }
    # for i in range(1, 4):
    #     params["page"] = i
    #     response = requests.get(url, params=params)

    #     # If the request was successful, append the films to the list
    #     if response.status_code == 200:
    #         id_films += response.json()["results"]
            
    # films = []
    # for ids in id_films:
    #     url = "https://api.themoviedb.org/3/movie/" + str(ids['id'])
    #     params = { 'api_key': '42b63ff025a9e7bb4de854e6a65b9be9' , 'language': 'fr-FR' }
    #     response = requests.get(url, headers=headers, params=params)
    #     if response.status_code == 200:
    #         films += [response.json()]
    # films = jsonify(films)

    # print(f"Résultat en json : { films.json() }")
    
   
    url = "https://api.themoviedb.org/3/discover/movie?api_key=8770fea03d8b0d550c4b50be1656d5cb&sort_by=popularity.desc"

    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        film_populaire = data.get('results', [])
        # image = "https://image.tmdb.org/t/p/w342/" + film['poster_path']
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

# ----- User -----

@page_blueprint.route('/profile', methods=['GET'])
@require_token
def show_profile():
    token = g.token
    return render_template('profile.html', cookie=token)

    # user_id = ...  # Obtenez l'ID de l'utilisateur actuel (inclus dans le token jwt)
    # user = UserController.get_user(user_id, 'get', 'GET')
    # return render_template('profile.html', user=user)
