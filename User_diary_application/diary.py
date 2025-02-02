from User_diary_application.entry import Entry
from User_diary_application.exception import IncorrectPin, LockedState


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
            raise IncorrectPin('Password does not match.')
        self.lock = True

    def unlock_diary(self, password):
        if password != self.password:
            raise IncorrectPin('Password does not match.')
        self.lock = False

    def create_entry(self, entry_id: int, title: str, body: str):
        if self.lock:
            raise LockedState("Diary is locked. Cannot add entry.")
        new_entry = Entry(entry_id, title, body)
        self.entries.append(new_entry)

    def get_diary_size(self):
        return len(self.entries)



