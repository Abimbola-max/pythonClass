from unittest import TestCase
import palindromechecker

class TestReversedNumber(TestCase):
	def test_that_palindrome_checker_exists(self):
		palindromechecker.is_palindrome(12234)

	def test_that_palindrome_checker_returns_correct_value(self):
		actual = palindromechecker.is_palindrome(12221)
		expected = True
		self.assertEqual(actual, expected)
