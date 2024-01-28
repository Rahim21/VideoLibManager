# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/movie_controller.py
from flask import render_template
from controllers.requestAPI import RequestAPI

class MovieController:

    api_url = "http://127.0.0.1:5001"
    movie_url = api_url + "/movies"

    @staticmethod
    def get_movies():
        url = MovieController.movie_url
        return RequestAPI.request_to_api('GET', url, success_message='Movies fetched successfully!', error_message='Failed to fetch movies!')

    @staticmethod
    def get_movie(movie_id):
        url = "{}/{}".format(MovieController.movie_url, movie_id)
        return RequestAPI.request_to_api('GET', url, success_message=f'Movie {movie_id} fetched successfully!', error_message=f'Failed to fetch movie {movie_id}!')

    @staticmethod
    def add_movie(user_id, movie_data, route_url, method):
        private = movie_data.form.get('private', '')
        title, overview, release_date, genres, poster_path, countries, vote_average, vote_count, images = (
        movie_data.form.get(field, '') for field in ['title', 'overview', 'release_date', 'genres', 'poster_path', 'countries', 'vote_average', 'vote_count', 'images'])
        url = MovieController.movie_url + route_url
        private = True if private == 'on' else False
        data = {
            key: value for key, value in {
                "title": title,
                "overview": overview,
                "release_date": release_date,
                "genres": genres,
                "poster_path": poster_path,
                "countries": countries,
                "vote_average": vote_average,
                "vote_count": vote_count,
                "images": images if isinstance(images, list) else [],
                "private": private,
                "user_id": user_id
            }.items() if value
        }
        print(f'Nos data: {data}')
        return RequestAPI.request_to_api(method, url, data, 'Movie added successfully!', 'Failed to add movie!')

    @staticmethod
    def edit_movie(updated_data, route_url, method):
        private = updated_data.form.get('private', '')
        title, overview, release_date, genres, poster_path, countries, vote_average, vote_count, images = (
            updated_data.form.get(field, '') for field in ['title', 'overview', 'release_date', 'genres', 'poster_path', 'countries', 'vote_average', 'vote_count', 'images']
        )
        data = {
            key: value for key, value in {
                "title": title,
                "overview": overview,
                "release_date": release_date,
                "genres": genres,
                "poster_path": poster_path,
                "countries": countries,
                "vote_average": vote_average,
                "vote_count": vote_count,
                "images": images if isinstance(images, list) else [],
                "private": private
            }.items() if value
        }
        url = "{}/{}".format(MovieController.movie_url, route_url)
        return RequestAPI.request_to_api("PUT", url, data, f'Movie updated successfully!', f'Failed to update movie!')

    @staticmethod
    def delete_movie(route_url, method):
        url = "{}/{}".format(MovieController.movie_url, route_url)
        return RequestAPI.request_to_api(method, url, None, f'Movie deleted successfully!', f'Failed to delete movie!')

    @staticmethod
    def search_movie(query, fields, route_url, method):
        url = "{}/{}".format(MovieController.movie_url, route_url)
        data = {"query": query, "fields": fields}
        return RequestAPI.request_to_api(method, url, data, f'Search completed successfully!', f'Failed to complete search!')

    @staticmethod
    def add_comment(comment_data, route_url, method):
        url = "{}/{}".format(MovieController.movie_url, route_url)
        data = {"comment": comment_data}
        return RequestAPI.request_to_api(method, url, data, f'Comment added successfully!', f'Failed to add comment!')

    @staticmethod
    def add_rating(rating_data, route_url, method):
        url = "{}/{}".format(MovieController.movie_url, route_url)
        data = {"rating": rating_data}
        return RequestAPI.request_to_api(method, url, data, f'Rating added successfully!', f'Failed to add rating!')

    @staticmethod
    def get_images(route_url, method):
        url = "{}/{}".format(MovieController.movie_url, route_url)
        return RequestAPI.request_to_api(method, url, None, f'Images retrieved successfully!', f'Failed to retrieve images!')
    
    # @staticmethod
    # def get_videos(route_url, method):
    #     pass

    # @staticmethod
    # def get_watch_providers(movie_id):
    #     pass
