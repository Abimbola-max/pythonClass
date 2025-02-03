import unittest

from User_diary_application.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def test_that_diaries_can_add_password_username(self):
        diaries = Diaries()
        diaries.add("username","password")
        diaries.add("username1","password1")

    def test_that_diaries_can_add_multiple_users_and_return_number_of_diary(self):
        diaries = Diaries()
        diaries.add("username","password")
        diaries.add("username1","password1")

        self.assertEqual(2, diaries.get_number_of_diary())

    def test_that_diaries_can_find_user_by_username(self):
        diaries = Diaries()
        diaries.add("username","password")
        diaries.add("username1","password1")
        found_diary = diaries.find_by_username("username")
        self.assertEqual("username", found_diary.getUsername())
        actual = diaries.get_number_of_diary()
        self.assertEqual(1, actual)

