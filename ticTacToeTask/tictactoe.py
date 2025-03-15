class TicTacToe:

    def __init__(self, player_one, player_two):
        self.__board = [[" " for row in range(3)] for column in range(3)]
        self.__winner = None
        self.__game_over = False
        self.__players = [player_one, player_two]
        self.__current_player = player_one

    def get_winner(self):
        return self.__winner

    def get_players(self):
        return self.__players

    def get_board(self):
        return self.__board

    def get_current_player(self):
        return self.__current_player

    def print_board(self):
        for i in range(3):
            for j in range(2):
                print(self.__board[i][j], end=" | ")
            print(self.__board[i][2])
            if i < 2:
                print("--+---+--")
        print()

    def check_win(self, player):
        for row in self.__board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.__board[row][col] == player for row in range(3)):
                return True

        if (self.__board == player and self.__board[1][1] == player and self.__board[2][2] == player) or (
                self.__board[2] == player and self.__board[1][1] == player and self.__board[2] == player):
            return True

        return False

    def make_move(self, cell_number: int):
        while True:
            try:
                move = int(input("Enter your move (1-9): "))

                row = (move - 1) // 3
                col = (move - 1) % 3

                if 1 <= move <= 9 and self.__board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid move! Try again.")

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def play_tic_tac_toe(self):
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        for turn in range(9):
            print(f"Player {self.get_current_player}'s turn.")
            row, col = self.make_move()
            board[row][col] = current_player

            self.print_board()

            if self.check_win(self):
                print(f"Congratulations! Player {self.get_current_player} wins!")
                return

            current_player = 'O' if current_player == 'X' else 'X'

        print("It's a draw!")

    # def print_board(self):

    #     for i in range(3):
    #         for j in range(2):
    #             print(self.__board[i][j], end=" | ")
    #         print(self.__board[i][2])
    #         if i < 2:
    #             print("--+---+--")
    #     print()

    # if self.board.set_cell(row, col, self.current_symbol):
    #     winner = self.board.check_winner()
    #     if winner:
    #         self.board.print_board()
    #         print(f"Congratulations! The player with {self.current_symbol.value} wins!")
    #         return True
    #
    #     elif self.board.is_full():
    #         self.board.print_board()
    #         print('Its a draw')
    #         return True
    #     else:
    #         self.switch_player()
    #         return False
    # else:
    #     print("This cell is already occupied, choose another one.")
    #     return False
