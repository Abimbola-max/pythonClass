import unittest

from ticTacToe.char import Char
from ticTacToe.exceptions.tictactoeexceptions import InvalidPlayerIdException
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

    def test_that_tictactoe_game_is_created_and_players_more_than_two_throws_exceptions(self):
        first_player = Player(1, Char.char_x.value)
        self.assertEqual(1, first_player.player_id)
        second_player = Player(2, Char.char_o.value)
        self.assertEqual(2, second_player.player_id)

        with self.assertRaises(InvalidPlayerIdException):
            third_player = Player(3, Char.char_o.value)


    def test_that_a_player_wins_the_game(self):
        first_player = Player(1, Char.char_x.value)
        second_player = Player(2, Char.char_o.value)
        game = TicTacToe(first_player, second_player)

        game.make_move(0, 0)
        game.make_move(1, 0)
        game.make_move(0, 1)
        game.make_move(1, 1)
        game.make_move(0, 2)

        winner = game.check_winner()
        self.assertTrue(first_player, winner)

    def test_that_there_is_draw_no_winner_or_loser(self):
        first_player = Player(1, Char.char_x.value)
        second_player = Player(2, Char.char_o.value)

        game = TicTacToe(first_player, second_player)

        game.make_move(0, 0)
        game.make_move(0, 1)
        game.make_move(0, 2)
        game.make_move(1, 0)
        game.make_move(1, 1)
        game.make_move(1, 2)
        game.make_move(2, 0)
        game.make_move(2, 1)
        game.make_move(2, 2)
        self.assertTrue(game.is_game_board_full())

    def test_that_there_is_draw_no_winner_or_loser_double_check(self):
        first_player = Player(1, Char.char_x.value)
        second_player = Player(2, Char.char_o.value)

        game = TicTacToe(first_player, second_player)

        game.make_move(0, 0)
        game.make_move(0, 1)
        game.make_move(0, 2)
        game.make_move(1, 0)
        game.make_move(1, 2)
        game.make_move(2, 0)
        game.make_move(2, 1)
        game.make_move(2, 2)
        self.assertFalse(game.is_game_board_full())
        game.make_move(1, 1)
        self.assertTrue(game.is_game_board_full())








