from unittest import TestCase
import itemsgreater

class TestItemsGreater(TestCase):
	def test_that_items_greater_than_exists(self):
		itemsgreater.get_check(["Apple", "Fish", "Orange", "Ice", "Lime"])

	def test_that_items_greater_returns_correct_value(self):
		actual = itemsgreater.get_check(["Apple", "Fish", "Orange", "Ice", "Lime"])
		expected = (["Apple", "Orange"]) 
		self.assertEqual(actual, expected)

