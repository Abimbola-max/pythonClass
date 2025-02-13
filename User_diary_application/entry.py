class Entry:

    def __init__(self, entry_id, title, body):
        self.entry_id_number = entry_id
        self.__title = title
        self.__body = body

    @property
    def entry_id(self):
        return self.entry_id_number

    # @id.setter
    # def id(self, value):
    #     self.__id = value

    @property
    def title(self):
        return self.__title

    @property
    def __body(self):
        return self.body

    @title.setter
    def title(self, title):
        self.__title = title

    @__body.setter
    def __body(self, body):
        self.body = body

    def __repr__(self):
        return self.__title + " " + self.__body

