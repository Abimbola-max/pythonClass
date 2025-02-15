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

    # def test_that_account_can_transfer_from_A_to_B(self):
    #     sender_account = Account(1, "firstname", "lastname", "password")
    #     recipient_account = Account(2, "firstname1", "lastname1", "password1")
    #     sender_account.increase_amount_by(1000)
    #     self.assertEqual(1000, sender_account.balance)
    #     self.account = transfer(sender_account, amount, recipient_account, password)
    #     self.assertEqual(500, recipient_account.balance)
    #     self.assertEqual(500, sender_account.balance)


