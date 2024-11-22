from unittest import TestCase
import averagenumbers

class TestAverageNumbers(TestCase):
	def test_that_average_numbers_exist(self):
		averagenumbers.get_average_numbers([1,2,4,5,6,7])

	def test_that_average_numbers_returns_correct_value(self):
		actual = averagenumbers.get_average_numbers([2,4,5,6,7,5,6])
		expected = 5
		self.assertEqual(actual, expected)


	def test_that_average_numbers_returns_negative_value(self):
		actual = averagenumbers.get_average_numbers([-3,5,7,-6, -10])
		expected = -1.4
		self.assertEqual(actual, expected)

	def test_that_average_numbers_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError,averagenumbers.get_average_numbers, "bimbola")
