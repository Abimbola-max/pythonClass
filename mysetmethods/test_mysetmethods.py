import unittest

from mysetmethods import MySet


class MySetTestCase(unittest.TestCase):
    def test_that_my_set_methods_exist(self):
        array_method = MySet(4)
        self.assertTrue(array_method.is_empty())


    def test_that_my_set_methods_can_add_items(self):
        array_method = MySet(6)
        array_method.add_element("34")
        self.assertFalse(array_method.is_empty())

    def test_that_my_set_methods_can_be_return_length_of_my_set(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.add_element("45")
        array_method.add_element("67")
        self.assertEqual(3, array_method.len())
        self.assertFalse(array_method.is_empty())

    def test_that_my_set_methods_can_remove_elements_and_return_size(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.remove_element("34")
        self.assertEqual(0, array_method.len())