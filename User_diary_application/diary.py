from random import randint

from User_diary_application.entry import Entry
from User_diary_application.exception import IncorrectPinException, LockedStateException, NotFoundException


def generate_id():
    return randint(1, 9)


class Diary:
    # diaries = []

    def __init__(self, username, password):
        self.entry_id = generate_id()
        self._username = username
        self._password = password
        self.entries = []
        self.lock = True
        # self.diaries.append(self)
        # self.entry = Entry(self.generate_id(), title, body)

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError('password cannot be Empty.')
        self._password = password

    @username.setter
    def username(self, username):
        if not username:
            raise ValueError('username cannot be Empty.')
        self._username = username

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
        generated_id = generate_id()
        new_entry = Entry(generated_id, title, body)
        self.entries.append(new_entry)
        # print(self.entries)

    def get_diary_size(self):
        return len(self.entries)

    def delete_entry_by_id(self, entry_id: int):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot delete entry.")
        for entry in self.entries:
            if entry.entry_id_number == entry_id:
                self.entries.remove(entry)

        return NotFoundException(f"Entry with id {entry_id} not found")


    def find_entry_by_id(self, entry_id: int):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot find entry.")

        for entry in self.entries:
            if entry.entry_id_number == entry_id:
                return str(entry)

        return NotFoundException(f"Entry with id {entry_id} not found")

    def update_entry(self, entry_id, title, body):
        if self.lock:
            raise LockedStateException("Diary is locked. Cannot update entry.")

        for entry in self.entries:
            if entry.entry_id_number == entry_id:
                entry.set_title(title)
                entry.set_body(body)

        return NotFoundException("Entry with id {entry_id} not found")

#     def __str__(self):
#         return f"{self.username} - {self.password} - {self.entry_id}- {self.entries}"
#
#     def __repr__(self):
#         return f"{self.username} - {self.password} - {self.entry_id}- {self.entries}"
#
#
#
#
#
# my_diary = Diary("bimbola", "password")
# my_diary.unlock_diary("password")
# my_diary.create_entry("hi", "how are you")
# print(my_diary)
#
# my_diary = Diary("bimbola1", "password1")
# my_diary.unlock_diary("password1")
# my_diary.create_entry("bimbola2", "password2")
# print(my_diary)
# print(Diary.diaries)
#






