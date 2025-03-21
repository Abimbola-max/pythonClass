import unittest

from SCMS.exceptions.exception import NullException
from movieRatingApp.src.movie import Movie


class MyTestCase(unittest.TestCase):

    def test_that_movie_can_be_added(self):
        movie_app = Movie("movie title")
        self.assertEqual("movie title", movie_app.title)
        movie_app2 = Movie("movie title2")
        self.assertEqual("movie title2", movie_app2.title)

    # def test_that_movie_can_be_rated(self):
    #     movie_app = Movie("movie title")
    #     movie_title = "born to lead"
    #     first_add = movie_app.add_movie(movie_title)
    #     self.assertIn(first_add, movie_app.show_movies())
    #     self.assertEqual(1, movie_app.number_of_movies_added())
    #     movie_rating = movie_app.rate_movie(2, movie_title)
    #     self.assertEqual(2, movie_rating.rating )
    #
    # def test_that_movie_title_field_being_empty_throws_exceptions(self):
    #     movie_app = Movie("movie title")
    #     movie_title = ""
    #     with self.assertRaises(NullException):
    #         first_add = movie_app.add_movie(movie_title)

