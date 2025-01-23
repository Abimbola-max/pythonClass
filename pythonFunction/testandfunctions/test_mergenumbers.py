from unittest import TestCase
import mergenumbers 

class TestMergeNumbers(TestCase):
	def test_that_merge_numbers_exists(self):
		mergenumbers.get_numbers_in_one([1, 3, 5, 9])

	def test_that_merge_numbers_returns_correct_value(self):
		actual = mergenumbers.get_numbers_in_one([1, 3, 5, 9,7])
		expected = [[1,3],[5,9,7]]
		self.assertEqual(actual, expected)

	