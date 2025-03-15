from ticTacToeTask.char import Characters
from ticTacToeTask.tictactoeexceptions import NullPointerException


class Player:
    existing_names = set()

    def __init__(self, name: str, character: Characters):
        self.__validate_name(name)
        self.__name = name
        self.__character = character
        self.__score = 0
        Player.existing_names.add(name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, character):
        self.__character = character

    def __validate_name(self, name):
        if name is None:
            raise NullPointerException("Name cannot be empty.")

        if name in Player.existing_names:
            raise NameError("Name already taken.")

        if not name.isalpha():
            raise NameError("Name must contain only letters.")


    def increment_score(self):
        self.__score += 1

    # def __str__(self):
    #     return 'X' + str(self.character)



