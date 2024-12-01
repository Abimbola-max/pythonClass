from unittest import TestCase
import sumofnumbers

class TestSumOfNumbers(TestCase):
	def test_that_sum_of_numberss_exists(self):
		sumofnumbers.get_add(1923)

	def test_that_sum_of_numbers_returns_correct_value(self):
		actual = sumofnumbers.get_add(192374)
		expected = 26 
		self.assertEqual(actual, expected)
