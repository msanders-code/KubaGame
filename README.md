# KubaGame
Files for a digital version of the board game 'Kuba'

Kuba is a board game involving marbles being pushed around and off a 7x7 board. There are
red, black, and white marbles; the black and white marbles are the players' marbles and
the red marbles are what each player can capture. A player wins if they capture 7 red
marbles by pushing them off the board or by pushing all of their opponents marbles off
the board. Each player starts with 8 marbles set in groups of 4 at diagonal corners and
the game starts with 13 red marbles in the center of the board. Full rules and a visual 
representation of the board can be seen here (https://sites.google.com/site/boardandpieces/list-of-games/kuba).
In this version, any player starts the game and no player gets a second turn; They can
only try again if they attempt to make an invalid move.

There are three classes within the main game code: Player, Board, and KubaGame. 

The player class defines everything related to players in the game; their name,
their marble color, it keeps track of their previous move(s), and the count of
their marbles left on the board. It also manipulates these attributes through
methods in the kubagame class.

The Board class defines everything to do with the game board; it defines and keeps
track of the current board state and the current count of every marble on the board.
These attributes get manipulated through the kubagame class.

The KubaGame class defines all the methods used for game play and initializes the game
board and both players. It holds methods to make moves, update the board, check for invalid
moves and to show specific attributes of the players and the board.

Future Work:
  - implement the Ko rule
  - create a GUI for the game
  - implement AI for single player games
  - translate to C# and create a version with the Unity engine 
 
