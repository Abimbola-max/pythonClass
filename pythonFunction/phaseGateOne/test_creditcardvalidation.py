import unittest

import creditcardvalidation


class TestCreditCardValidator(unittest.TestCase):
    def test_that_credit_card_validator_exists(self):
        creditcardvalidator.get_sum_of_doubled_odd_place("5399831619690404")

    def test_that_credit_card_validator_returns_correct_value(self):
        actual = creditcardvalidator.get_sum_of_doubled_odd_place("5399831619690404")
        expected = 47
        self.assertEqual(actual, expected)





