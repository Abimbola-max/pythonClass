import unittest

from User_diary_application.diary import Diary


class MyDiaryTestCase(unittest.TestCase):
    def test_that_diary_can_be_created(self):
        my_diary = Diary("username", "password")

    def test_that_diary_cannot_be_created_without_username(self):
        with self.assertRaises(ValueError):
            Diary(None, "password")

    def test_that_diary_cannot_be_created_without_password(self):
        with self.assertRaises(ValueError):
            Diary("username", None)





