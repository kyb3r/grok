import copy

DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
DOT    = '.'
GHOST  = 'G'
PACMAN = 'P'
SPACE  = ' '
WALL   = '#'

def best_path(grid, ghost):
  todo = []  # [ [ (row, col) ] ]
  seen = set()  # { (row, col) }
  
  todo.append([ghost])
  while todo:
    path = todo.pop(0)
    cr, cc = path[-1]
    if grid[cr][cc] == PACMAN:
      return path
    if (cr, cc) in seen:
      continue
    seen.add((cr, cc))
    for dr, dc in DIRS:
      r, c = cr + dr, cc + dc
      if (r, c) not in path and grid[r][c] != WALL:
        new_path = path + [(r, c)]
        todo.append(new_path)

input_grid, ghosts, pacman = [], [], None
with open('maze.txt') as f:
  for r, line in enumerate(f):
    row = list(line.strip())
    input_grid.append(row)
    for c, cell in enumerate(row):
      if cell == PACMAN:
        pacman = (r, c)
      elif cell == GHOST:
        ghosts.append((r, c))

output_grid = copy.deepcopy(input_grid)
for ghost in ghosts:
  path = best_path(input_grid, ghost)
  r, c = ghost
  output_grid[r][c] = SPACE
  r, c = path[1]
  output_grid[r][c] = GHOST
  
for row in output_grid:
  print(''.join(row))