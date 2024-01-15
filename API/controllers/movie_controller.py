# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/movie_controller.py
from flask import jsonify, request
from services.movie_service import MovieService

class MovieController:

    @staticmethod
    def get_movies():
        try:
            movies = MovieService.get_movies()
            return jsonify({"statusCode": 200, "movies": movies})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def get_movie(movie_id):
        try:
            movie = MovieService.get_movie_by_id(movie_id)
            if not movie:
                return jsonify({"statusCode": 200, "movie": None})
            return jsonify({"statusCode": 200, "movie": movie})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def add_movie(movie_data):
        try:
            movie = MovieService.create_movie(movie_data)
            if movie:
                return jsonify({"statusCode": 201, "movie": movie})
            else:
                return jsonify({"statusCode": 400, "error": "Erreur lors de l'ajout du film."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def edit_movie(movie_id, updated_data):
        try:
            movie = MovieService.update_movie(movie_id, updated_data)
            if not movie:
                return jsonify({"statusCode": 200, "movie": None})
            return jsonify({"statusCode": 200, "movie": movie})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def delete_movie(movie_id):
        try:
            movie = MovieService.delete_movie(movie_id)
            if not movie:
                return jsonify({"statusCode": 200, "movie": None})
            return jsonify({"statusCode": 200, "movie": movie})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def search_movie(query):
        try:
            results = MovieService.search_movie(query)
            return jsonify({"statusCode": 200, "results": results})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def add_comment(movie_id, comment_data):
        try:
            comment = MovieService.add_comment(movie_id, comment_data)
            return jsonify({"statusCode": 200, "comment": comment})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def add_rating(movie_id, rating_data):
        try:
            rating = MovieService.add_rating(movie_id, rating_data)
            return jsonify({"statusCode": 200, "rating": rating})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def get_videos(movie_id):
        try:
            videos = MovieService.get_videos(movie_id)
            return jsonify({"statusCode": 200, "videos": videos})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def get_images(movie_id):
        try:
            images = MovieService.get_images(movie_id)
            return jsonify({"statusCode": 200, "images": images})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def get_watch_providers(movie_id):
        try:
            providers = MovieService.get_watch_providers(movie_id)
            return jsonify({"statusCode": 200, "providers": providers})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})
