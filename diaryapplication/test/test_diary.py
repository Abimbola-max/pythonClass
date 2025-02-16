import unittest

from bankapp.Exception import NullPointerException
from diaryapplication.diary import Diary


class MyDiaryTestCase(unittest.TestCase):

    def test_that_i_can_create_a_diary(self):
        username = "username"
        password = "password"
        my_diary = Diary(username, password)

        self.assertEqual(username, my_diary.username)
        self.assertEqual(password, my_diary.password)

    def test_that_my_diary_can_throw_null_exception_if_username_field_is_empty(self):
        with self.assertRaises(NullPointerException):
            Diary(None, "password")

    def test_that_my_diary_can_throw_null_exception_if_password_field_is_empty(self):
        with self.assertRaises(NullPointerException):
            Diary("username", None)

    def test_that_my_diary_can_create_entries_and_return_number_of_entries(self):
        username = "username"
        password = "password"
        my_diary = Diary(username, password)
        self.assertIsNotNone(username, password)
        my_diary.create_entry("title", "body")
        self.assertEqual(1, my_diary.get_number_of_entries())
        my_diary.create_entry("title2", "body2")
        self.assertEqual(2, my_diary.get_number_of_entries())
        my_diary.create_entry("title3", "body3")
        self.assertEqual(3, my_diary.get_number_of_entries())




