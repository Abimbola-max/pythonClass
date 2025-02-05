import unittest


class MyTelevisionTestCase(unittest.TestCase):
    def test_that_television_is_off_by_default(self):
        self.assertEqual(True, television.is_on())  # add assertion here

