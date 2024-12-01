from unittest import TestCase
import squareofnumberinlist

class TestSumOfNumbersInAList(TestCase):
	def test_that_sum_of_numberss_exists(self):
		sumofevennumberss.get_sum_even_numbers([1, 3, 5, 9, 4, 8, 10])

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = sumofevennumberss.get_sum_even_numbers([3, 4, 9,7,10,6])
		expected = 3
		self.assertEqual(actual, expected)
