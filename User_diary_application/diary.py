class Diary:

    def __init__(self, username, password):
        if not username:
            raise ValueError('username cannot be Empty.')
        if not password:
            raise ValueError('password cannot be Empty.')
        self.username = username
        self.password = password
        self.entries = []
        self.lock = True

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def setUsername(self, username):
        self.username = username

    def is_locked(self):
        return self.lock

    def lock_diary(self, password):
        if password != self.password:
            raise ValueError('Password does not match.')
        self.lock = True

    def is_unlocked(self, password):
        if self.password_validation(password):
            self.lock = False

        return True

    def password_validation(self, password):
        if self.password != password:
            raise ValueError('Password does not match.')
        return True



