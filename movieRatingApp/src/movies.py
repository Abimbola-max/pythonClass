from movieRatingApp.exceptions.exception import *
from movieRatingApp.src.movie import Movie


class Movies:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title):
        if title in self.movies:
            raise MovieAlreadyExistException(f"Movie '{title}' already exists.")

        movie = Movie(title)
        self.movies[title] = movie
        print(f"Movie '{title}' added on {movie.date_time.strftime('%Y-%m-%d %H:%M')}.")

    def rate_movie(self, title, rating):
        if title not in self.movies:
            raise MovieNotFoundException(f"Movie '{title}' not found.")
        self.movies[title].add_rating(rating)
        print(f"Rating {rating} added for movie '{title}'.")

    def get_average_ratings(self, title):
        if title not in self.movies:
            raise MovieNotFoundException(f"Movie '{title}' not found.")
        return self.movies[title].get_average_rating()

    def view_average_ratings(self):
        if not self.movies:
            print("No movies yet.")
            return
        print("\nAverage Ratings:")
        for title, movie in self.movies.items():
            print(f"{title}: {movie.get_average_rating():.2f}")

    def display_movies(self):
        if not self.movies:
            print("No movies .")
            return
        for title, movie in self.movies.items():
            print(movie)























# class Movies:
#
#     def __init__(self):
#         self.movies = {}
#
#     def add_movie(self, title):
#         if title in self.movies:
#             raise MovieAlreadyExistException(f"Movie '{title}' already exists.")
#
#         movie = Movie(title)
#         self.movies[title] = movie
#         print(f"Movie '{title}' added on {movie.date_time.strftime('%Y-%m-%d %H:%M')}.")
#
#     def rate_movie(self, title, rating):
#         if title not in self.movies:
#             raise MovieNotFoundException(f"Movie '{title}' not found.")
#         self.movies[title].add_rating(rating)
#         print(f"Rating {rating} added for movie '{title}'.")
#
#     def get_average_ratings(self, title):
#         if title not in self.movies:
#             raise MovieNotFoundException(f"Movie '{title}' not found.")
#         return self.movies[title].get_average_rating()
#
#     def view_average_ratings(self):
#         if not self.movies:
#             print("No movies in the system yet.")
#             return
#         print("\n--- Average Ratings ---")
#         for title, movie in self.movies.items():
#             print(f"{title}: {movie.get_average_rating():.2f}")
#
#     def get_average_ratings_all_movies(self):
#         total_average = sum(movie.get_average_rating() for movie in self.movies.values())
#         return total_average / len(self.movies)
#
#     def display_movies(self):
#         for movie in self.movies.values():
#             return movie


    # def add_movie(self, title):
    #     if title in self.movies:
    #         raise MovieAlreadyExistException(f"Movie '{title}' already exists.")
    #
    #     movie = Movie(title)
    #     self.movies[title] = movie
    #     print(f"Movie '{title}' added on {movie.date_time.strftime('%Y-%m-%d %H:%M')}.")
    #
    # def rate_movie(self, title, rating):
    #     if title not in self.movies:
    #         raise MovieNotFoundException(f"Movie '{title}' not found.")
    #     self.movies[title].add_rating(rating)
    #     print(f"Rating {rating} added for movie '{title}'.")
    #
    # def get_average_rating(self, title):
    #     return self.movies[title].get_average_ratings()
    #
    #






