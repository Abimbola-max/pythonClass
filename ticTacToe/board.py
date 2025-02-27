from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import FullCellsException, InvalidCharacterIdException


class Board:

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__board = [
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty],
                [Char.char_empty, Char.char_empty, Char.char_empty]
        ]
        self.__players = [player1, player2]
        self.__current_player = player1

    def currentPlayer(self):
        return self.__current_player

    def player(self):
        return self.__players

    def make_move(self, row, column):
        if row >= 0 and row < 3 and column >= 0 and column < 3 and self.__board[row][column] == Char.char_empty:
            self.__board[row][column] = self.__current_player.char
            self.print_board()
            if self.check_winner():
                return "Player " + self.__current_player.player_id + " won!"
            elif self.is_game_board_full():
                return "It is a tie!"
            else:
                self.switch_player()
        else:
            raise InvalidCharacterIdException("Don't waste my time!")

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

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.__board[i][j], end="")
                if j < 2:
                    print("|", end="")
            print()
            if i < 2:
                print("-+-+-")

        print()



