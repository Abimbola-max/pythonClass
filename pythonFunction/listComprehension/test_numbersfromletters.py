from unittest import TestCase
import numbersfromletters

class TestListPalindrome(TestCase):
	def test_that_word_palindrome_exist(self):
		numbersfromletters.get_letters_out('abc123df456')

	def test_that_word_palindrome_returns_false_as_output(self):
		actual = numbersfromletters.get_letters_out('abc123def456')
		expected = [1, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)