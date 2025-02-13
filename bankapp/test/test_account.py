import unittest

from User_diary_application.exception import IncorrectPinException
from bankapp.account import Account

class MyAccountTestCase(unittest.TestCase):
    def test_that_account_can_check_balance_and_returns_default_amount(self):
        account = Account(1, "firstname", "lastname", "password")
        self.assertEqual(0, account.balance)

    def test_that_incorrect_password_raises_invalid_pin_exception(self):
        account = Account(1, "firstname", "lastname", "password")
        self.assertRaises(IncorrectPinException, account.check_balance, "pass")




