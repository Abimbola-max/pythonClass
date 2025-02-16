import random

from bankapp.Exception import NullPointerException, InvalidPasswordException
from diaryapplication.entry import Entry
from diaryapplication.exception import LockedStateException


class Diary:

    def __init__(self, username, password):
        if not username:
            raise NullPointerException("Username cannot be Empty")
        if not password:
            raise NullPointerException("Password cannot be Empty")
        self.__username = username
        self.__password = password
        self.lock = True
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
        if self.is_locked() == False:
            raise LockedStateException("Diary is locked, unlock diary to create entry")
        self.entries.append(Entry(self.generate_id(), title, body))

    def generate_id(self):
        return random.randint(1, 900)



