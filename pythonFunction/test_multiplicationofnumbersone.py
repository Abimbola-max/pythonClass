from unittest import TestCase
import multiplicationofnumbersone

class TestMultiplicationOfNumbersOne(TestCase):
	def test_that_multiplication_of_numbers_one_exists(self):
		multiplicationofnumbersone.get_multiply(2.3,5.6)

	def test_that_multiplication_of_numbers_one_returns_correct_value_with_float(self):
		actual = multiplicationofnumbersone.get_multiply(2.3, 5.6)
		expected = 12.88
		self.assertEqual(actual, expected)
