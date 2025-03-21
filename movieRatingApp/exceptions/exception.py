class MovieAlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MovieNamingException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidRatingException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MovieTitleNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MovieNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
