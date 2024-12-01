from unittest import TestCase
import sumofevennumbers 

class TestSumOfNumbers(TestCase):
	def test_that_sum_of_numbers_exists(self):
		sumofevennumbers.get_sum_even_numbers([1, 3, 5, 9, 4, 8, 10])

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = sumofevennumbers.get_sum_even_numbers([3, 4, 9,7,10])
		expected = 14
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_returns_negative_value(self):
		actual = sumofevennumbers.get_sum_even_numbers([3, 6, -4, 9, 7, -10])
		expected = -8
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = sumofevennumbers.get_sum_even_numbers([3.1, 6.0, 9.4, 7, 10.0])
		expected = 16.0
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, sumofevennumbers.get_sum_even_numbers, "bimbola")




