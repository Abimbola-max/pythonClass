import unittest

from datastructuresproject import mystackmethods


class MyTestCase(unittest.TestCase):
    def test_that_stack_is_empty(self):
        mystackmethods.is_empty()

