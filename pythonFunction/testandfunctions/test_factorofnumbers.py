from unittest import TestCase
import factorofnumbers




class TestSquareOfNumber(TestCase):
	def test_that_factor_of_numbers_exists(self):
		factorofnumbers.get_number_of_factors(7)

	def test_that_factor_of_numbers_returns_correct_value(self):
		actual = factorofnumbers.get_number_of_factors(9)
		expected = 3
		self.assertEqual(actual, expected)
