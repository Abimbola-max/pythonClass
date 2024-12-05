from unittest import TestCase
import phonebook

class TestPhoneBook (TestCase):

	def test_phone_book_exist(self):
		phonebook.get_contact()

	def test_that_phone_book_returns_correct_value(self):
		actual = phonebook.get_contact("Enter name ")
		expected = bimbola
		self.assertEqual(actual, expected)
		actual = phonebook.get_contact("Enter phone number")
		expected = "08118256508"
		self.assertEqual(actual, expected)

	def test_that_phone_book_returns_correct_value(self):
		actual = phonebook.get_options("Enter option")
		expected = 2
		self.assertEqual(actual, expected)
		actual = phonebook.get_options("Enter")
		expected =1
		self.assertEqual(actual, expected)

