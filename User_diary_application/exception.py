class IncorrectPin(Exception):
    def __init__(self, message):
        super().__init__(message)

class LockedState(Exception):
    def __init__(self, message):
        super().__init__(message)

