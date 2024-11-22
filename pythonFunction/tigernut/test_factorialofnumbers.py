from unittest import TestCase
import factorialofnumbers


class TestFactorialOfNumbers(TestCase):
	def test_that_factorial_of_numbers_exists(self):
		factorialofnumbers.get_factorial_of_numbers(5)

	def test_that_factorial_of_numbers_returns_correct_value(self):
		actual = factorialofnumbers.get_factorial_of_numbers(5)
		expected = 120
		self.assertEqual(actual, expected)

	def test_that_factorial_of_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, factorialofnumbers.get_factorial_of_numbers, "bimbola")

	

