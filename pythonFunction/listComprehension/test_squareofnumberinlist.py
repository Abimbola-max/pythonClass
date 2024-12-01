from unittest import TestCase
import squareofnumberinlist

class TestSumOfNumbersInAList(TestCase):
	def test_that_sum_of_numberss_exists(self):
		squareofnumberinlist.get_square_of(3)

	def test_that_sum_of_even_numbers_returns_correct_value(self):
		actual = squareofnumberinlist.get_square_of(4)
		expected = ([1,4,9,16]) 
		self.assertEqual(actual, expected)
