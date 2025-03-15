from ticTacToeTask.tictactoe import TicTacToe
from ticTacToeTask.tictactoeexceptions import InvalidCharacterIdException


class Main:

    player1 = input("Player One Please Enter your name: ")
    player2 = input("Player Two Please Enter your name: ")
    game = TicTacToe(player1, player2)


def play_game(self):
    while True:
        print(f"Player {self.game.currentPlayer().player_id}, enter your move")
        try:
            move = int(input("Enter move (1-9): "))
            self.game.print_board()
            result = self.game.make_move(move)
            if result:
                print(result)
                break
        except InvalidCharacterIdException as e:
            print(e)
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

    print(self.game.get_scores())


