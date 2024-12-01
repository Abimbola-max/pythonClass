from unittest import TestCase
import squareofnumbers

class TestSumOfNumbers(TestCase):
	def test_that_square_of_numbers_exists(self):
		squareofnumbers.get_squared([1,2,3,5,6])

	def test_that_square_of_numbers_returns_correct_value(self):
		actual = squareofnumbers.get_squared([1,2,3])
		expected = [2,4,6] 
		self.assertEqual(actual, expected)
