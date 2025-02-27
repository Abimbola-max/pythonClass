from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import InvalidRowOrColumnException, InvalidCharacterIdException
from ticTacToe.player import Player
from ticTacToe.board import Board


class TicTacToeApp:
    if __name__ == "__main__":
        player1 = Player(1, Char.char_x)
        player2 = Player(2, Char.char_o)

        game = Board(player1, player2)
        game.print_board()

        while not game.check_winner() and not game.is_game_board_full():
            try:
                print(f"Player {game.currentPlayer().player_id}, enter your move")
                row = int(input("Row (0-2): "))
                column = int(input("Column (0-2): "))

                game.make_move(row, column)

                if game.check_winner() or game.is_game_board_full():
                    break
            except InvalidRowOrColumnException:
                print("Invalid input. Please enter integers for row and column.")
            except InvalidCharacterIdException as e:
                print(f"Error {e}")
        if game.check_winner():
            print(f"Player {game.currentPlayer().player_id} wins!")
        else:
            print("It's a draw!")
