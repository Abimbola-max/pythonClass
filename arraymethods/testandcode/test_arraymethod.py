import unittest

from myarraymethod import MyArrayMethod


class TestMyArrayMethod(unittest.TestCase):
    def test_that_my_array_method_exist(self):
        array = MyArrayMethod(4)
        self.assertTrue(array.is_empty())

    def test_that_my_array_method_can_add_element(self):
        array = MyArrayMethod(4)
        array.add_element("34")
        self.assertFalse(array.is_empty())

    def test_that_my_array_method_can_add_multiple_elements(self):
        array = MyArrayMethod(4)
        array.add_element("8")
        array.extend_element([34, 45, 23])
        self.assertFalse(array.is_empty())

    def test_that_my_array_method_can_insert_element_at_a_particular_index_return_the_index(self):
        array = MyArrayMethod(4)
        array.add_element("34")
        array.add_element("8")
        array.insert_index("4", 1)
        self.assertEqual(2, array.get_index_of_an_element("8"))
        self.assertFalse(array.is_empty())