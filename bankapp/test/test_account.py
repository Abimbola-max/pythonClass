import unittest

from User_diary_application.exception import IncorrectPinException
from bankapp.account import Account

class MyAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.account = Account(1, "firstname", "lastname", "password")


    def test_that_account_can_check_balance_and_returns_default_balance(self):
        self.assertEqual(0, self.account.balance)

    def test_that_incorrect_password_raises_invalid_pin_exception(self):
        self.assertRaises(IncorrectPinException, self.account.check_balance, "pass")

