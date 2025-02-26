class InvalidPlayerIdException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FullCellsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)