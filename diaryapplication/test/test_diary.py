import unittest
from datetime import datetime

from bankapp.Exception import NullPointerException, InvalidPasswordException
from diaryapplication.diary import Diary
from diaryapplication.exception import LockedStateException, NotFoundException


class MyDiaryTestCase(unittest.TestCase):

    def test_that_i_can_create_a_diary(self):
        username = "username"
        password = "password"
        my_diary = Diary(username, password)
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
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
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
        self.assertIsNotNone(username, password)
        my_diary.create_entry("title", "body")
        self.assertEqual(1, my_diary.get_number_of_entries())
        my_diary.create_entry("title2", "body2")
        self.assertEqual(2, my_diary.get_number_of_entries())
        my_diary.create_entry("title3", "body3")
        self.assertEqual(3, my_diary.get_number_of_entries())

    def test_that_diary_can_would_not_be_unlocked_with_incorrect_pin(self):
        my_diary = Diary("username", "password")
        with self.assertRaises(InvalidPasswordException):
            my_diary.unlock_diary("pasword")

    def test_that_diary_cannot_perform_operation_when_locked_raises_locked_state_exception(self):
        my_diary = Diary("username", "password")
        self.assertEqual(True, my_diary.is_locked())
        with self.assertRaises(LockedStateException):
            my_diary.create_entry("fish", "protein")

    def test_that_diary_can_find_entry_by_entry_id(self):
        my_diary = Diary("username", "password")
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
        entry_id_one = my_diary.create_entry("fish", "protein")
        entry_id_two = my_diary.create_entry("beef", "meat")
        found_entry_two = my_diary.find_entry_by(entry_id_two)
        self.assertEqual("beef meat", found_entry_two.__str__())
        found_entry_one = my_diary.find_entry_by(entry_id_one)
        self.assertEqual("fish protein", found_entry_one.__str__())

    def test_that_diary_can_delete_and_by_entry_id_returns_number_of_entries(self):
        my_diary = Diary("username", "password")
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
        entry_id_one = my_diary.create_entry("fish", "protein")
        entry_id_two = my_diary.create_entry("beef", "meat")
        my_diary.delete_entry_by(entry_id_one)
        self.assertEqual(1, my_diary.get_number_of_entries())
        my_diary.delete_entry_by(entry_id_two)
        self.assertEqual(0, my_diary.get_number_of_entries())

    def test_that_diary_can_create_entry_A_delete_A_throws_Not_found_exception_when_searching(self):
        my_diary = Diary("username", "password")
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
        entry_id_one = my_diary.create_entry("fish", "protein")
        entry_id_two = my_diary.create_entry("beef", "meat")
        my_diary.delete_entry_by(entry_id_one)
        self.assertEqual(1, my_diary.get_number_of_entries())
        with self.assertRaises(NotFoundException):
            my_diary.find_entry_by(entry_id_one)

    def test_that_diary_can_update_entry_find_and_retruns_size(self):
        my_diary = Diary("username", "password")
        self.assertEqual(True, my_diary.is_locked())
        my_diary.unlock_diary("password")
        self.assertEqual(False, my_diary.is_locked())
        entry_id_one = my_diary.create_entry("fish", "protein")
        set_date = datetime.now().strftime("%m/%d/%Y")
        entry_id_two = my_diary.create_entry("beef", "meat")
        my_diary.update_entry(entry_id_one, "is good", "is good also")
        self.assertEqual(2, my_diary.get_number_of_entries())
        self.assertEqual("is good is good also", my_diary.find_entry_by(entry_id_one).__str__())
        self.assertEqual(2, my_diary.get_number_of_entries())


