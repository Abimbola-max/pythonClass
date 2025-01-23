from unittest import TestCase
import cubeofnumbers 

class TestCubeOfNumbers(TestCase):
	def test_that_cube_of_numbers_exists(self):
		cubeofnumbers.get_cube(3)

	def test_that_cube_of_numbers_returns_correct_value(self):
		actual = cubeofnumbers.get_cube(3)
		expected = 27
		self.assertEqual(actual, expected)
		actual = cubeofnumbers.get_cube(10)
		expected = 1000
		self.assertEqual(actual, expected)
		
	def test_that_cube_of_numbers_raise_exception_with_invalid_input(self):
		self.assetRaises(TypeError, cubeofnumbers.get_cube, "moses")

	def test_that_cube_of_numbers_returns_correct_value_with_float(self):
		actual = cubeofnumbers.get_cube(2.3)
		expected = 12.167
		self.assertEqua(actual, expected)

