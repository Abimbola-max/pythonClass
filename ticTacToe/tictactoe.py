from ticTacToe import char
from ticTacToe.char import Char


class TicTacToe:

    def __init__(self, player1, player2):
        self.__board = [
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty]
        ]