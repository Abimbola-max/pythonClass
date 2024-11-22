from unittest import TestCase
import sumofproduct

class TestSumOfProduct(TestCase):
	def test_that_sum_of_product_exist(self):
		sumofproduct.get_sum_of_product([1,2,3,4,5])

	def test_that_sum_of_product_returns_correct_value(self):
		actual = sumofproduct.get_sum_of_product([1,2,3,4,5,6])
		expected = 105
		self.assertEqual(actual, expected)