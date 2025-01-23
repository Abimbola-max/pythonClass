from unittest import TestCase
import oddandeven 

class TestOddAndEven(TestCase):
	def test_that_odd_and_even_exists(self):
		oddandeven.get_odd_even([1, 3, 5, 9, 4, 8, 10])

	def test_that_odd_and_even_returns_correct_value(self):
		actual = oddandeven.get_odd_even([1, 2, 6, 8, 10, 12])
		expected = [False, True, True, True, True, True]
		self.assertEqual(actual, expected)

	def test_that_odd_and_even_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, oddandeven.get_odd_even, "bimbola")

	def test_that_odd_and_even_returns_only_false_output(self):
		actual = oddandeven.get_odd_even([1, 3, 5, 7, 11, 13])
		expected = [False, False, False, False, False, False]
		self.assertEqual(actual, expected)
	
	def test_that_odd_and_even_returns_only_true_output(self):
		actual = oddandeven.get_odd_even([2, 4, 6, 8, 60, 50])
		expected = [True, True, True, True, True, True]
		self.assertEqual(actual, expected)

		


