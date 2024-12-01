from unittest import TestCase
import elementsinoddpositions 

class TestElementsInOddPositions(TestCase):
	def test_that_elements_in_odd_position_exists(self):
		elementsinoddpositions.get_odd_positions([1,2,4,6,7,8,8,9,3])

	def test_that_elements_in_odd_position_returns_correct_value(self):
		actual = elementsinoddpositions.get_odd_positions([1,2,4,6,7,8,8,9,3])
		expected = ([2,6,8,9])
		self.assertEqual(actual, expected)

		
		