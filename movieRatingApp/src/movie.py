import datetime

from movieRatingApp.exceptions.exception import InvalidRatingException
from movieRatingApp.src.validator import Validator


class Movie:
    def __init__(self, title):
        self.title = title
        self.ratings = []
        self.date_time = datetime.datetime.now()

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            raise InvalidRatingException("Rating must be between 1 and 5.")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        return f"Title: {self.title}, Added on: {self.date_time.strftime('%Y-%m-%d %H:%M')}, Average Rating: {self.get_average_rating():.2f}"


















# class Movie:
#
#     def __init__(self, title):
#         self.title = title
#         self.ratings = []
#         self.date_time = datetime.datetime.now()
#
#     @property
#     def title(self):
#         return self.__title
#
#     @title.setter
#     def title(self, value):
#         self.__title = value
#
#     @property
#     def date_time(self):
#         return self.__date_time
#
#     @date_time.setter
#     def date_time(self, value):
#         self.__date_time = value
#
#     def add_rating(self, rating):
#         Validator.validate_rating(rating)
#         self.ratings.append(rating)
#
#     def total_ratings(self):
#         return sum(self.ratings)
#
#     def number_of_ratings(self):
#         return len(self.ratings)
#
#     def get_average_ratings(self):
#         result =  self.total_ratings() / self.number_of_ratings()
#         return result
#
#     def __repr__(self):
#         return f'Movie title: {self.title}, was added {self.date_time.strftime("%Y-%m-%d %H:%M")}, average rating: {self.get_average_rating():.2f}.'
