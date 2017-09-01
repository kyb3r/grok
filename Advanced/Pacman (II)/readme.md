# Pacman (II)

In this problem, we will extend upon the previous Pac Man problem. Here, you will need to allow a player to play Pac Man.

You will be given a file called maze.txt describing a Pac Man maze. The file will be in the following format:

`maze.txt`
```
########
#......#
# ## #.#
#.#P.#.#
#G . #G#
########
```
Pac Man will appear once in the maze and is represented by `P`. Ghosts are represented by `G`, impenetrable walls by `#`, pac dots by `.`, and empty floor space by a space. The maze will always have an outside border of walls. The initial position of the ghosts do not contain pac dots.

The rules about ghosts and their movement is the same as it was in the previous Pac Man problem, except that this time, ghosts do not consume pac dots. Instead, they leave untouched any pac dots they move over.

Your program should read in a single line of input from the user: a space separated list of single letter instructions. The set of instructions are as follows:

 * `U`: move Pac Man up one square this turn
 * `D`: move Pac Man down one square this turn
 * `L`: move Pac Man left one square this turn
 * `R`: move Pac Man right one square this turn
 * `O`: print out the current state of the game. This does not result in a turn of the game happening.

When a turn of the game occurs due to user input, the following should happen in this order:

1. Pac Man makes his move;
2. Check for game ending conditions (see below);
3. All of the ghosts take a single step;
4. Check for game ending conditions (see below).

The ghosts are aiming to move towards where Pac Man was before the step he just took. If the input is O, then no movement on the board should occur. If the players movement command moves Pac Man into a wall, Pac Man remains stationary that turn instead.

When Pac Man moves over a pac dot, the pac dot is consumed and the players points are increased by one. The player starts off with zero points. When a pac dot is consumed, empty floor space replaces the cell that the pac dot was in.

The game ends when one of the following three conditions occur:

1. Pac Man runs into a ghost, or vice versa. If this occurs, your program should output You died! followed by the final game configuration.
2. Pac Man consumes all of the pac dots. If this occurs, your program should output You won! followed by the final game configuration.
3. Neither of the previous two situations occurred and there was no more user commands to execute. In this case, the final game configuration should be printed.

If Pac Man moves onto a square that contains a ghost and a pac dot, the pac dot should not be consumed as Pac Man has died.

The output format for the game is as follows: a line starting with Points:, followed by how many points the player currently has. After this line, you should print out the board in the same format as it was read in. The one exception to this is when Pac Man and a ghost are on the same square (and thus Pac Man has died). In that case, you should output a X instead of a P or a G.

Here are three example interactions with your program, using the example maze.txt above:

```
Commands: R U O R U R R
Points: 1
########
#......#
# ##P#G#
#.#  #.#
#  G # #
########
You died!
Points: 2
########
#... X.#
# ## #.#
#.# G#.#
#  . # #
########
```
```
Commands: R U U L L L L
Points: 5
########
#PGG ..#
# ## #.#
#.#  #.#
#  . # #
########
```
```
Commands: R U U L L L L D D D R R R U U U R R D D
You won!
Points: 11
########
#    GG#
# ## # #
# #  #P#
#    # #
########
```
There will always be at least one pac dot in the maze.
