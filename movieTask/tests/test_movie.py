import unittest

from movieTask.src.movie import Movie


class MyMovieTestCase(unittest.TestCase):
    def test_that_movie_can_add_rating(self):
        movie = Movie("beauty")
        movie.add_rating(5)
        self.assertEqual(movie.rating, [5])
