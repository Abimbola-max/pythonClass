from unittest import TestCase
import valuesonly

class TestValuesOnly(TestCase):
	def test_values_only_exists(self):
		valuesonly.only_value({"name":"Alice","age": 25,"city":"New York"})

	def test_that_two_lists_returns_correct_value(self):
		actual = valuesonly.only_value({"name":"Alice","age": 25,"city": "New York"})
		expected = ['Alice', 25, 'New York']
		self.assertEqual(actual, expected)