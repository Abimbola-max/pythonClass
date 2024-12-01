from unittest import TestCase
import consonantsonly

class TestConsonantsOnly(TestCase):
	def test_that_consonants_only_exists(self):
		consonantsonly.get_consonant(1923)

	def test_that_sum_of_numbers_returns_correct_value(self):
		actual = consonantsonly.get_consonant(["orange", "Apple", "Ice", "Beans", "Rice"])
		expected = ["rng", "ppl", "c", "Bns", "Rc"]
		self.assertEqual(actual, expected)


