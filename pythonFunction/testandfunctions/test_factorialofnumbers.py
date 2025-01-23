from unittest import TestCase
import factorialofnumbers

class TestFactorialOfNumbers(TestCase):
	def test_that_factorial_of_number_exists(self):
		factorialofnumbers.get_factorial(6)

	def test_that_reversed_number_returns_correct_value(self):
		actual = factorialofnumbers.get_factorial(5)
		expected = 120
		self.assertEqual(actual, expected)
