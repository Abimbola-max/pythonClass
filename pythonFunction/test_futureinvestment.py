from unittest import TestCase
import futureinvestment

class TestFutureInvestment(TestCase):
	def test_get_future_investment_exist(self):
		futureinvestment.get_future_investment(100 , 12, 2)

	def test_that_get_future_investment_returns_correct_value(self):
		futureinvestment.get_future_investment
		actual = futureinvestment.get_future_investment(100000 , 0.05, 3)
		expected = 579181.61
		self.assertEqual(actual, expected)

	def test_that_get_future_investment_returns_exception_with_zero_input(self):
		actual = futureinvestment.get_future_investment(0, 0.15, 2)
		expected = 0
		self.assertEqual(actual, expected)
		actual = futureinvestment.get_future_investment(0,30, 4)
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_get_future_investment_returns_negative_input(self):
		actual = futureinvestment.get_future_investment(-100000, 0.05, 3)
		expected = -579181.61
		self.assertEqual(actual, expected)

	def test_that_my_discount_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError,futureinvestment.get_future_investment, "bimbola")
		

	def test_that_get_future_investment_returns_exception_with_zero_input(self):
		actual = futureinvestment.get_future_investment(10000, 0.15, 0)
		expected = 0
		self.assertEqual(actual, expected)
		actual = futureinvestment.get_future_investment(120000,30, 0)
		expected = 0
		self.assertEqual(actual, expected)


