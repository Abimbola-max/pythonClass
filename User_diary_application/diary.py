from User_diary_application.entry import Entry
from User_diary_application.exception import IncorrectPinException, LockedStateException, NotFoundException


class Diary:

    def __init__(self, username, password):
        if not username:
            raise ValueError('username cannot be Empty.')
        if not password:
            raise ValueError('password cannot be Empty.')
        self.username = username
        self.password = password
        self.entries = []
        self.entry_id = 0
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
            raise IncorrectPinException('Password does not match.')
        self.lock = True

    def unlock_diary(self, password):
        if password != self.password:
            raise IncorrectPinException('Password does not match.')
        self.lock = False

    def create_entry(self, title: str, body: str):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot add entry.")
        new_entry = Entry(self.generate_id(), title, body)
        self.entries.append(new_entry)

    def get_diary_size(self):
        return len(self.entries)


    def delete_entry_by_id(self, entry_id: int):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot delete entry.")
        for entry in self.entries:
            if entry.get_id == entry_id:
                self.entries.remove(entry)

        return NotFoundException("Entry with id {entry_id} not found")


    def find_entry_by_id(self, entry_id: int):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot find entry.")

        for entry in self.entries:
            if entry.get_id() == entry_id:
                return str(entry)

        return NotFoundException("Entry with id {entry_id} not found")

    def generate_id(self):
        return self.entry_id + 1

    def update(self, entry_id, title, body):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot update entry.")

        for entry in self.entries:
            if entry.get_id() == entry_id:
                entry.set_title(title)
                entry.set_body(body)

        return NotFoundException("Entry with id {entry_id} not found")










