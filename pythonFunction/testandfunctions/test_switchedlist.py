from unittest import TestCase
import switchedlist

class TestSwitchedList(TestCase):
	def test_that_switched_list_exist(self):
		x = [1, 3, 5, 7, 4, 9]
		y = 2
		switchedlist.get_switched_list(x, y)