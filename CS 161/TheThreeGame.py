# Author: Eric Hauschild
# Date: 11/25/2021
# Description: This program Allows two players to play a game in which they
#     alternately choose numbers from 1-9. If at any point exactly three
#     of a player's numbers sum to exactly 15, then that player has won.
#     If all numbers from 1-9 are chosen, but neither player has won,
#     then the game ends in a draw.

class TheThreeGame:
    """Allows two players to play a game in which they
    alternately choose numbers from 1-9. This includes the data
    members for keeping track of which numbers have been chosen and
    by whom, the current state (either "FIRST_PLAYER_WON",
    "SECOND_PLAYER_WON", "IT_IS_A_DRAW", or "GAME_UNFINISHED,
    and which player's turn it is. If at any point exactly three
    of a player's numbers sum to exactly 15, then that player has won.
    If all numbers from 1-9 are chosen, but neither player has won,
    then the game ends in a draw."""

    def __init__(self, player_1_list, player_2_list, current_state, player_turn):
        """Initiates the variables for lists of numbers chosen by player 1 and player 2,
        along with a variable in which to record the current state (either "FIRST_PLAYER_WON",
        "SECOND_PLAYER_WON", "IT_IS_A_DRAW", or "GAME_UNFINISHED) and which player's turn it is"""
        self._player_1_list = list
        self._player_2_list = list
        self._current_state = str
        self._player_turn = 1

    def get_player_1_list(self):
        """Returns the list of player 1's numbers."""
        return self._player_1_list

    def get_player_2_list(self):
        """Returns the list of player 2's numbers."""
        return self._player_2_list

    def get_current_state(self):
        """Returns the current state (either "FIRST_PLAYER_WON",
        "SECOND_PLAYER_WON", "IT_IS_A_DRAW", or "GAME_UNFINISHED)."""
        return self._current_state

    def get_player_turn(self):
        """Returns the even or odd number designating which
        player's turn it is."""
        return self._player_turn

    def get_winner(self):
        """Returns "FIRST_PLAYER_WON" if first player has won (total numbers
        equal 15), "SECOND_PLAYER_WON" if second player has won (total numbers
        equal 15) and None if no player has won."""
        pass
        return current_state

    def is_it_a_draw(self):
        """Returns "IT_IS_A_DRAW" if it's a draw (all numbers 1-9 are chosen),
        else returns "GAME_UNFINISHED". If a player has won and is_it_a_draw
        is called, then it should return "FIRST_PLAYER_WON" or "SECOND_PLAYER_WON",
        depending which applies."""
        pass
        return current_state

    def make_move(self, player_string, integer_1):
        """Two parameters are input. There is a string instructing which the player
        should make the move and a place to enter in an integer between 1 and 9 that
        hasn't yet been chosen. If the integer is not between 1 and 9 or has already
        been chosen, the program returns with False. Otherwise, it records the move
        in one of two lists of player numbers, updates which player's turn it is, and return True."""
        pass