import unittest

from User_diary_application.diary import Diary
from User_diary_application.exception import IncorrectPinException, LockedStateException


class MyDiaryTestCase(unittest.TestCase):

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
        my_diary.unlock_diary("password")
        self.assertFalse(my_diary.is_locked())

    def test_that_diary_can_would_not_be_unlocked_with_incorrect_pin(self):
        my_diary = Diary("username", "password")
        with self.assertRaises(IncorrectPinException):
            my_diary.unlock_diary("pasword")

    def test_that_diary_can_create_entry(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        my_diary.unlock_diary("password")
        my_diary.create_entry("fish", "protein")
        my_diary.create_entry("beef", "meat")
        self.assertEqual(2, my_diary.get_diary_size())

    def test_that_diary_cannot_perform_operation_when_locked_raises_locked_state_exception(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        with self.assertRaises(LockedStateException):
            my_diary.create_entry( "fish", "protein")

    def test_that_diary_can_find_entry_by_entry_id(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        my_diary.unlock_diary("password")
        my_diary.create_entry("fish", "protein")
        my_diary.create_entry("beef", "meat")

        self.assertEqual("fish protein", my_diary.find_entry_by_id(1))

    def test_that_diary_can_delete_and_find_entry_by_entry_id(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        my_diary.unlock_diary("password")
        my_diary.create_entry("fish", "protein")
        my_diary.create_entry("beef", "meat")
        my_diary.delete_entry_by_id(2)
        self.assertEqual("fish protein", my_diary.find_entry_by_id(1))

    # def test_that_diary_entry_can_be_deleted_and_return_size(self):
    #     my_diary = Diary("username", "password")
    #     my_diary.is_locked()
    #     my_diary.unlock_diary("password")
    #     my_diary.create_entry("fish", "protein")
    #     my_diary.create_entry("beef", "meat")
    #     my_diary.create_entry("fish", "animal")
    #
    #     my_diary.delete_entry_by_id(1)
    #
    #     self.assertEqual(2, my_diary.get_diary_size())

    def test_that_diary_can_update_entry(self):
        my_diary = Diary("username", "password")
        my_diary.is_locked()
        my_diary.unlock_diary("password")
        my_diary.create_entry("fish", "protein")
        my_diary.create_entry("beef", "meat")

        my_diary.update(1, "is good", "is good also")

        self.assertEqual("is good is good also", my_diary.find_entry_by_id(1))













