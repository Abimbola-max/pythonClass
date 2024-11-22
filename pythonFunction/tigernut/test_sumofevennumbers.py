from unittest import TestCase
import sumofevennumbers

class TestSumOfEvenNumbers(TestCase):
	def test_that_sum_of_even_numbers_exist(self):
		sumofevennumbers.get_sum_of_even_numbers([1,2,3,4,5])

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = sumofevennumbers.get_sum_of_even_numbers([2,3,4,5,6,7,8,9])
		expected = 20
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_returns_negative_value(self):
		actual = sumofevennumbers.get_sum_of_even_numbers([4,5,6,-8,9,-10])
		expected = -8
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_returns_exception_with_zero_input(self):
		actual =sumofevennumbers.get_sum_of_even_numbers([1,-2,-4,5,6])
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_sum_of_even_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, sumofevennumbers.get_sum_of_even_numbers, "bimbola")

	def test_that_sum_of_even_numbers_returns_float_value(self):
		actual = sumofevennumbers.get_sum_of_even_numbers([2.0, 6.0, 4.0, 8])
		expected = 20.0
		self.assertEqual(actual, expected)


