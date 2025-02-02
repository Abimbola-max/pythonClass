import unittest

from User_Diary.diaryapplication.entry import Entry


class MyEntryTestCase(unittest.TestCase):
    def test_that_entry_is_empty(self):
        entry = Entry(0, "", "")
        self.assertTrue(entry.is_empty())



