class InvalidBalanceException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidAmountException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InsufficientFundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPasswordException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullPointerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AccountNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncompletePhoneNumberException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)