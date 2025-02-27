import unittest

from multipleofnumbers import get_multiple_of_numbers


class MyMultipleOfNumbersTestCase(unittest.TestCase):
    def test_that_my_multiple_of_number(self):
       actual = get_multiple_of_numbers(1, 10, 2)
       expected = [2,4,6,8,10]
       self.assertEqual(actual, expected)

    def test_that_my_multiple_of_number_2(self):
        actual = get_multiple_of_numbers(1, 15, 3)
        expected = [3, 6, 9, 12, 15]
        self.assertEqual(actual, expected)
