class InvalidPlayerIdException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FullCellsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidRowOrColumnException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCharacterIdException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullPointerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidMoveException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)