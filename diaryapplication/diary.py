import random

from bankapp.Exception import NullPointerException, InvalidPasswordException
from diaryapplication.entry import Entry
from diaryapplication.exception import LockedStateException, NotFoundException


class Diary:

    def __init__(self, username, password):
        if not username:
            raise NullPointerException("Username cannot be Empty")
        if not password:
            raise NullPointerException("Password cannot be Empty")
        self.__username = username
        self.__password = password
        self.lock = True
        self.entry_id = 0
        self.entries = []

    def is_locked(self):
        return self.lock

    def unlock_diary(self, password):
        if password != self.__password:
            raise InvalidPasswordException("passwords do not match")
        self.lock = False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def get_number_of_entries(self):
        return len(self.entries)

    def create_entry(self, title: str, body: str):

            if self.is_locked():
                raise LockedStateException("Diary is locked, unlock diary to create entry")
            self.entry_id += 1
            entry_id = self.entry_id
            new_entry = Entry(entry_id, title, body)
            self.entries.append(new_entry)
            return entry_id

    # def generate_id(self):
    #     return random.randint(1, 900)

    def find_entry_by(self, entry_id)->Entry:
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry

        raise NotFoundException("Entry not found")

    def delete_entry_by(self, entry_id):
        entry = self.find_entry_by(entry_id)
        self.entries.remove(entry)

    def update_entry(self, entry_id, title, body):
        entry = self.find_entry_by(entry_id)
        entry.title = title
        entry.body = body









