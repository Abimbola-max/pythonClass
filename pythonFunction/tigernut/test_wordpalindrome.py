from unittest import TestCase
import wordpalindrome

class TestWordPalindrome(TestCase):
	def test_that_word_palindrome_exist(self):
		wordpalindrome.get_palindrome("madam")

	def test_that_word_palindrome_returns_false_as_output(self):
		actual = wordpalindrome.get_palindrome("fine")
		expected = False
		self.assertEqual(actual, expected)

	def test_that_word_palindrome_returns_true_as_output(self):
		actual = wordpalindrome.get_palindrome("MADAM")
		expected = True
		self.assertEqual(actual, expected)

	def test_that_get_word_palindrome_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, wordpalindrome.get_palindrome, 12346)