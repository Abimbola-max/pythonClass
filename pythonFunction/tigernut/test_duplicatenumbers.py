from unittest import TestCase
import duplicatenumbers


class TestDuplicateNumbers(TestCase):
	def test_that_duplicate_numbers_exists(self):
		duplicatenumbers.get_duplicate_numbers([1,2,4,4,5,6])

	def test_that_duplicate_numbers_returns_false_value(self):
		actual = duplicatenumbers.get_duplicate_numbers([1,2,4,5,6])
		expected = False
		self.assertEqual(actual, expected)

	def test_that_duplicate_numbers_returns_true_value(self):
		actual = duplicatenumbers.get_duplicate_numbers([1,2,2,4,5,6])
		expected = True
		self.assertEqual(actual, expected)