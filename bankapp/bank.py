import random

from bankapp.Exception import AccountNotFoundException
from bankapp.account import Account

class Bank:

    def __init__(self):
        self.accounts = []


    def create_account(self, first_name, last_name, password):
        account = Account(self.generate_account_number(), first_name, last_name, password)
        self.accounts.append(account)
        return account

    def get_number_of_accounts(self):
       return len(self.accounts)

    def generate_account_number(self):
        random_number = random.randint(100000, 999999)
        return random_number

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        if account:
            return account.increase_amount_by(amount)

        raise AccountNotFoundException("Account not found")

    def check_balance(self, account_number, password):
        account = self.find_account(account_number)
        if account:
            return account.check_balance(password)
        raise AccountNotFoundException("Account not found")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise AccountNotFoundException("Account not found")

    def withdraw(self, amount, account_number, password):
        account = self.find_account(account_number)
        if account:
            return account.decrease_amount_by(amount, password)

        raise AccountNotFoundException("Account not found")

    def transfer(self, sender_account_number, amount, receiver_account_number, password):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)

        if not sender_account:
            raise AccountNotFoundException("Sender account not found")
        if not receiver_account:
            raise AccountNotFoundException("Receiver account not found")

        sender_account.decrease_amount_by(amount, password)
        receiver_account.increase_amount_by(amount)









