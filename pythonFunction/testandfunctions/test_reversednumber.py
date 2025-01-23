from unittest import TestCase
import reversednumber




class TestReversedNumber(TestCase):
	def test_that_reversed_number_exists(self):
		reversednumber.get_reversed_number([1,2,4,6,7,8,8,9,3])

	def test_that_reversed_number_returns_correct_value(self):
		actual = reversednumber.get_reversed_number([1,2,4,6,7,8,8,9,3])
		expected = ([3,9,8,8,7,6,4,2,1])
		self.assertEqual(actual, expected)
