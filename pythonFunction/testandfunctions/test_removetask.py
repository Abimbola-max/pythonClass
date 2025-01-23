from unittest import TestCase
import removetask

class TestRemoveTask(TestCase):
	def test_that_remove_task_exists(self):
		x = [1,2,4,5]
		removetask.remove_task(x)

	def test_that_remove_task_returns_correct_values(self):
		actual = removetask.remove_task([1, 2, 9, 17, 14, 12, 4])
		expected = [1, 2, 17, 14, 12, 4]
		self.assertEqual(actual, expected)
		actual = removetask.remove_task([10, 6, 90, 65, 1, 43, 40])
		expected = [10, 6, 65, 1, 43, 40]
		self.assertEqual(actual, expected)



