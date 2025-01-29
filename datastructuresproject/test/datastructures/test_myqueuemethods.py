import unittest

from datastructures.myqueuemethods import MyQueue


class MyQueueMethodTestCase(unittest.TestCase):
    def test_that_my_queue_is_empty(self):
        my_queue = MyQueue(0)
        self.assertTrue(my_queue.is_empty())

    def test_that_my_queue_can_add_elements(self):
        my_queue = MyQueue(4)
        my_queue.add("50")
        my_queue.add("60")
        self.assertFalse(my_queue.is_empty())

    def test_that_my_queue_can_do_peek_method(self):
        my_queue = MyQueue(4)
        my_queue.add("50")
        my_queue.add("60")
        my_queue.add("70")

        self.assertEqual("50", my_queue.peek())

        

