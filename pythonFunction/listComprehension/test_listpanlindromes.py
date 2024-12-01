from unittest import TestCase
import listpanlindromes

class TestListPalindrome(TestCase):
	def test_that_word_palindrome_exist(self):
		listpanlindromes.is_palindrome(['madam', 'apple', 'racecar'])

	def test_that_word_palindrome_returns_false_as_output(self):
		actual = listpanlindromes.is_palindrome(['madam', 'apple', 'racecar'])
		expected = ([True, False, True])
		self.assertEqual(actual, expected)
