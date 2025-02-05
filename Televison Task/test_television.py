import unittest

import television


class MyTelevisionTestCase(unittest.TestCase):
    def test_that_television_is_off_by_default(self):
        tv = television.Television()
        self.assertEqual(False, tv.is_tv_on())

    def test_that_television_is_turned_on(self):
        tv = television.Television()
        self.assertEqual(True, tv.is_tv_on())

