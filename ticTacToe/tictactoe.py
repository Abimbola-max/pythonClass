from ticTacToe import char
from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import FullCellsException


class TicTacToe:

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__board = [
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty]
        ]
        self.players = [player1, player2]
        self.__current_player = player1

    def make_move(self, row, column):
        if self.__board[row][column] == Char.char_empty:
            self.__board[row][column] = self.__current_player.char
            self.switch_player()
        else:
            raise FullCellsException("Cell is already occupied")

    def switch_player(self):
        if self.__current_player == self.__player1:
            self.__current_player = self.__player2
        else:
            self.__current_player = self.__player1

    def check_winner(self) -> bool:

        check = self.__current_player.char
        for i in range(3):
            if self.__board[i][0] == check and self.__board[i][1] == check and self.__board[i][2] == check: return True
            if self.__board[0][i] == check and self.__board[1][i] == check and self.__board[2][i] == check: return True

        if self.__board[0][0] == check and self.__board[1][1] == check and self.__board[2][2] == check: return True
        if self.__board[0][2] == check and self.__board[1][1] == check and self.__board[2][0] == check: return True

        return False

    def is_game_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == Char.char_empty: return False
        return True



