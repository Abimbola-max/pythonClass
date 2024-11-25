from unittest import TestCase
import sumofnumbers

class TestSumOfNumbers(TestCase):
	def test_that_sum_of_numbers_exists(self):
		x = [3,6,8,2]
		sumofnumbers.get_sum_of_numbers(x)

	def test_that_sum_of_numbers_returns_correct_value(self):
		actual = sumofnumbers.get_sum_of_numbers([3, 4, 9,7])
		expected = 23
		self.assertEqual(actual, expected)

	def test_that_sum_of_numbers_returns_negative_value(self):
		actual = sumofnumbers.get_sum_of_numbers([-20, 4, 9,-5])
		expected = -12
		self.assertEqual(actual, expected)

	def test_that_sum_of_numbers_returns_exception_with_zero_input(self):
		actual = sumofnumbers.get_sum_of_numbers([-20, 10, 5, 5])
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_sum_of_numbers_returns_floating_value(self):
		actual = sumofnumbers.get_sum_of_numbers([3.0, 4.5, 9.0,7.5])
		expected = 24.0
		self.assertEqual(actual, expected)




