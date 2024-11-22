from unittest import TestCase
import acronyms

class TestAcronyms(TestCase):
	def test_that_acronyms_exist(self):
		acronyms.get_acronyms("Post Virgo")

	def test_that_acronyms_returns_correct_output(self):
		actual = acronyms.get_acronyms("Portable Network Graphics")
		expected = png
		self.assertEqual(actual, expected)
