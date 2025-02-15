import unittest

from bankapp.bank import Bank


class MyBankTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_that_bank_can_create_account(self):
        self.bank.create_account("Femi", "Moses", "password")
        self.assertEqual(1, self.bank.get_number_of_accounts())
        self.bank.create_account("Lara", "Pelumi", "password1")
        self.assertEqual(2, self.bank.get_number_of_accounts())

    def test_that_bank_account_can_deposit_5k_checks_balance_and_returns_5K(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        self.assertEqual(1, self.bank.get_number_of_accounts())
        account_number = account.account_number
        self.bank.deposit(5_000, account_number)
        self.assertEqual(5_000, self.bank.check_balance(account_number, "password"))

    def test_that_bank_account_can_deposit_10K_and_withdrawals_4k_checks_balance_and_returns_6K(self):
        account = self.bank.create_account("Femi", "Moses", "password")
        self.assertEqual(1, self.bank.get_number_of_accounts())
        account_number = account.account_number
        self.bank.deposit(10_000, account_number)
        self.assertEqual(10_000, self.bank.check_balance(account_number, "password"))
        self.bank.withdraw(4_000, account_number, "password")
        self.assertEqual(6_000, self.bank.check_balance(account_number, "password"))

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




