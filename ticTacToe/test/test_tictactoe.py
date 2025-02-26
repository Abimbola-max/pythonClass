import unittest

from ticTacToe.char import Char
from ticTacToe.player import Player
from ticTacToe.tictactoe import TicTacToe


class MyTicTacToeTestCase(unittest.TestCase):
    def test_that_first_player_is_player_one_and_plays_x(self):
        first_player = Player(1, Char.char_x.value)
        self.assertEqual(1, first_player.player_id)

    def test_that_second_player_is_player_two_and_plays_o(self):
        first_player = Player(1, Char.char_x.value)
        self.assertEqual(1, first_player.player_id)
        second_player = Player(2, Char.char_o.value)
        self.assertEqual(2, second_player.player_id)

    def test_that_my_board_is_empty_at_the_creation_of_my_game(self):
        first_player = Player(1, Char.char_x.value)
        second_player = Player(2, Char.char_o.value)
        game = TicTacToe(first_player, second_player)




