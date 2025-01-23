from unittest import TestCase
import subtractionofnumbers




class TestSquareOfNumber(TestCase):
	def test_that_subtraction_of_number_exists(self):
		subtractionofnumbers.get_subtractNumbers(7,6)

	def test_that_subtraction_of_number_returns_correct_value(self):
		actual = subtractionofnumbers.get_subtractNumbers(4,5)
		expected = 1
		self.assertEqual(actual, expected)
