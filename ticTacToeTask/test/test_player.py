import unittest

from ticTacToeTask.char import Characters
from ticTacToeTask.player import Player


class MyPlayerTestCase(unittest.TestCase):
    def test_that_repetition_of_player_name_would_throw_error(self):
        player_one = Player("abimbola", Characters.X.value)
        with self.assertRaises(NameError):
            player_two = Player("abimbola", Characters.O.value)

    def test_that_two_players_can_exist(self):
        player_one_name = "abimbola"
        player_one_character = Characters.X.value
        player_one = Player(player_one_name, player_one_character)
        player_two_name = "femi"
        player_two_character = Characters.O.value
        self.assertTrue(player_one, player_one_character)
        self.assertTrue(player_two_name, player_two_character)


