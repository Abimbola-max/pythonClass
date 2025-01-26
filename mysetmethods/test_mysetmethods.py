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