from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import InvalidPlayerIdException, InvalidCharacterIdException


class Player:

    def __init__(self, player_id: int, char_name: Char):
        self.__validate_player_id(player_id)
        self.__validate_char(char_name)
        self.__player_id = player_id
        self.__char = char_name

    @property
    def player_id(self):
        return self.__player_id

    @player_id.setter
    def player_id(self, player_id):
        self.__player_id = player_id

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char_name):
        self.__char = char_name

    def __validate_char(self,char_name):
        if char_name not in [Char.char_x.value, Char.char_o.value, Char.char_empty.value]:
            raise InvalidCharacterIdException("Character must be X or O or empty")
        return True


    def __validate_player_id(self, player_id):
        if player_id < 1 or player_id > 2:
            raise InvalidPlayerIdException("Player ID must be between 1 and 2")
        return True
