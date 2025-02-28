from ticTacToeTasks.charvalue import Char


class Board:

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__board = [[" " for row in range(3)] for column in range(3)]
        # self.__board = [
        #         [Char.empty, Char.empty, Char.empty],
        #         [Char.empty, Char.empty, Char.empty],
        #         [Char.empty, Char.empty, Char.empty],
        # ]
        self.__players = [player1, player2]
        self.__current_player = player1
        self.__winner = None
        self.__game_over = False

    @property
    def get_winner(self):
        return self.__winner

    @property
    def current_player(self):
        return self.__current_player

    def players(self):
        return self.__players

    def make_move(self, row, column) -> bool:
        if self.__game_over == True:
            print("Game is over.")
            return True

        if not row >= 0 and row < 3 and column >= 0 and column < 3 and self.__board[row][column] == Char.empty:
            print("Invalid row or column.")
            return False

        self.__board[row][column] = self.__current_player.char.value
        self.print_board()

        if self.check_winner():
            print(f"Player {self.__current_player.player_id} wins!")
            self.__current_player.increment_score()
            self.__game_over = True
            return True

        self.switch_player()

        return True


    def switch_player(self):
        if self.__current_player == self.__players[0]:
            self.__current_player = self.__players[1]
        else:
            self.__current_player = self.__players[1]

    def check_winner(self) -> bool:

        check = self.__current_player.char

        for i in range(3):
            if self.__board[i][0] == check and self.__board[i][1] == check and self.__board[i][2] == check:
                self.__winner = self.__current_player
                return True
            if self.__board[0][i] == check and self.__board[1][i] == check and self.__board[2][i] == check:
                self.__winner = self.__current_player
                return True

        if self.__board[0][0] == check and self.__board[1][1] == check and self.__board[2][2] == check:
            self.__winner = self.__current_player
            return True
        if self.__board[0][2] == check and self.__board[1][1] == check and self.__board[2][0] == check:
            self.__winner = self.__current_player
            return True

        return False

    def is_game_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == Char.empty.value:
                    return True

    def reset_board(self):
        self.__board = [[Char.empty.value, Char.empty.value, Char.empty.value],
                        [Char.empty.value, Char.empty.value, Char.empty.value],
                        [Char.empty.value, Char.empty.value, Char.empty.value]
                        ]
        self.__winner = None
        self.__game_over = False
        self.__current_player = self.players

    def is_game_over(self):
        if self.check_winner(): return True
        if self.is_game_board_full(): return True

    def print_board(self):
        for i in range(3):
            for j in range(2):
                print(self.__board[i][j], end=" | ")
            print()
            if i < 2:
                print("--+---+--")

        print()

    def get_scores(self):
        return f"Player 1: {self.__players[0].score}, Player 2: {self.__players[1].score}"

    # def is_full(self, row: int, column: int) -> bool:
    #     for i in range(3):
    #         if self.__board[row][column] != Char.empty: return False
    #     return True





