from ticTacToe.char import Char
from ticTacToe.player import Player
from ticTacToe.board import Board
from ticTacToeTask.tictactoeexceptions import InvalidCharacterIdException


class TicTacToeApp:

    def __init__(self):
        self.player1 = Player(1, Char.char_x)
        self.player2 = Player(2, Char.char_o)
        self.game = Board(self.player1, self.player2)

    def play_game(self):
        while True:
            print(f"Player {self.game.currentPlayer().player_id}, enter your move")
            try:
                row = int(input("Row (0-2): "))
                col = int(input("Column (0-2): "))
                self.game.print_board()
                result = self.game.make_move(row, col)
                if result:
                    print(result)
                    break
            except InvalidCharacterIdException as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")

        print(self.game.get_scores())


if __name__ == "__main__":
    app = TicTacToeApp()
    app.play_game()
