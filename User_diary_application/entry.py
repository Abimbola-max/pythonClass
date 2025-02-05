class Entry:

    def __init__(self, entry_id, title, body):
        self.__id = entry_id
        self.__title = title
        self.__body = body

    def is_empty(self):
        return self.__title == "" and self.__body == ""

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_title(self, title):
        self.__title = title

    def set_body(self, body):
        self.__body = body

    def set_id(self, entry_id):
        self.__id = entry_id

    def __repr__(self):
        return "from entry class " + self.__title + " " + self.__body
