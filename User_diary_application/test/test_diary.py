import unittest

from User_diary_application.diary import Diary
from User_diary_application.exception import IncorrectPin


class MyDiaryTestCase(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("username", "password")

    def test_that_diary_can_be_created(self):
        Diary("username", "password")

    def test_that_diary_cannot_be_created_without_username(self):
        with self.assertRaises(ValueError):
            Diary(None, "password")

    def test_that_diary_cannot_be_created_without_password(self):
        with self.assertRaises(ValueError):
            Diary("username", None)

    def test_that_diary_is_locked(self):
        my_diary = Diary("username", "password")
        self.assertTrue(my_diary.is_locked())

    def test_that_diary_can_be_unlocked_using_correct_password(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        self.assertTrue(my_diary.unlock_diary("password"))

    def test_that_diary_can_would_not_be_unlocked_with_incorrect_pin(self):
        my_diary = Diary("username", "password")
        with self.assertRaises(IncorrectPin):
            my_diary.unlock_diary("pasword")

    def test_that_diary_can_create_entry(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        my_diary.unlock_diary("password")
        my_diary.create_entry(1,"fish", "protein")
        my_diary.create_entry(2,"beef", "meat")
        self.assertEqual(2, my_diary.get_diary_size())








