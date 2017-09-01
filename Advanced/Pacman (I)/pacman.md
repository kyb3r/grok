# Pacman (I)

In the classic arcade game Pac Man, you control a small hockey-puck shaped character through a maze. You accumulate points by eating pac dots, whilst trying to avoid four ghost enemies who kill you upon touch.

You will be given a file called maze.txt describing a Pac Man maze. The file will be in the following format:

`maze.txt`
```
############################
#  G  .   #      # ##.     #
######.## #      # ##.######
#    #.## ######## ##.#    #
#    #.##          ##.#    #
#    #.##### ## #####.#    #
######.#####.##.#####.######
#G.....##....##....##......#
#.####.##.########.##.####.#
#.####.##P########.##.####.#
#............G.............#
#.####.#####.##.#####.####.#
#.#  #.#   #.##.#   #.#  #.#
#.####.#####.##.#####.####.#
#............##...........G#
############################
```
Pac Man will appear once in the maze and is represented by `P`. Ghosts are represented by `G`, impenetrable walls by `#`, pac dots by `.`, and empty floor space by a space. The maze will always have an outside border of walls.

In this problem, each ghost will take one step along the shortest path that takes them to Pac Man, while Pac Man himself will not move. Your program should print out the maze as it will look after all ghosts takes this single step.

More than one ghost is allowed to occupy the same square on the maze. Ghosts with more than one possible shortest path to take should prefer to take their initial step in the following order: `up`, `left`, `down`, `right`. Ghosts cannot move diagonally.

To make this problem simpler, when a ghost leaves a square on the maze, the square they leave will always be empty floor space. Given the example maze above, your program should output:

```
############################
#   G .   #      # ##.     #
######.## #      # ##.######
#    #.## ######## ##.#    #
#    #.##          ##.#    #
#    #.##### ## #####.#    #
######.#####.##.#####.######
# .....##....##....##......#
#G####.##.########.##.####.#
#.####.##P########.##.####.#
#...........G .............#
#.####.#####.##.#####.####.#
#.#  #.#   #.##.#   #.#  #.#
#.####.#####.##.#####.####G#
#............##........... #
############################
```
Here is a simpler example. Given the following `maze.txt`:

`maze.txt`
```
###############
#             #
#G     P     G#
#             #
###############
```
your program should output:

```
###############
#             #
# G    P    G #
#             #
###############
​```

You are guaranteed that there exists a path from each ghost to Pac Man, and that ghosts in maze.txt will be more than one step away from Pac Man.

Your program will need to work with mazes that contain up to 10,000 squares.