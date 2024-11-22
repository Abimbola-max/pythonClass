from unittest import TestCase
import sumofoddnumbers

class TestSumOfOddNumbers(TestCase):
	def test_that_sum_of_odd_numbers_exist(self):
		sumofoddnumbers.get_sum_of_odd_numbers([1,2,3,4,5])

	def test_that_odd_of_even_numbers_returns_correct_value(self):
		actual = sumofoddnumbers.get_sum_of_odd_numbers([2,3,4,5,6,7,8,9])
		expected = 24
		self.assertEqual(actual, expected)

	def test_that_sum_of_odd_numbers_returns_negative_value(self):
		actual = sumofoddnumbers.get_sum_of_odd_numbers([4,-5,6,8,-9,10])
		expected = -14
		self.assertEqual(actual, expected)

	def test_that_sum_of_odd_numbers_returns_exception_with_zero_input(self):
		actual =sumofoddnumbers.get_sum_of_odd_numbers([1,-2,3,3,-4,-7,6])
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_sum_of_odd_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, sumofoddnumbers.get_sum_of_odd_numbers, "bimbola")

	def test_that_sum_of_even_numbers_returns_float_value(self):
		actual = sumofoddnumbers.get_sum_of_odd_numbers([2.0, 3.0, 6.0, 4.0, 9, 11.3])
		expected = 23.3
		self.assertEqual(actual, expected)

