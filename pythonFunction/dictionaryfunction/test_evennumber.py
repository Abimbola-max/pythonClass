from unittest import TestCase
import evennumber

class TestEvenNumbers(TestCase):
	def test_that_even_numberss_exists(self):
		evennumber.get_even({1,2,3})

	def test_that_sum_of_numbers_returns_correct_value(self):
		actual = evennumber.get_even({1,2,3,4,5,6,7,8,9,10})
		expected = {2:4, 4:16, 6:36, 8:64, 10:100} 
		self.assertEqual(actual, expected)
