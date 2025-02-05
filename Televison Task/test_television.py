import unittest

from exception import VolumeException, ChannelTypeException
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

    def test_that_television_also_raises_a_mute_exception_if_volume_is_zero(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.decrease_volume()
        with self.assertRaises(VolumeException):
            tv.decrease_volume()

    def test_that_television_can_put_chanel_down_once_raise_an_exception(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.decrease_channel()
        with self.assertRaises(ChannelTypeException):
            tv.decrease_channel()

    def test_that_television_can_put_chanel_up(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.increase_channel()
        self.assertEqual(4, tv.channel)

    def test_that_television_can_increase_volume_twice_and_decrease_volume_once_return_ten(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.increase_volume()
        tv.increase_volume()
        tv.decrease_volume()
        self.assertEqual(10, tv.volume)

    def test_that_television_can_increase_channel_twice_and_reduce_channel_once_return_four(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.increase_channel()
        tv.increase_channel()
        tv.decrease_channel()
        self.assertEqual(4, tv.channel)

    def test_that_television_can_set_channel_to_a_preferred_channel(self):
        tv = Television()
        tv.is_tv_on()
        tv.turn_on()
        tv.set_channel(22)
        self.assertEqual(22, tv.channel)
        tv.set_channel(26)
        self.assertEqual(26, tv.channel)







