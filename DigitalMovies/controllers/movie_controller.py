# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/movie_controller.py
from flask import jsonify, request, render_template, make_response

class MovieController:

    @staticmethod
    def get_movies():
        pass

    @staticmethod
    def get_movie(movie_id):
        pass

    @staticmethod
    def add_movie(movie_data):
        pass

    @staticmethod
    def edit_movie(movie_id, updated_data):
        pass
        # title, genre, director = (updated_data.form.get(field, '') for field in ['title', 'genre', 'director'])

        # # Dictionnaire avec les champs non vides
        # data = {
        #     key: value for key, value in {
        #         "title": title,
        #         "genre": genre,
        #         "director": director,
        #     }.items() if value
        # }

        # # Vérifier si le dictionnaire est vide
        # if not data:
        #     return render_template('index.html', message='No data to edit!')

        # url = f"http://127.0.0.1:5001/movies/{movie_id}/edit"

        # #   headers = {'Authorization': f'Bearer {token}'} # Replace {token} with your actual token
        # response = make_request('PUT', url, data=data)

        # if response and response.get('statusCode', '') == 200:
        #     return render_template('index.html', message=f'Movie {title} edited successfully!')
        # else:
        #     return render_template('index.html', message='Edit failed!')


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
