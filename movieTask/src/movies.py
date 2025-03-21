from movieRatingApp.exceptions.exception import *
from movieTask.src.movie import Movie


class Movies:

    def __init__(self):
        self.movies = {}

    def add_movie(self, title: str):
        if title in self.movies:
            raise MovieAlreadyExistException(f"Movie {title} already exists")

        self.movies[title] = Movie(title)

    def numbers_of_movies(self):
        return len(self.movies)

