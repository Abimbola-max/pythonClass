from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import InvalidPlayerIdException


class Player:

    def __init__(self, player_id: int, char: Char):
        self.__player_id = player_id
        self.__char = char

    @property
    def player_id(self):
        return self.__player_id

    @player_id.setter
    def player_id(self, player_id):
        if player_id < 1 or player_id > 2:
            raise InvalidPlayerIdException("Player ID must be between 1 and 2")
        self.__player_id = player_id

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char):
        if char not in [Char.char_x.value, Char.char_o.value, Char.char_empty.value]:
            raise InvalidPlayerIdException("Character must be X or O or empty")
        self.__char = char