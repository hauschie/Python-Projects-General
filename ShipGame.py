# Author: Eric Hauschild
# Date: 3/2/2022
# Description: This program contains a class called ShipGame that allows two people to play the game Battleship. Each
#           player has their own 10x10 grid they place their ships on. On their turn, they can fire a torpedo at a
#           square on the enemy's grid. Player 'first' gets the first turn to fire a torpedo, after which players
#           alternate firing torpedos. A ship is sunk when all of its squares have been hit. When a player sinks their
#           opponent's final ship, they win.

class ShipGame:
    """
    The ShipGame class should have these methods:
    - an init method that has no parameters and sets all data members to their initial values
    - place_ship takes as arguments: the player (either 'first' or 'second'), the length of the ship, the coordinates of
     the square it will occupy that is closest to A1, and the ship's orientation - either 'R' if its squares occupy the
     same row, or 'C' if its squares occupy the same column (there are a couple of examples below). If a ship would not
     fit entirely on that player's grid, or if it would overlap any previously placed ships on that player's grid, or if
      the length of the ship is less than 2, the ship should not be added and the method should return False. Otherwise,
       the ship should be added and the method should return True. You may assume that all calls to place_ship() are
       made before any other methods are called (besides the init method, of course). You should not enforce turn order
       during the placement phase.
    - get_current_state returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
    - fire_torpedo takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates of
    the target square, e.g. 'B7'. If it's not that player's turn, or if the game has already been won, it should just
    return False. Otherwise, it should record the move, update whose turn it is, update the current state (if this turn
    sank the opponent's final ship), and return True. If that player has fired on that square before, that's not illegal
     - it just wastes a turn. You can assume place_ship will not be called after firing of the torpedos has started.
    - get_num_ships_remaining takes as an argument either "first" or "second" and returns how many ships the specified
    player has left.

    References: Coordinates class
    """
    def __init__(self):
        """
        Has no parameters and sets all data members (turn number, and player 1 and 2 variables) to their initial values.
        """
        self._turn_num = 'first'
        self._player_1 = Coordinates()
        self._player_2 = Coordinates()

    def get_player_1_coord(self):
        """Returns player 1 ship coordinates"""
        return self._player_1.get_dict_of_ship_coord()

    def get_player_2_coord(self):
        """Returns player 1 ship coordinates"""
        return self._player_2.get_dict_of_ship_coord()

    def place_ship(self, player, len_of_ship, coord_close_to_a1, ship_orient):
        """
        takes as arguments: the player (either 'first' or 'second'), the length of the ship, the coordinates of the
        square it will occupy that is closest to A1, and the ship's orientation - either 'R' if its squares occupy the
        same row, or 'C' if its squares occupy the same column (there are a couple of examples below). If a ship would
        not fit entirely on that player's grid, or if it would overlap any previously placed ships on that player's
        grid, or if the length of the ship is less than 2, the ship should not be added and the method should return
        False. Otherwise, the ship should be added and the method should return True. You may assume that all calls to
        place_ship() are made before any other methods are called (besides the init method, of course). You should not
        enforce turn order during the placement phase.
        """
        ship_coord_to_be_validated = {coord_close_to_a1: 'not hit'}
        coord_to_add = coord_close_to_a1
        len_of_ship -= 1
        if player == 'first':
            player_dictionary = self._player_1.get_dict_of_ship_coord()
        elif player == 'second':
            player_dictionary = self._player_1.get_dict_of_ship_coord()
        else:
            player_dictionary = False

        if len_of_ship < 2:     # too small of a ship
            return False

        if ship_orient == 'R':      # horizontal ship
            while len_of_ship != 0:
                len_of_ship -= 1
                if len(coord_to_add) == 2:
                    if int(coord_to_add[-1]) + 1 == 10:     # far right side
                        coord_num_to_add = coord_to_add[:-1] + '1' + '0'
                        # checking if coordinates are the same as existing ship
                        for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                            for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                                if key_2 == coord_num_to_add:
                                    return False
                        ship_coord_to_be_validated[coord_num_to_add] = 'not hit'
                    else:   # normal case
                        coord_num_to_add = coord_to_add[:-1] + str(int(coord_to_add[-1]) + 1)
                        coord_to_add = coord_num_to_add
                        # checking if coordinates are the same as existing ship
                        for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                            for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                                if key_2 == coord_num_to_add:
                                    return False
                        ship_coord_to_be_validated[coord_num_to_add] = 'not hit'
                else:
                    return False   # off the board
        if ship_orient == 'C':      # vertical ship
            coord_letter_to_add = coord_to_add[0]
            while len_of_ship != 0:
                len_of_ship -= 1
                coord_letter_to_add = self.next_letter(coord_letter_to_add)
                if coord_letter_to_add is False:    # if ship doesn't fit on board
                    return False
                coord_to_add = coord_letter_to_add + coord_close_to_a1[1:]
                # checking if coordinates are the same as existing ship
                for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                    for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                        if key_2 == coord_to_add:
                            return False
                ship_coord_to_be_validated[coord_to_add] = 'not hit'
        if player == 'first':
            self._player_1.store_ships(ship_coord_to_be_validated)
            return True
        if player == 'second':
            self._player_2.store_ships(ship_coord_to_be_validated)
            return True

    def next_letter(self, letter):
        """
        Takes in a letter and returns the next letter in the coordinate system if it is valid/before K
        """
        alphabet = 'ABCDEFGHIJ'
        for char in alphabet:
            if letter == char:
                return alphabet[alphabet.index(letter) + 1]
        return False

    def get_current_state(self):
        """
        returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
        """
        if self.get_num_ships_remaining('first') == 0 and self.get_num_ships_remaining('second') > 0:
            return 'SECOND_WON'
        elif self.get_num_ships_remaining('second') == 0 and self.get_num_ships_remaining('first') > 0:
            return 'FIRST_WON'
        else:
            return 'UNFINISHED'     # if neither player has won yet

    def fire_torpedo(self, player_firing_torpedo, coord_target_square):
        """
        takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates of the target
        square, e.g. 'B7'. If it's not that player's turn, or if the game has already been won, it should just return
        False. Otherwise, it should record the move, update whose turn it is, update the current state (if this turn
        sank the opponent's final ship), and return True. If that player has fired on that square before, that's not
        illegal - it just wastes a turn. You can assume place_ship will not be called after firing of the torpedos has
        started.
        """
        if self._turn_num == player_firing_torpedo:
            pass

        if self.get_current_state() != 'UNFINISHED':    # if the game is over
            return False

        if player_firing_torpedo == 'first':
            player_dictionary = self._player_2.get_dict_of_ship_coord()
            for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                    if key_2 == coord_target_square:
                        player_dictionary[key_1][key_2] = 'hit'     # records which part of ship was hit

        if player_firing_torpedo == 'second':
            player_dictionary = self._player_1.get_dict_of_ship_coord()
            for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                    if key_2 == coord_target_square:
                        player_dictionary[key_1][key_2] = 'hit'     # records which part of ship was hit

        # updating what player's turn it is
        if self._turn_num == 'first':
            self._turn_num = 'second'

        if self._turn_num == 'second':
            self._turn_num = 'first'

        return True


    def get_num_ships_remaining(self, player):
        """
        takes as an argument either "first" or "second" and returns how many ships the specified player has left.
        """
        total_parts_of_ship = 0
        parts_of_ship_hit = 0
        num_of_ships_left = 0
        if player == 'first':
            player_dictionary = self._player_1.get_dict_of_ship_coord()
            for key_1, value_1 in player_dictionary.items():  # looks at individual ship
                for key_2, value_2 in value_1.items():  # looks at individual coordinates within ship
                    total_parts_of_ship += 1
                    if value_2 == 'hit':
                        parts_of_ship_hit += 1
                if total_parts_of_ship != parts_of_ship_hit:
                    num_of_ships_left += 1
        if player == 'second':
            player_dictionary = self._player_2.get_dict_of_ship_coord()
            for key_1, value_1 in player_dictionary.items():
                for key_2, value_2 in value_1.items():
                    total_parts_of_ship += 1
                    if value_2 == 'hit':
                        parts_of_ship_hit += 1
                if total_parts_of_ship != parts_of_ship_hit:
                    num_of_ships_left += 1
        return num_of_ships_left


class Coordinates:
    """
    This class contains data on the ships hit and the locations of ships placed by a given player. It has a list that
    contains the data for the outline of the board, a dictionary of coordinates of ships, and a dictionary of the
    coordinates of the ships that were hit.

    Referenced by: ShipGame class
    """
    def __init__(self):
        self._list_creating_board = []
        self._dict_of_ship_coord = {}
        self._dict_of_ships_hit = {}
        self._ship_number = 1

    def get_dict_of_ship_coord(self):
        """Returns the dictionary of ship coordinates"""
        return self._dict_of_ship_coord

    def store_ships(self, dict_of_newly_validated_ship_coord):
        """
        Stores ships for a specific player when place_ship method is used in ShipGame.
        """
        self._dict_of_ship_coord[self._ship_number] = dict_of_newly_validated_ship_coord
        self._ship_number += 1


#   DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
#
#   1) Determining how to store the boards
#       Boards will be stored as a list in Coordinates class:
#       list's first value set as blank
#       list's next 10 values are stored as 1, 2, 3, 4, 5, 6. 7, 8, 9, 10
#       same for A-J but offset since they're columns
#       the place in the list that has the intersection of 1 and A will be [A, 1]
#       same process for other coordinates
#   2) Initializing the boards
#       a variable for player 1 and player two are each initialized as Coordinates classes,
#           which also will create the board.
#       As mentioned before in board storage, this will all be set up as a list in the Coordinates class
#   3) Determining how to track which player's turn it is to play right now
#       each time fire torpedo method is used, the variable turn_num is incremented
#       if turn number is odd: "player 2's turn"
#       else: "player 1's turn"
#   4) Determining how to validate piece placement
#       creates a  list of where the ship is, starts by inserting first coordinate
#       if orientation is R
#           for the length of the length of the ship:
#               add 1 to the first coordinate number
#               add this coordinate to the list
#       else:
#           for the length of the length of the ship:
#               add a letter to the first coordinate letter
#               add this coordinate to the list
#       for loop across the list of coordinates that was created
#           if the coordinates do not equal a coordinate in a list of valid coordinates
#               return False
#       for the length of the list
#           for a coordinate in the list:
#               for another coordinate in the list
#                   if both coordinates are equal, False is returned
#       otherwise validated, and entered into the player's variable using the Coordinates class
#   5) Determining when ships have been sunk
#       (dictionary in the Coordinates class in the player's variable contains list of ships hit)
#       if coordinate of torpedo is equal to a coordinate number in the list of ships
#       that coordinate is removed from the list of ships
#       that coordinate is added to the list of ships hit
#       if list of ships hit is equal to the length of a ship, ship has been sunk
#   6) Determining when the game has ended
#       if in the Coordinate class in the player variable the list of ships is empty
#       game has ended
#       current_state becomes 'FIRST_WON' or 'SECOND_WON'
#       if list of ships of player 1 is empty:
#           'SECOND_WON'
#       if list of ships of player 2 is empty:
#           'FIRST_WON'

#test
#game = ShipGame()
#game.place_ship('first', 5, 'B2', 'C')
#game.place_ship('first', 2, 'I8', 'R')
#game.place_ship('second', 3, 'H2', 'C')
#game.place_ship('second', 2, 'A1', 'C')
#game.place_ship('first', 8, 'H2', 'R')
#game.fire_torpedo('first', 'H3')
#game.fire_torpedo('second', 'A1')
#game.fire_torpedo('first', 'H2')
#game.fire_torpedo('second', 'B1')
#print(game.get_current_state())

#test = ShipGame()
#test.place_ship('first', 3, 'B1', 'C')
#print(test.place_ship('first', 4, 'B1', 'C'))
#print(test.get_player_1_coord())
#test.fire_torpedo('second', 'B1')
#test.fire_torpedo('second', 'C1')
#print(test.get_player_1_coord())
#print(test.get_num_ships_remaining('first'))
#print(test.get_current_state())


