import unittest

from classTask.stringsTask.stringmethods import get_count, swap_string_and_strip, divide_and_insert, \
    display_upper_case_first, get_number_of_char, remove_character


class MyStringTestCase(unittest.TestCase):
    def test_that_string_methods_can_count_occurrence(self):
        input_string = 'semicolon.africa'
        expected = get_count(input_string)
        actual = {'s':1,'e':1,'m':1,'i':2,'c':2,'o':2,'l':1,'n':1,'.':1,'a':2,'f':1,'r':1}
        self.assertEqual(expected, actual)

    def test_that_string_methods_can_count_occurrence_two(self):
        input_string = 'bibi'
        expected = get_count(input_string)
        actual = {'b': 2, 'i': 2}
        self.assertEqual(expected, actual)

    def test_that_string_can_be_swapped_and_stripped(self):
        first_input_string = 'abc'
        second_input_string = 'xyz'
        expected = swap_string_and_strip(first_input_string, second_input_string)
        actual = 'xyc abz'
        self.assertEqual(expected, actual)

    def test_that_word_ce_can_be_added_to_the_middle_of_a_string(self):
        input_string = 'helloo'
        second_input = "ce"
        expected = divide_and_insert(input_string, second_input)
        actual = 'helceloo'
        self.assertEqual(expected, actual)

    def test_that_word_can_take_mixed_cases_and_return_words_arranged_in_mixed_cases(self):
        input_string = 'sEmIColOn'
        expected = display_upper_case_first(input_string)
        actual = 'EICOsmoln'
        self.assertEqual(expected, actual)

    def test_that_word_and_character_as_parameters_return_a_tuple(self):
        input_string = 'semicolon'
        input_char = 'o'
        expected = get_number_of_char(input_string, input_char)
        actual = ('o', 2)
        self.assertEqual(expected, actual)

    def test_that_function_removes_any_special_characters_from_the_string(self):
        input_string = 'he,ll.o'
        expected = remove_character(input_string)
        actual = 'hello'
        self.assertEqual(expected, actual)

