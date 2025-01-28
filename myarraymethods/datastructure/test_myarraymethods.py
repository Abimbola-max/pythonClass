import unittest

from datastructure.myarraymethods import MyArrayMethod


class TestMyArrayMethod(unittest.TestCase):
    def test_that_my_array_method_exist(self):
        array = MyArrayMethod(4)
        self.assertTrue(array.is_empty())

    def test_that_my_array_method_can_add_element(self):
        array = MyArrayMethod(4)
        array.add_element("34")
        self.assertFalse(array.is_empty())

    def test_that_my_array_method_can_add_multiple_elements(self):
        array = MyArrayMethod(4)
        array.add_element("8")
        array.extend_element([34, 45, 23])
        self.assertFalse(array.is_empty())

    def test_that_my_array_method_can_insert_element_at_a_particular_index_return_the_index(self):
        array = MyArrayMethod(4)
        array.add_element("34")
        array.add_element("8")
        array.insert_index("4", 1)
        self.assertEqual(2, array.get_index_of_an_element("8"))
        self.assertFalse(array.is_empty())

    def test_that_my_array_method_can_remove_element_at_a_particular_index_and_return_size(self):
        array = MyArrayMethod(4)
        array.add_element("34")
        array.add_element("8")
        array.remove_element("8")

        self.assertFalse(array.is_empty())
        self.assertEqual(1, array.len())

    def test_that_my_array_method_can_remove_element_and_return_true_if_is_empty(self):
        array = MyArrayMethod(4)
        array.add_element("7")
        array.remove_element("7")
        self.assertTrue(array.is_empty())

    def test_that_my_array_method_can_clear_all_elements_in_array_and_return_true_for_is_empty(self):
        array = MyArrayMethod(4)
        array.add_element("7")
        array.add_element("bibi")

        array.clear()
        self.assertTrue(array.is_empty())

    def test_that_my_array_method_can_count_the_number_of_occurrence_of_an_element(self):
        array = MyArrayMethod(7)
        array.add_element("7")
        array.add_element("bibi")
        array.add_element("bibi")
        array.add_element("bibi")

        self.assertEqual(3, array.count("bibi"))

    def test_that_my_array_method_does_not_contains_a_specific_element(self):
        array = MyArrayMethod(4)
        array.add_element("7")
        array.add_element("2")
        array.add_element("18")

        self.assertFalse(array.contains_element("1"))