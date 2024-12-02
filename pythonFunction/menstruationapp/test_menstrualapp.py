from unittest import TestCase
import menstualapp

class TestPizzaWahala(TestCase):
	def test_that_pizza_wahala_exists(self):
		pizzawahala.welcome_message()

	def test_that_pizza_wahala_returns_correct_output(self):
		actual = pizzawahala.welcome_message()
		expected = "Welcome to Iya Moses Pizza joint!! The best pizza you would ever get and i can bet that"
		self.assertEqual(actual, expected)

	def test_that_pizza_wahala_returns_correct_output(self):
		actual = pizzawahala.number_Of_Guest()
		expected = "Enter number of birthday guests"
		self.assertEqual(actual, expected)