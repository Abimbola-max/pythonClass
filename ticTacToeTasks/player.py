from ticTacToeTasks.charvalue import Char
from ticTacToeTasks.tictactoeexceptions import InvalidCharacterIdException, InvalidPlayerIdException


class Player:

    def __init__(self, player_id: int, char_value: Char):
        self.__validate_player_id(player_id)
        self.__player_id = player_id
        self.__char = char_value
        self.score = 0

    @property
    def player_id(self) -> int:
        return self.__player_id

    @player_id.setter
    def player_id(self, player_id):
        self.__player_id = player_id

    @property
    def char(self) -> Char:
        return self.__char

    def increment_score(self):
        self.score += 1

    @staticmethod
    def __validate_player_id(player_id) -> bool:
        if player_id < 1 or player_id > 2:
            raise InvalidPlayerIdException("Player ID must be between 1 and 2")
        return True

    @staticmethod
    def __validate_char_value(char_value) -> bool:
        if char_value not in [Char.x.value, Char.o]:
            raise InvalidCharacterIdException("Character must be X or O or empty")
        return True
