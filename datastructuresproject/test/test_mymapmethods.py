import unittest

from datastructuresproject.mymapmethods import MyMap


class MyMapMethodTestCase(unittest.TestCase):
    def test_that_map_is_empty(self):
        test_map = MyMap()
        self.assertTrue(test_map.is_empty())

    def test_that_map_is_can_add_keys_and_values(self):
        test_map = MyMap()
        test_map.add('apple', 1)
        test_map.add('banana', 2)
        test_map.add('cherry', 3)





