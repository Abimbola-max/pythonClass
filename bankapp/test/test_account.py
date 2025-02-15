import unittest

from bankapp.Exception import InvalidPasswordException
from bankapp.account import Account

class MyAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.account = Account(1, "firstname", "lastname", "password")

    def test_that_account_can_check_balance_and_returns_default_balance(self):
        self.assertEqual(0, self.account.balance)

    def test_that_incorrect_password_raises_invalid_pin_exception(self):
        self.assertRaises(InvalidPasswordException, self.account.check_balance, "pass")

    def test_that_account_deposit_6k_returns_6k_as_balance(self):
        self.account.increase_amount_by(6_000)
        self.assertEqual(6_000, self.account.balance)

    def test_that_account_deposit_6k_withdraws_2k_returns_4k_as_balance(self):
        self.account.increase_amount_by(6_000)
        self.assertEqual(6_000, self.account.balance)
        self.account.decrease_amount_by(2_000, "password")
        self.assertEqual(4_000, self.account.balance)

    def test_that_account_can_buy_airtime_2k_after_deposit_of_5K(self):
        self.account.increase_amount_by(5_000)
        self.assertEqual(5_000, self.account.balance)
        self.account.buy_airtime(2_000, "08118245363", "GLO", "password")
        self.assertEqual(3_000, self.account.balance)





