
from unittest import TestCase
import multiplicationofnumbers

class TestMultiplicationOfNumbers(TestCase):
	def test_that_multiplication_of_numbers_exists(self):
		multiplicationofnumbers.get_multiply(9,5)
	

	def test_that_multiplication_of_numbers_returns_correct_value(self):
		actual = multiplicationofnumbers.get_multiply(3,4)
		expected = 12
		self.assertEqual(actual, expected)
	
	def test_that_multiplication_of_numbers_returns_float_value(self):
		actual = multiplicationofnumbers.get_multiply(30.6,4)
		expected = 122.4
		self.assertEqual(actual, expected)

	def test_that_multiplication_of_numbers_returns_exception_with_zero_input(self):
		actual = multiplicationofnumbers.get_multiply(0,1)
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_multiplication_of_numbers_returns_negative_value(self):
		actual = multiplicationofnumbers.get_multiply(-20, 5)
		expected = -100
		self.assertEqual(actual, expected)

	def test_that_multiplication_of_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, multiplicationofnumbers.get_multiply, "bmbola")


		







