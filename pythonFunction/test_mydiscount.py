from unittest import TestCase
import mydiscount 

class TestMyDiscount(TestCase):
	def test_my_discount_exist(self):
		mydiscount.my_discount(50, 6)

	def test_that_my_discount_returns_correct_value(self):
		actual = mydiscount.my_discount(150,15)
		expected = 127.5
		self.assertEqual(actual, expected)
		actual = mydiscount.my_discount(2000, 13)
		expected = 1740
		self.assertEqual(actual, expected)

	def test_that_my_discount_returns_exception_with_zero_input(self):
		actual = mydiscount.my_discount(0,10)
		expected = 0
		self.assertEqual(actual, expected)
		actual = mydiscount.my_discount(0,30)
		expected = 0
		self.assertEqual(actual, expected)


	def test_that_my_discount_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, mydiscount.my_discount, "bimbola")

	def test_that_my_discount_returns_negative_value(self):
		actual = mydiscount.my_discount(-150, 15)
		expected = -127.5
		self.assertEqual(actual, expected)
		actual = mydiscount.my_discount(-1150, 5)
		expected = -1092.5	
		self.assertEqual(actual, expected)

	def test_that_my_discount_input_float_value_for_price(self):
		actual = mydiscount.my_discount(1201.7, 4)
		expected = 1153.632
		self.assertEqual(actual, expected)

	def test_that_my_discount_raises_an_error_message(self):
		self.assertRaises(TypeError, mydiscount.my_discount, "0")




	