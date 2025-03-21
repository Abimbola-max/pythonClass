import unittest

from movieTask.src.movies import Movies


class MyTestCase(unittest.TestCase):
    def test_that_movie_can_be_added(self):
        movie = Movies()
        movie.add_movie("beauty")
        self.assertEqual(1, movie.numbers_of_movies())

    def test_that_movie_


