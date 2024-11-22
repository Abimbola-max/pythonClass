from unittest import TestCase
import mergednumbers

class TestMergedNumbers(TestCase):
	def test_that_get_number_merged_exist(self):
		numberOne = [3,4,9,10]
		numberTwo = [1,5,7,8]
		mergednumbers.get_number_merged(numberOne, numberTwo)

	def test_that_get_number_merged_returns_correct_value(self):
		numberOne = ([3,4,9,10,-5])
		numberTwo = ([0,-0,9,4,1])
		actual = mergednumbers.get_number_merged(numberOne, numberTwo)
		expected = ([-5,-0,0,1,3,4,4,9,9,10])
		self.assertEqual(actual, expected)
		
