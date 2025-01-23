from unittest import TestCase
import evenandoddnumbers




class TestSquareOfNumber(TestCase):
	def test_that_square_of_number_exists(self):
		evenandoddnumbers.isEven(7)

	def test_that_reversed_number_returns_correct_value(self):
		actual = evenandoddnumbers.isEven(8)
		expected = True
		self.assertEqual(actual, expected)
