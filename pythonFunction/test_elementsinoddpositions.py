from unittest import TestCase
import elementsinoddpositions 
import elementsinoddpositions

class TestElementsInOddPositions(TestCase):
	def test_that_elements_in_odd_position_exists(self):
		elementsinoddpositions.get_odd_positions([1,2,4,6,7,8,8,9,3])

	def test_that_elements_in_odd_position_returns_correct_value(self):
		actual = elementsinoddpositions.get_odd_positions([1,2,4,6,7,8,8,9,3])
		expected = ([2,6,8,9])
		self.assertEqual(actual, expected)

class TestReversedNumber(TestCase):
	def test_that_reversed_number_exists(self):
		reversednumber.get_reversed_number([1,2,4,6,7,8,8,9,3])

	def test_that_reversed_number_returns_correct_value(self):
		actual = reversednumber.get_reversed_number([1,2,4,6,7,8,8,9,3])
		expected = ([3,9,8,8,7,6,4,2,1])
		self.assertEqual(actual, expected)
		
		