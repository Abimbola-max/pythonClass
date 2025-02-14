import random

from User_diary_application.exception import IncorrectPinException
from bankapp.Exception import InsufficientFundException, InvalidAmountException, InvalidPasswordException, \
    NullPointerException


class Account:

    def __init__(self, account_number, first_name, last_name, password):
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def password(self):
        return self.__password

    @property
    def account_number(self):
        return self.__account_number

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name.isEmpty():
            raise NullPointerException("First name cannot be empty")
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name.isEmpty():
            raise NullPointerException("First name cannot be empty")
        self.__last_name = last_name

    @password.setter
    def password(self, password):
        if password != self.__password:
            raise IncorrectPinException("password does not match")
        if password.isEmpty():
            raise NullPointerException("password field cannot be empty")
        self.__password = password


    def check_balance(self, password):
        if self.invalid_password(password):
            raise IncorrectPinException("Passwords don't match")
        return self.__balance

    def increase_amount_by(self, amount):
        if self.invalid_amount(amount):
            raise InvalidAmountException("Insufficient funds")
        self.__balance += amount

    def invalid_amount(self, amount):
        if amount < 0:
            return True
        return False

    def decrease_amount_by(self, amount, password):
        if self.invalid_password(password):
            raise InvalidPasswordException("Paaswords don't match")
        if self.insufficient_fund(amount):
            raise InsufficientFundException("Insufficient funds")
        self.__balance -= amount

    def insufficient_fund(self, amount):
        if amount > self.__balance:
            return True
        return False

    def invalid_password(self, password):
        if not password != self.__password:
            return True
        return False

    def update_password(self, password, new_password):
        if new_password != password:
            raise InvalidPasswordException("Passwords don't match")
        self.__password = new_password

    # def transfer(self, sender_account, amount, recipient_account, password):
    #     sender_account.withdraw(amount, password)
    #     recipient_account.deposit(amount)
    #
    # def find_account_by(self, account_number):
    #     for account in self
