from unittest import TestCase
import primenumbers

class TestPrimeNumbers(TestCase):
	def test_that_prime_numbers_exist(self):
		primenumbers.get_prime_numbers(7)

	def test_that_prime_numbers_returns_false_as_output(self):
		actual = primenumbers.get_prime_numbers(8)
		expected = False
		self.assertEqual(actual, expected)

	def test_that_prime_numbers_returns_true_as_output(self):
		actual = primenumbers.get_prime_numbers(7)
		expected = True
		self.assertEqual(actual, expected)