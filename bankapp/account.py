from User_diary_application.exception import IncorrectPinException


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

    @password.setter
    def password(self, password):
        if password != self.__password:
            raise IncorrectPinException()

    def check_balance(self, password):
        if password != self.__password:
            raise IncorrectPinException("Passwords don't match")
        return self.__balance

    # @balance.setter
    # def balance(self, value):
    #     self.__balance = value