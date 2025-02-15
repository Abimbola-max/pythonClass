import unittest

from bankapp.Exception import InvalidAmountException
from bankapp.bank import Bank


class MyBankTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_that_bank_can_create_two_new_accounts_returns_zero_balance(self):
        first_account = self.bank.create_account("Femi", "Moses", "password")
        first_account_number = first_account.account_number
        self.assertEqual(1, self.bank.get_number_of_accounts())
        second_account = self.bank.create_account("Lara", "Pelumi", "password1")
        second_account_number = second_account.account_number
        self.assertEqual(2, self.bank.get_number_of_accounts())

    def test_that_bank_account_can_deposit_5k_checks_balance_and_returns_5K(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        account_number = account.account_number
        self.assertEqual(1, self.bank.get_number_of_accounts())
        self.bank.deposit(5_000, account_number)
        self.assertEqual(5_000, self.bank.check_balance(account_number, "password"))

    def test_that_user_cannot_deposit_minus_5k_throws_invalid_amount_exception(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        self.assertRaises(InvalidAmountException, self.bank.deposit, -5_000, account.account_number)

    def test_that_bank_account_can_deposit_10K_and_withdrawals_4k_checks_balance_and_returns_6K(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        account_number = account.account_number
        self.assertEqual(1, self.bank.get_number_of_accounts())
        self.bank.deposit(10_000, account_number)
        self.assertEqual(10_000, self.bank.check_balance(account_number, "password"))
        self.bank.withdraw(4_000, account_number, "password")
        self.assertEqual(6_000, self.bank.check_balance(account_number, "password"))

    def test_that_user_can_deposit_5k_but_cannot_withdrawals_minus_4k_throws_invalid_amount_exception(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        account_number = account.account_number
        self.bank.deposit(5_000, account_number)
        self.assertEqual(5_000, self.bank.check_balance(account_number, "password"))
        self.assertRaises(InvalidAmountException, self.bank.deposit, -5_000, account_number)

    def test_that_account_A_can_transfer_5K_to_account_B_returns_both_accounts_balance(self):
        sender_account = self.bank.create_account("Femi", "Moses", "password")
        receiver_account = self.bank.create_account("bibi", "abimbola", "password1")

        sender_account_number = sender_account.account_number
        receiver_account_number = receiver_account.account_number

        self.bank.deposit(10_000, sender_account_number)
        self.assertEqual(10_000, self.bank.check_balance(sender_account_number, "password"))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, "password1"))

        self.bank.transfer(sender_account_number, 5_000, receiver_account_number, "password")
        self.assertEqual(5_000, self.bank.check_balance(sender_account_number, "password"))
        self.assertEqual(5_000, self.bank.check_balance(receiver_account_number, "password1"))

    def test_that_user_cannot_deposit_5K_and_transfer_minus_3k_throws_invalid_amount_exception(self):
        sender_account = self.bank.create_account("Femi", "Moses", "password")
        sender_account_number = sender_account.account_number
        receiver_account = self.bank.create_account("Tope", "Ola", "password1")
        receiver_account_number = receiver_account.account_number
        self.assertEqual(2, self.bank.get_number_of_accounts())
        self.bank.deposit(5_000, sender_account_number)
        self.assertEqual(5_000, self.bank.check_balance(sender_account_number, "password"))
        with self.assertRaises(InvalidAmountException):
            self.bank.transfer(sender_account_number, -3_000, receiver_account_number, "password")

    def test_that_bank_can_delete_user_account_if_requested_by_user(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        account_number = account.account_number
        self.assertEqual(1, self.bank.get_number_of_accounts())
        self.bank.delete_account(account_number, "password")
        self.assertEqual(0, self.bank.get_number_of_accounts())

    def test_that_user_can_buy_airtime(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        account_number = account.account_number
        self.bank.deposit(1000, account_number)
        airtime_purchase = self.bank.buy_airtime(account_number, "password", 500, "08012345678", "MTN")
        self.assertIn("Airtime of 500 successfully purchased for 08012345678 on MTN", airtime_purchase)
        self.assertEqual(500, self.bank.check_balance(account_number, "password"))




