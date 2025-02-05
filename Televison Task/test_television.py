import unittest

from television import Television


class MyTelevisionTestCase(unittest.TestCase):
    def test_that_television_is_off_by_default(self):
        tv = Television()
        self.assertEqual(False, tv.is_tv_on())

    def test_that_television_is_turned_on(self):
        tv = Television()
        tv.turn_off()
        self.assertTrue(tv.turn_on())

    def test_that_television_is_turned_off(self):
        tv = Television()
        tv.is_tv_on()
        self.assertFalse(tv.turn_off())

    def test_that_television_can_increase_volume_once_and_volume_returns_ten(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.increase_volume()
        self.assertEqual(10, tv.volume)

    def test_that_television_can_increase_volume_twice_and_volume_return_fifteen(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        self.assertEqual(15, tv.volume)

    def test_that_television_can_decrease_volume_one_volume_returns_zero_also_mute(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.decrease_volume()
        self.assertEqual(0, tv.volume)





