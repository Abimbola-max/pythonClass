import unittest

from datastructures.datastructure.mysetmethods import MySet


class MySetTestCase(unittest.TestCase):
    def test_that_my_set_methods_exist(self):
        array_method = MySet(4)
        self.assertTrue(array_method.is_empty())


    def test_that_my_set_methods_can_add_items(self):
        array_method = MySet(6)
        array_method.add_element("34")
        self.assertFalse(array_method.is_empty())

    def test_that_my_set_methods_can_be_return_length_of_my_set(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.add_element("45")
        array_method.add_element("67")
        self.assertEqual(3, array_method.len())
        self.assertFalse(array_method.is_empty())

    def test_that_my_set_methods_can_remove_elements_and_return_size(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.remove_element("34")
        self.assertEqual(0, array_method.len())

        array_method.add_element("45")
        array_method.add_element("bibi")
        array_method.remove_element("bibi")
        self.assertEqual(1, array_method.len())

    def test_that_my_set_methods_can_insert_element_at_a_particular_index(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.add_element("45")
        array_method.add_element("bibi")
        array_method.insert_element_at("tayo", 1)

        self.assertEqual(4, array_method.len())
        self.assertFalse(array_method.is_empty())

    def test_that_my_set_method_can_get_index_of_an_element(self):
        array_method = MySet(6)
        array_method.add_element("34")
        array_method.add_element("45")
        array_method.add_element("bibi")

        self.assertEqual(2, array_method.get_index_of("bibi"))
        self.assertEqual(0, array_method.get_index_of("34"))

    def test_that_my_set_method_can_clear_all_items_in_set_and_return_size_to_nothing(self):
        array_method = MySet(6)
        array_method.add_element("bolu")
        array_method.add_element("abefe")
        array_method.add_element("bibi")

        array_method.clear()
        self.assertEqual(0, array_method.len())
        self.assertTrue(array_method.is_empty())

    def test_that_my_set_method_contains_a_specific_element(self):
        array = MySet(4)
        array.add_element("7")
        array.add_element("2")
        array.add_element("18")

        self.assertTrue(array.contains_element("2"))

    def test_that_my_set_method_does_not_contains_a_specific_element(self):
        array = MySet(4)
        array.add_element("7")
        array.add_element("2")
        array.add_element("18")

        self.assertFalse(array.contains_element("1"))





