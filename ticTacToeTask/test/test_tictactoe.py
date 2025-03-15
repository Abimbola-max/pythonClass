import unittest

from ticTacToeTask.char import Characters
from ticTacToeTask.player import Player
from ticTacToeTask.tictactoe import TicTacToe
from ticTacToeTask.tictactoeexceptions import FullCellsException


class MyTestCase(unittest.TestCase):

    def test_that_creation_of_tic_tac_toe_game_with_2_player_is_valid(self):
        self.player1 = Player("abimbola", Characters.X.value)
        self.player2 = Player("Femi", Characters.O.value)
        self.my_game = TicTacToe(self.player1, self.player2)
        self.assertListEqual([self.player1, self.player2], self.my_game.get_players())

    def test_to_ensure_that_the_game_has_a_score_board_that_is_initialized_correctly_with_an_empty_string(self):
        self.player1 = Player("abimbola", Characters.X.value)
        self.player2 = Player("Femi", Characters.O.value)
        my_game = TicTacToe(self.player1, self.player2)
        self.assertListEqual([[' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' ']
                                    ], my_game.get_board())

    def test_that_i_can_get_current_player(self):
        self.player1 = Player("abimbola", Characters.X.value)
        self.player2 = Player("Femi", Characters.O.value)
        self.my_game = TicTacToe(self.player1, self.player2)

        self.assertListEqual([self.player1, self.player2], self.my_game.get_players())
        self.assertListEqual([[' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' ']
                                    ], self.my_game.get_board())

        self.my_game.make_move(1)
        self.assertEqual(self.player1, self.my_game.get_current_player())

    def test_that_a_player_cannot_play_in_a_cell_that_is_already_occupied(self):
        self.player1 = Player("Abimbola", Characters.X.value)
        self.player2 = Player("Femi", Characters.O.value)
        self.my_game = TicTacToe(self.player1, self.player2)

        self.assertListEqual([self.player1, self.player2], self.my_game.get_players())
        self.assertListEqual([[' ', ' ', ' '],
                              [' ', ' ', ' '],
                              [' ', ' ', ' ']], self.my_game.get_board())

        self.my_game.make_move(1)
        self.assertEqual(self.player1, self.my_game.get_current_player())
        self.my_game.make_move(2)
        self.assertEqual(self.player1, self.my_game.get_current_player())
        with self.assertRaises(FullCellsException):
            self.my_game.make_move(2)




