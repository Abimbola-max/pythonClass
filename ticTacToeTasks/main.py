from typing import Tuple

from ticTacToeTasks.board import Board
from ticTacToeTasks.charvalue import Char
from ticTacToeTasks.player import Player
from ticTacToeTasks.tictactoeexceptions import InvalidCharacterIdException


class Main:

    def __init__(self):
        self.player1 = Player(1, Char.x)
        self.player2 = Player(2, Char.o)

    def play_tic_tac_toe(self):
        while True:
            game = Board(self.player1, self.player2)
            game.print_board()

            while not game.is_game_board_full():
                row, col = self.get_player_move(game.current_player)
                if game.make_move(row, col):
                    game.print_board()

                    if game.is_game_board_full():
                        break
                game.switch_player()

            if game.get_winner:
                print(f"Player {game.current_player.player_id} wins!")
                game.current_player.increment_score()
            elif game.is_game_board_full():
                print("It's a draw!")

            if not self.play_again():
                break

            game.reset_board()

        self.print_final_scores()

    def get_player_move(self, player) -> Tuple[int, int]:
        while True:
            try:
                row = int(input(f"Player {player.player_id}, enter the row (0-2): "))
                col = int(input(f"Player {player.player_id}, enter the column (0-2): "))
                return row, col
            except InvalidCharacterIdException:
                print("Invalid input. Please enter a number between 0 and 2.")

    def play_again(self) -> bool:
        while True:
            response = input("Do you want to play again? (yes/no): ").casefold()
            if response.lower() == "yes":
                return True
            elif response.lower() == "no":
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    def print_final_scores(self):
        print("\nFinal Scores:")
        print(f"Player 1: {self.player1.score}")
        print(f"Player 2: {self.player2.score}")


if __name__ == "__main__":
    main = Main()
    main.play_tic_tac_toe()
