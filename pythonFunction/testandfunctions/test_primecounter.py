from unittest import TestCase
import primecounter

class TestPrimeCounter2(TestCase):
	def test_that_prime_counter_exist(self):
		primecounter.get_prime_numbers(7)

	def test_that_prime_counter_returns_correct_input(self):
		actual = primecounter.get_prime_numbers(20)
		expected = ([2,3,5,7,9,11,13])
		self.assertEqual(actual, expected)

	