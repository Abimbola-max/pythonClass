class Diary:

    def __init__(self, username, password):
        if not username:
            raise ValueError('username cannot be Empty.')
        if not password:
            raise ValueError('password cannot be Empty.')
        self.username = username
        self.password = password
        self.entries = []
        is_locked = True

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

