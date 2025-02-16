import unittest

from diaryapplication.diaries import Diaries


class MyDiariesTestCase(unittest.TestCase):
    def test_that_users_can_register(self):
        diaries = Diaries()
        diaries.add("username", "password")
        self.assertEqual(1, diaries.get_number_of_diaries())
        diaries.add("username1", "password1")
        self.assertEqual(2, diaries.get_number_of_diaries())

    def test_that_diaries_can_find_users_by_username(self):
        diaries = Diaries()
        diary1 = diaries.add("username", "password")
        self.assertEqual(1, diaries.get_number_of_diaries())
        diary2 = diaries.add("username1", "password1")
        self.assertEqual(2, diaries.get_number_of_diaries())
        found_diary = diaries.find_by("username")
        self.assertEqual(diary1, found_diary)



