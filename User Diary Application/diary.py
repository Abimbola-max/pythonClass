class Diary:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.entries = []
        is_locked = True