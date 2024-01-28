# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# services/movie_service.py
import json
import os
from models.movie_model import Movie
from flask import jsonify

class MovieService:

    @staticmethod
    def get_movies():
        movies = MovieService._load_movies()
        return [Movie(**movie).__dict__ for movie in movies]

    @staticmethod
    def get_movie_by_id(movie_id):
        movies = MovieService._load_movies()
        for movie in movies:
            if movie['id'] == movie_id:
                return Movie(**movie).__dict__
        return None

    @staticmethod
    def create_movie(movie_data, user_id):
        movies = MovieService._load_movies()
        max_id = max(movie['id'] for movie in movies) if movies else 0
        new_movie = Movie(id=max_id + 1, **movie_data)
        movies.append(vars(new_movie))  # Use vars() to convert the object to a dictionary
        new_movie.user_id = user_id
        MovieService._save_movies(movies)
        return new_movie.__dict__

    @staticmethod
    def update_movie(movie_id, updated_data):
        movies = MovieService._load_movies()
        for i, movie in enumerate(movies):
            if movie['id'] == movie_id:
                movies[i].update(updated_data)
                MovieService._save_movies(movies)
                return Movie(**movies[i]).__dict__
        return None

    @staticmethod
    def delete_movie(movie_id):
        movies = MovieService._load_movies()
        for i, movie in enumerate(movies):
            if movie['id'] == movie_id:
                deleted_movie = Movie(**movies[i])
                del movies[i]
                MovieService._save_movies(movies)
                return deleted_movie.__dict__
        return None

    @staticmethod
    def search_movie(query, fields):
        with open('database/index.json', 'r') as f:
            index = json.load(f)
        query_words = query.lower().split()
        results = []
        for word in query_words:
            if word in index:
                results.extend(index[word])
        return [Movie(**movie).__dict__ for movie in results if any(any(word in str(movie[field]).lower().split() for word in query_words) for field in fields if field in movie)]
    
    @staticmethod
    def build_index():
        movies = MovieService._load_movies()
        index = {}
        for movie in movies:
            for field in ['title', 'overview', 'release_date', 'genres', 'poster_path', 'countries', 'vote_average', 'vote_count']:
                for word in str(movie[field]).split():
                    word = word.lower()
                    if word not in index:
                        index[word] = []
                    index[word].append(movie)
        with open('database/index.json', 'w') as f:
            json.dump(index, f)

    @staticmethod
    def add_comment(movie_id, user_id, comment_data):
        movies = MovieService._load_movies()  # Load all movies
        movie_index = next((i for i, movie in enumerate(movies) if movie['id'] == movie_id), None)  # Find the index of the movie with the given id
        if movie_index is not None:
            if set(comment_data.keys()) != {'comment'}:
                raise ValueError("Invalid comment data. Only 'comment' field is allowed.")
            comment_data['user_id'] = user_id
            movies[movie_index]['comments'].append(comment_data)  # Add the comment to the movie in the original list
            MovieService._save_movies(movies)  # Save all movies
            return movies[movie_index]
        return None

    @staticmethod
    def add_rating(movie_id, user_id, rating_data):
        movies = MovieService._load_movies()  # Load all movies
        movie_index = next((i for i, movie in enumerate(movies) if movie['id'] == movie_id), None)  # Find the index of the movie with the given id
        if movie_index is not None:
            if set(rating_data.keys()) != {'rating'}:
                raise ValueError("Invalid rating data. Only 'rating' field is allowed.")
            # Find the existing rating by the user
            rating_index = next((i for i, rating in enumerate(movies[movie_index]['ratings']) if rating['user_id'] == user_id), None)
            rating_data['user_id'] = user_id
            new_rating = {
                'user_id': user_id,
                'rating': rating_data['rating']['rating']
            }
            if rating_index is not None:
                # If a rating by the user exists, replace it
                movies[movie_index]['ratings'][rating_index] = new_rating
            else:
                # If no rating by the user exists, add a new one
                movies[movie_index]['ratings'].append(new_rating)
            MovieService._save_movies(movies)  # Save all movies
            return movies[movie_index]
        return None

    @staticmethod
    def get_images(movie_id):
        movie = MovieService.get_movie_by_id(movie_id)
        if movie:
            return movie['images']
        return None

    @staticmethod
    def _save_movies(movies):
        file_path = "database/movies.json"
        with open(file_path, "w") as file:
            json.dump(movies, file, indent=2)

    @staticmethod
    def _load_movies():
        try:
            with open('database/movies.json', 'r') as f:
                movies = json.load(f)
                # Ensure movies is a list of dictionaries
                assert isinstance(movies, list)
                assert all(isinstance(movie, dict) for movie in movies)
                return movies
        except (json.JSONDecodeError, AssertionError):
            return []

    # @staticmethod
    # def get_videos(movie_id):
    #     pass

    # @staticmethod
    # def get_watch_providers(movie_id):
    #     pass
