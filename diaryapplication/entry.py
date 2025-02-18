from datetime import datetime
from xmlrpc.client import DateTime

from bankapp.Exception import NullPointerException


class Entry:

    def __init__(self, entry_id, title, body):
        self.__entry_id = entry_id
        self.__title = title
        self.__body = body
        self.__date = datetime.now()

    @property
    def entry_id(self):
        return self.__entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        self.__entry_id = entry_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not title:
            raise NullPointerException("Title cannot be empty")
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        if not body:
            raise NullPointerException("Body cannot be empty")
        self.__body = body

    def __str__(self):
        return f"{self.title} {self.body} {self.__date}"
