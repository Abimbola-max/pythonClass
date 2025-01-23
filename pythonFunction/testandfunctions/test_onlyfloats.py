from unittest import TestCase
import onlyfloats

class TestOnlyFloats(TestCase):
	def test_that_only_floats_exist(self):
		onlyfloats.only_floats(50.5 , 12.2)

	def test_that_only_floats_returns_correct_value_two(self):
		actual = onlyfloats.only_floats(150.4, 15.1)
		expected = 2
		self.assertEqual(actual, expected)
		actual = onlyfloats.only_floats(34.6, 13.1)
		expected = 2
		self.assertEqual(actual, expected)

	def test_that_only_floats_returns_correct_value_one(self):
		actual = onlyfloats.only_floats(150.4, 1)
		expected = 1
		self.assertEqual(actual, expected)
		actual = onlyfloats.only_floats(34, 13.1)
		expected = 1
		self.assertEqual(actual, expected)

	def test_that_only_floats_returns_correct_value_zero(self):
		actual = onlyfloats.only_floats(15, 1)
		expected = 0
		self.assertEqual(actual, expected)
		actual = onlyfloats.only_floats(34, 13)
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_only_floats_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, onlyfloats.only_floats, "bimbola")

	def test_that_only_floats_returns_negative_input(self):
		actual = onlyfloats.only_floats(-0.10,10)
		expected = 4
		self.assertEqual(actual, expected)
		actual = onlyfloats.only_floats(-1.4, 23.3)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_only_floats_returns_negative_input_two(self):
		actual = onlyfloats.only_floats(10.6,-10.5)
		expected = 3
		self.assertEqual(actual, expected)
		actual = onlyfloats.only_floats(1.4, -30.1)
		expected = 3
		self.assertEqual(actual, expected)
	

















