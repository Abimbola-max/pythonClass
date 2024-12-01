from unittest import TestCase
import numbergreaterthan

class TestNumberGreaterThan(TestCase):
	def test_that_numbers_that_number_greater_exists(self):
		numbergreaterthan.get_number_greater([1, 3, 15, 9, 14, 8, 11])

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = numbergreaterthan.get_number_greater([3, 14, 9,7,11,6])
		expected = [14, 11]
		self.assertEqual(actual, expected)


 