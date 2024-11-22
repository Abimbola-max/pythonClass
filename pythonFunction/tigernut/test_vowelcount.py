from unittest import TestCase
import vowelcount

class TestVowelCount(TestCase):
	def test_that_vowel_count_exist(self):
		vowelcount.get_vowels("python is sweet")


	def test_that_vowel_count_returns_correct_value(self):
		actual = vowelcount.get_vowels("bimbola is a girl")
		expected = 6
		self.assertEqual(actual, expected)


	def test_that_vowel_count_returns_exception_with_zero_input(self):
		actual =vowelcount.get_vowels("bmbtgvrl")
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_vowel_count_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, vowelcount.get_vowels, 1234)
