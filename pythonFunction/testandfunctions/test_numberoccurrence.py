from unittest import TestCase
import numberoccurrence




class TestNumberOccurrence(TestCase):
	def test_that_number_occurrence_exists(self):
		 numberoccurrence.get_number_occurrence([1,2,4,6,7,8,8,9,3],9)

	def test_that_reversed_number_returns_correct_value(self):
		actual =  numberoccurrence.get_number_occurrence([1,2,4,6,7,8,8,9,3],90)
		expected = False
		self.assertEqual(actual, expected)
