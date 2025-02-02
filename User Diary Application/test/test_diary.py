import unittest


class MyDiaryTestCase(unittest.TestCase):
    def test_that_my_diary_is_empty(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
