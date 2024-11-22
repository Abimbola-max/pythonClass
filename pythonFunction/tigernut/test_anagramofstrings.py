from unittest import TestCase
import anagramofstrings

class TestAnagramOfStrings(TestCase):
	def test_that_get_anagram_of_strings_exist(self):
		anagramofstrings.get_anagram_of_strings("silent", "listen")

	def test_that_get_anagram_of_strings_exist(self):
		actual = anagramofstrings.get_anagram_of_strings("madam", "leave")
		expected = False
		self.assertEqual(actual, expected)

	def  test_that_get_anagram_of_strings_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, anagramofstrings.get_anagram_of_strings, 1234)