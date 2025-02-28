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

    def make_move(self, cell_number: int):
        if self.__game_over == True:
            print("Game is over.")
            return True


    def print_board(self):
        for i in range(3):
            for j in range(2):
                print(self.__board[i][j], end=" | ")
            print()
            if i < 2:
                print("--+---+--")

        print()



