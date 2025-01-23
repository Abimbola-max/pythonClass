from unittest import TestCase
import squareofnumbers




class TestSquareOfNumber(TestCase):
	def test_that_square_of_number_exists(self):
		squareofnumbers.get_square(7)

	def test_that_reversed_number_returns_correct_value(self):
		actual = squareofnumbers.get_square(9)
		expected = 81
		self.assertEqual(actual, expected)
