import unittest

from src.romannumeral import convert_figure_to_roman


class MyRomanTestCase(unittest.TestCase):
    def test_figure_thirty_eight_can_be_converted(self):
        number = 38
        convert = convert_figure_to_roman(number)
        answer = 'XXXVIII'
        self.assertEqual(convert, answer)

    def test_figure_one_thousand_can_be_converted(self):
        number = 1000
        convert = convert_figure_to_roman(number)
        answer = 'M'
        self.assertEqual(convert, answer)

    def test_something_one_thousand_and_one_can_be_converted(self):
            number = 1001
            convert = convert_figure_to_roman(number)
            answer = 'MI'
            self.assertEqual(convert, answer)

    def test_number_five_hundred_and_five_can_be_converted_to_roman_number(self):
            number = 505
            convert = convert_figure_to_roman(number)
            answer = 'DV'
            self.assertEqual(convert, answer)

    def test_figure_three_hundred_and_fifty_five_can_be_converted_to_roman_number(self):
            number = 355
            convert = convert_figure_to_roman(number)
            answer = 'CCCLV'
            self.assertEqual(convert, answer)

    def test_figure_two_hundred_can_be_converted_to_roman_number(self):
            number = 200
            convert = convert_figure_to_roman(number)
            answer = 'CC'
            self.assertEqual(convert, answer)

    def test_figure_six_hundred_and_twelve_can_be_converted_to_roman_number(self):
            number = 612
            convert = convert_figure_to_roman(number)
            answer = 'DCXII'
            self.assertEqual(convert, answer)

    def test_figure_four_hundred_and_ninety_can_be_converted_to_roman_number(self):
            number = 490
            convert = convert_figure_to_roman(number)
            answer = 'CDXC'
            self.assertEqual(convert, answer)

    def test_figure_hundred_and_eleven_can_be_converted_to_roman_number(self):
            number = 111
            convert = convert_figure_to_roman(number)
            answer = 'CXI'
            self.assertEqual(convert, answer)

    def test_figure_one_thousand_two_hundred_and_twenty_one_can_be_converted_to_roman_number(self):
            number = 1221
            convert = convert_figure_to_roman(number)
            answer = 'MCCXXI'
            self.assertEqual(convert, answer)

    def test_figure_one_thousand_five_hundred_and_fourty_three_can_be_converted_to_roman_number(self):
            number = 1543
            convert = convert_figure_to_roman(number)
            answer = 'MDXLIII'
            self.assertEqual(convert, answer)

    def test_figure_one_thousand_nine_hundred_and_eight_can_be_converted_to_roman_number(self):
            number = 1908
            convert = convert_figure_to_roman(number)
            answer = 'MCMVIII'
            self.assertEqual(convert, answer)

    def test_figure_two_hundred_and_ninety_two_can_be_converted_to_roman_number(self):
            number = 292
            convert = convert_figure_to_roman(number)
            answer = 'CCXCII'
            self.assertEqual(convert, answer)




if __name__ == '__main__':
    unittest.main()
