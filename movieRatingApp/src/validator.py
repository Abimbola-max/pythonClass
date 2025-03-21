from SCMS.exceptions.exception import NullException
from movieRatingApp.exceptions.exception import *


class Validator:

    @staticmethod
    def validate_title(title: str):
        if not title:
            raise NullException("Title is required")

        # if not title.isalnum():
        #     raise MovieNamingException("Title should not contain any special characters")

    @staticmethod
    def validate_rating(rating: int):
        if rating < 1 or rating > 5:
            raise InvalidRatingException("Rating should be between 1 and 5.")

        if not isinstance(rating, int):
            raise InvalidRatingException("Rating should be a number.")

