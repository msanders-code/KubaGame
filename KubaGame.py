# Author: Matt Sanders
# Date: 6/13/2021
# Description: This program defines methods for playing a game called 'Kuba'. There is
#              a method that defines the game board, the players, the game itself.

class Board:
    """
    Defines the game board, sets up the initialization, methods to update it when a player moves and it keeps
    track of the number of each color marble currently on the board. It takes no parameters. The KubaGame class
    is the only class that it communicates with in order to update it's state and track the marbles that are still
    in play.
    """

    def __init__(self):
        """
        Initializes the game board at set up and the total of each color marble on the board. returns nothing and
        takes no parameters.
        """

        # initializes the game board positions
        self._grid = [["W", "W", "X", "X", "X", "B", "B"], ["W", "W", "X", "R", "X", "B", "B"],
                      ["X", "X", "R", "R", "R", "X", "X"], ["X", "R", "R", "R", "R", "R", "X"],
                      ["X", "X", "R", "R", "R", "X", "X"], ["B", "B", "X", "R", "X", "W", "W"],
                      ["B", "B", "X", "X", "X", "W", "W"]]
        self._state_of_board = [8, 8, 13]  # Initializes the count of marbles of each color on the board (W, B, R)

    def get_grid(self):
        """
        Returns the game board as a list. Takes no parameters.
        """

        return self._grid

    def set_grid(self, new_grid):
        """
         Updates the game board positions after any change to the marbles on the board. It
         takes a new list as a parameter and returns nothing.
        """

        self._grid = new_grid

    def get_state_of_board(self):
        """
        Returns a tuple of the count of each color marble currently on the board, ('W', 'B', 'R'); in that order.
        It takes no parameters.
        """

        return tuple(self._state_of_board)

    def set_state_of_board(self, color_knocked_off):
        """
        Updates the count of each color on the board. It takes a string for the color that was knocked off the
        end of the board as a parameter and returns nothing.
        """

        if color_knocked_off == "W":        # Check of a white marble is knocked off
            self._state_of_board[0] -= 1
        elif color_knocked_off == "B":      # Check if a black marble is knocked off
            self._state_of_board[1] -= 1
        elif color_knocked_off == "R":      # Check if a red marble is knocked off
            self._state_of_board[2] -= 1


class Player:
    """
    Defines each game player based on their name and color of marble. It holds methods to initialize the name,
    marble color, count of captured red marbles, current count of player's marbles, and the most recent move
    made by that player. It takes player name and marble color as parameters. It only needs to communicate with
    the KubaGame class in order to update information concerning the player.
    """

    def __init__(self, players_name, marble_color):
        """
        Initializes the player's name, marble color, number of red marbles, number of their marbles,
        and the coordinates of their most recent move. It takes strings of players' name and their
        marble color ('W' or 'B') and returns nothing.
        """

        self._players_name = players_name
        self._marble_color = marble_color
        self._red_marbles = 0               # Initializes the number of captured red marbles
        self._marbles = 8                   # Initializes the number of marbles they have on the board
        self._last_move = None              # Initializes the last move made

    def get_players_name(self):
        """
        Returns the player's name as a string. Takes no parameters.
        """

        return self._players_name

    def get_marble_color(self):
        """
        Returns the color of the player's marbles as a string. Takes no parameters.
        """

        return self._marble_color

    def get_red_marbles(self):
        """
        Returns the number of the red marbles the player has captured as an integer.
        Takes no parameters.
        """

        return self._red_marbles

    def set_red_marbles(self):
        """
        Updates the number of captured red marbles. Takes no parameters and returns nothing.
        """

        self._red_marbles += 1

    def get_marbles(self):
        """
        Returns the number of player's stones on the board as an integer. Takes no parameters.
        """

        return self._marbles

    def set_marbles(self):
        """
        Updates the number of player's stones left on the board. Takes no parameters and returns nothing.
        """

        self._marbles -= 1

    def get_last_move(self):
        """
        Returns the coordinates of the last move made by the player as a tuple of integers.
        Takes no parameters.
        """

        return self._last_move

    def set_last_move(self, coordinates, direction_moved):
        """
         Updates the _last_move with the coordinates and direction of the last move made by the player as a tuple. Takes
         a tuple of integers, (row, column), as coordinates and a direction as a string. It returns nothing.
        """

        self._last_move = (coordinates, direction_moved)


class KubaGame:
    """
    The main class for the game to run. It holds methods for updating the board information, the players information
    and in order to execute a move in any of the four directions (right, left, forward and backward). It keeps track
    of which players' turn it is and if a winner has been declared. It updates how many red marbles have been captured
    by each player and how many marbles are left on the board. It can also provide information about the board and
    about each player. It takes two parameter: player_one and player_two as tuples of players' name and their marble
    color (white or black). It communicates with the Board class in order to initialize the board, update the board
    after a move has been executed, judge if a valid move can be executed and access the count of each color of marble
    currently on the board. It communicates with the Player class in order to initialize each player in the game,
    access the number of red marbles that have been captured by a player, and allow each player to try and execute
    a new move. It communicates with the exception class to handle a player name entered into the make_move and
    get_captured methods who is not actually playing the game.
    """

    def __init__(self, player_one, player_two):
        """
        Initializes the players, the game board, the current player who turn it is and who has one the game.
        It takes two tuples, (player name, marble color) in that order of the players playing the game. and
        returns nothing.
        """

        self._player1 = Player(player_one[0], player_one[1].upper())    # Initializes the first player
        self._player2 = Player(player_two[0], player_two[1].upper())    # Initializes the second player

        # player dictionary
        self._players = {player_one[0]: self._player1, player_two[0]: self._player2}
        self._game_board = Board()                                      # Initializes the game board
        self._current_turn = None                                       # Any player can start the game
        self._winner = None                                             # Nobody has one yet

    def get_current_turn(self):
        """
        Returns which players' turn it is as a string. Takes no parameters.
        """

        return self._current_turn

    def get_winner(self):
        """
        Returns the players' name who has won the game as a string. Takes no parameters.
        """

        return self._winner

    def get_captured(self, players_name):
        """
        Returns the number of red marbles a specified player has captured as an integer. Takes the
        player's name as a string for a parameter. Returns nothing or returns a message saying that
        the entered name does not match a player in the current game.
        """

        # Handles exception for an entered name that is not a player in the game
        try:
            return self._players[players_name].get_red_marbles()
        except IndexError:
            return "That player is not part of this game."

    def get_marble_count(self):
        """
        Returns a tuple of the number of white, black and red marbles still on the board; in that order.
        Takes no parameters.
        """

        return self._game_board.get_state_of_board()

    def get_marble(self, coordinates):
        """
        Checks the board for the color of marble at the specified coordinate value. Coordinates
        are input as a tuple of integers, (row, column); in that order as a parameter.
        The function returns 'W', 'B', 'R', or 'X'; white, black, red, or empty space respectively as a string.
        """

        return self._game_board.get_grid()[coordinates[0]][coordinates[1]]

    def move_right(self, starting_coordinate):
        """
        Executes a move to the right and updates the game board. It takes the coordinates
        of the marble being moved as a tuple of integers, (row, column), as a parameter. It returns the
        value removed to shift the values within the row as a string and the updated board
        as a list.
        """

        current_board = self._game_board.get_grid()                 # Saves the current board to a variable
        start_pos = starting_coordinate[1]                          # Sets the loop starting position

        while start_pos <= (len(current_board[starting_coordinate[0]]) - 1):
            # Sets the character that is removed from the board
            end_char = current_board[starting_coordinate[0]][start_pos]

            # Checks for an empty square or the end of the row
            if end_char == 'X' or start_pos == (len(current_board[starting_coordinate[0]]) - 1):
                removed_value = current_board[starting_coordinate[0]].pop(start_pos)    # Removes the last value

                # Inserts a value before the moved marble
                current_board[starting_coordinate[0]].insert(starting_coordinate[1], "X")
                return removed_value, current_board     # Returns the removed value and the updated marble positions

            start_pos += 1

    def move_left(self, starting_coordinate):
        """
        Executes a move to the left and updates the game board. It takes the coordinates
        of the marble being moved as a tuple of integers, (row, column), as a parameter. It returns
        the value removed to shift the values within the row as a string and the updated
        board as a list.
        """

        current_board = self._game_board.get_grid()                 # Saves the current board to a variable
        start_pos = starting_coordinate[1]                          # Sets the loop starting position

        while start_pos >= 0:
            # Sets the character that is removed from the board
            end_char = current_board[starting_coordinate[0]][start_pos]

            if end_char == 'X' or start_pos == 0:           # Checks for an empty square or the beginning of the row
                removed_value = current_board[starting_coordinate[0]].pop(start_pos)        # Removes the last value

                # Inserts a value before the moved marble
                current_board[starting_coordinate[0]].insert(starting_coordinate[1], "X")
                return removed_value, current_board     # Returns the removed value and the updated marble positions

            start_pos -= 1

    def move_backward(self, starting_coordinate):
        """
        Executes a backward move on the board and updates the game board. It takes the
        coordinates of the marble being moved as a tuple of integers, (row, column), as a parameter.
        It returns the value removed to shift the values within the column as a string
        and the updated board as a list.
        """

        current_board = self._game_board.get_grid()                 # Saves the current board to a variable
        start_pos = starting_coordinate[0]                          # Sets the loop starting position
        column = []                                                 # Initializes a temporary list for column values

        while start_pos <= (len(current_board) - 1):
            end_char = current_board[start_pos][starting_coordinate[1]]  # Sets the current character on the board
            column.append(end_char)

            # Checks for an empty square or the end of the column
            if end_char == 'X' or start_pos == (len(current_board) - 1):
                removed_value = column.pop(-1)                # Removes the last value in the temp list
                column.insert(0, 'X')
                start_pos = starting_coordinate[0]            # Sets the reassignment starting position

                for value in column:
                    current_board[start_pos][starting_coordinate[1]] = value # Update positions on the saved board
                    start_pos += 1

                return removed_value, current_board     # Returns the value that was removed and the updated board

            start_pos += 1

    def move_forward(self, starting_coordinate):
        """
        Executes a forward move on the board and updates the game board. It takes the
        coordinates of the marble being moved as a tuple of integers, (row, column), as a parameter.
        It returns the value removed to shift the values in the column as a string and
        the updated board as a list.
        """

        current_board = self._game_board.get_grid()                 # Saves the current board to a variable
        start_pos = starting_coordinate[0]                          # Sets the loop starting position
        column = []                                                 # Initializes a temporary list for column values

        while start_pos >= 0:
            end_char = current_board[start_pos][starting_coordinate[1]]  # Sets the current character on the board
            column.append(end_char)

            if end_char == 'X' or start_pos == 0:   # Checks for an empty square or the beginning of the column
                removed_value = column.pop(-1)      # Removes the last value in the temp list
                column.insert(0, 'X')
                start_pos = starting_coordinate[0]  # Sets the reassignment starting position

                for value in column:
                    current_board[start_pos][starting_coordinate[1]] = value # Update positions on the saved board
                    start_pos -= 1

                return removed_value, current_board     # Returns the removed value and the updated board

            start_pos -= 1

    def check_marble_access(self, coordinate_pair, move_direction):
        """
        Checks if there is an empty space on the side of the marble one space
        in the direction opposite the given movement direction based on the
        coordinates of the marble that is being moved. If there is not an empty
        space, it returns False, otherwise it returns True. It takes a coordinate
        pair as a tuple, (row, column), in order and a direction, 'R', 'L', 'B', 'F'.
        """

        board_position = self._game_board.get_grid()

        if move_direction == "R":

            if coordinate_pair[1] == 0:     # Checks for the left edge of the board
                return True
            elif board_position[coordinate_pair[0]][coordinate_pair[1] - 1] == "X": # Checks position to left of marble
                return True

            return False

        elif move_direction == "L":

            if coordinate_pair[1] == 6:     # Checks for the right edge of the board
                return True
            elif board_position[coordinate_pair[0]][coordinate_pair[1] + 1] == "X": # Checks position to right of marble
                return True

            return False

        elif move_direction == "B":

            if coordinate_pair[0] == 0:     # Checks for the top edge of the board
                return True
            elif board_position[coordinate_pair[0] - 1][coordinate_pair[1]] == "X": # Checks position behind marble
                return True

            return False

        elif move_direction == "F":

            if coordinate_pair[0] == 6:     # Checks for the bottom edge of board
                return True
            elif board_position[coordinate_pair[0] + 1][coordinate_pair[1]] == "X": # Checks position behind marble
                return True

            return False

        return False  # Output if a valid direction is not used

    def reverse_opponents_move(self, move_coordinates, move_direction, opponent_move):
        """
        Checks if the proposed move will result in undoing the opponents previous move.
        It takes the proposed coordinates, the direction, and opponents last move coordinates;
        returns True if the move will not undo the opponents and False if it will.
        """

        board = self._game_board.get_grid()

        if opponent_move is None:      # Checks if the opponent has not made a move yet
            return True

        if move_direction == "R" and opponent_move[1] == "L": # Checks if we're moving in the opposite direction
            if move_coordinates[0] == opponent_move[0][0]:  #Check if in the same row
                index = move_coordinates[1]

                while index <= 6:

                    # Checks for an empty space at the same point in the grid as the opponent just moved from
                    if board[move_coordinates[0]][index] == "X" and index != opponent_move[0][1]:
                        return True
                    elif index == opponent_move[0][1]: # checks for the same grid pt at the end of the row
                        return False

                    index += 1
                return True

        elif move_direction == "L" and opponent_move[1] == "R": # Checks if we're moving in the opposite direction

            if move_coordinates[0] == opponent_move[0][0]:  # Checks if we're in the same row
                index = move_coordinates[1]

                while index >= 0:

                    # Checks for an empty space at the same point in the grid as the opponent just moved from
                    if board[move_coordinates[0]][index] == "X" and index != opponent_move[0][1]:
                        return True
                    elif index == opponent_move[0][1]: # checks for the same grid pt at the beginning of the row
                        return False

                    index -= 1
                return True

        elif move_direction == "B" and opponent_move[1] == "F": # Checks if we're moving in the opposite direction
            if move_coordinates[1] == opponent_move[0][1]:  # Checks if we're in the same column
                index = move_coordinates[0]

                while index <= 6:

                    # Checks for an empty space at the same point in the grid as the opponent just moved from
                    if board[index][move_coordinates[1]] == "X" and index != opponent_move[0][0]:
                        return True
                    elif index == opponent_move[0][0]: # checks for the same grid pt at the end of the column
                        return False

                    index += 1
                return True

        elif move_direction == "F" and opponent_move[1] == "B": # Checks if we're moving in the opposite direction
            if move_coordinates[1] == opponent_move[0][1]:  # Checks if we're in the same column
                index = move_coordinates[0]

                while index >= 0:

                    # Checks for an empty space at the same point in the grid as the opponent just moved from
                    if board[index][move_coordinates[1]] == "X" and index != opponent_move[0][0]:
                        return True
                    elif index == opponent_move[0][0]: # Checks for the same grid pt at the beginning of the column
                        return False

                    index -= 1
                return True

        return True

    def update_current_turn(self, players_name):
        """
        Handles updating the current turn. Takes current player name as a string for a parameter and
        doesn't return anything.
        """

        if players_name == self._player1.get_players_name():
            return self._player2.get_players_name()

        return self._player1.get_players_name()

    def make_move(self, player_name, marble_coordinate, movement_direction):
        """
         Moves the marbles on the board is the specified direction. It also updates
         the board, checks for a winner, makes sure it is the specified player's turn,
         makes sure the player is not reversing the opponents last move or trying to
         make the same move, it makes sure the player is not trying to push their own
         marble off the board, updates the number of marbles left on the board
         after the move has been made and makes sure that the player is only going to
         move their own marble. It takes the players' name as string, the coordinate of
         the marble they want to move as a tuple of integers, (row, column), and the
         direction they want to move as a string for parameters. It returns False if
         the proposed move is not valid, True if the proposed move is valid, or a message
         if the player trying to make the move is not a valid player.
        """

        # Check for a winner of the game
        if self._winner is not None:
            return False

        # Check for the the players' turn or the start of the game
        if self._current_turn != player_name and self._current_turn is not None:
            return False

        # Checks if the coordinates are valid
        if marble_coordinate[0] < 0 or marble_coordinate[0] > 6:
            self._current_turn = self.update_current_turn(player_name)  # Updates the current turn to the next player
            return False
        elif marble_coordinate[1] < 0 or marble_coordinate[1] > 6:
            self._current_turn = self.update_current_turn(player_name)  # Updates the current turn to the next player
            return False

        # Check for access to the marble
        if not self.check_marble_access(marble_coordinate, movement_direction):
            self._current_turn = self.update_current_turn(player_name)  # Updates the current turn to the next player
            return False

        # Check for a player trying to move any mable but their own
        if self._players[player_name].get_marble_color() != self.get_marble(marble_coordinate):
            self._current_turn = self.update_current_turn(player_name)  # Updates the current turn to the next player
            return False

        # Check for reversing an opponents previous move
        if player_name == self._player1.get_players_name():

            if not self.reverse_opponents_move(marble_coordinate, movement_direction, self._player2.get_last_move()):
                self._current_turn = self.update_current_turn(player_name) # Updates the current turn to the next player
                return False

        elif player_name == self._player2.get_players_name():

            if not self.reverse_opponents_move(marble_coordinate, movement_direction, self._player1.get_last_move()):
                self._current_turn = self.update_current_turn(player_name) # Updates the current turn to the next player
                return False

        # Make the move
        if movement_direction == "R":
            made_move = self.move_right(marble_coordinate) # Return the value removed at the new board arrangement
        elif movement_direction == "L":
            made_move = self.move_left(marble_coordinate) # Return the value removed at the new board arrangement
        elif movement_direction == "B":
            made_move = self.move_backward(marble_coordinate) # Return the value removed at the new board arrangement
        elif movement_direction == "F":
            made_move = self.move_forward(marble_coordinate) # Return the value removed at the new board arrangement
        else:
            self._current_turn = self.update_current_turn(player_name) # Updates the current turn to the next player
            return False

        try:
            # Check removed value and update board and players' marble counts
            if made_move[0] == "R":
                self._players[player_name].set_red_marbles()   # Adds one to the captured marbles for the player

                # Sets players last move
                self._players[player_name].set_last_move(marble_coordinate, movement_direction)
                self._game_board.set_state_of_board("R")  # Update count of red marbles on board
                self._game_board.set_grid(made_move[1])   # Update game board
                self._current_turn = self.update_current_turn(player_name)  # Update the current turn

                if self._players[player_name].get_red_marbles() == 7:    # Check if the player has won
                    self._winner = player_name
                    return True

                return True

            elif made_move[0] == "X":
                # Sets players' last move
                self._players[player_name].set_last_move(marble_coordinate, movement_direction)
                self._game_board.set_grid(made_move[1]) # Updates the game board
                self._current_turn = self.update_current_turn(player_name)  # Updates the current turn
                return True

            # Checks if the player is removing their marble
            elif made_move[0] == self._players[player_name].get_marble_color():
                self._current_turn = self.update_current_turn(player_name)  # Updates the current turn
                return False
            else:
                # Sets players' last move
                self._players[player_name].set_last_move(marble_coordinate, movement_direction)
                self._current_turn = self.update_current_turn(player_name)  # Updates the current turn
                self._game_board.set_grid(made_move[1]) # Updates the game board
                self._game_board.set_state_of_board(made_move[0])   # Updates the count of marbles on board

                if self._player1.get_marble_color() == made_move[0]:
                    self._player1.set_marbles() # Updates player 1's marble count

                    if self._player1.get_marbles() == 0: # Checks if player 1 has marbles on the board
                        self._winner = player_name
                        return True

                    return True

                elif self._player2.get_marble_color() == made_move[0]:
                    self._player2.set_marbles() # Updates player 2's marble count

                    if self._player2.get_marbles() == 0:    # Checks if player 2 has marbles on the board
                        self._winner = player_name
                        return True

                    return True

        except IndexError:
            return "This player is not in this game."
