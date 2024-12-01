from unittest import TestCase
import twolists

class TestTwoLists(TestCase):
	def test_that_two_exists(self):
		twolists.get_values_keys(["name","age"], ["Alice", 25])

	def test_that_two_lists_returns_correct_value(self):
		actual = twolists.get_values_keys(["name","age","city"], ["Alice", 25, "New York"])
		expected = {'age': 25, 'city': 'New York', 'name': 'Alice'}
		self.assertEqual(actual, expected)
