from ticTacToe import char
from ticTacToe.exceptions.tictactoeexceptions import InvalidRowOrColumnException
from ticTacToe.player import Player
from ticTacToe.tictactoe import TicTacToe


class TicTacToeApp:
    if __name__ == "__main__":
        """Main section to run the Tic Tac Toe game."""
        player1 = Player(1, char.char_x)
        player2 = Player(2, char.char_o)

        game = TicTacToe(player1, player2)
        game.print_board()

        while not game.check_winner() and not game.is_game_board_full():
            try:
                print(f"Player {game.__current_player.player_id}, enter your move")
                row = int(input("Row (0-2): "))
                column = int(input("Column (0-2): "))

                game.make_move(row, column)

                if game.check_winner() or game.is_game_board_full():
                    break
            except InvalidRowOrColumnException:
                print("Invalid input. Please enter integers for row and column.")
            except InvalidRowOrColumnException as e:
                print(e)

        if game.check_winner():
            print(f"Player {game.__current_player.player_id} wins!")
        else:
            print("It's a draw!")
