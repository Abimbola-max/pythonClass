from unittest import TestCase
import maximumnumbers


class TestSquareOfNumber(TestCase):
	def test_that_square_of_number_exists(self):
		maximumnumbers.get_maximum_numbers([1,2,4,4,5,6])

	def test_that_reversed_number_returns_correct_value(self):
		actual = maximumnumbers.get_maximum_numbers([1,2,4,4,5,6,60,100,120,200])
		expected = 200
		self.assertEqual(actual, expected)
