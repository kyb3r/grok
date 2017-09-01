import copy

class Pacman:
  
  PACMAN = 'P'
  GHOST = 'G'
  PACDOT = '.'
  WALL = '#'
  DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  COMMANDS = {
         'U': (-1, 0),
         'D': (1, 0),
         'L': (0, -1),
         'R': (0, 1),
         }
  
  def __init__(self, file):
    with open(file) as f:
      self.raw = f.read()
      self.grid = [list(i) for i in self.raw.splitlines()]
    self.score = 0 
    self.original_grid = self.grid.copy()
    self.pacdot_pos = self.pacdots() # Stores pacdot positions
    self.next_ghosts = [] # Stores the next moves the ghosts
    self.after_move = None # Stores the last pacman position after a move
    self.before_move = None # Stores the last pacman position before a move
    
  def pacdots(self):
    '''Returns all pacdot positions'''
    ret = set()
    for x, row in enumerate(self.original_grid):
      for y, val in enumerate(row):
        if val == self.PACDOT:
          ret.add((x, y))
    return ret
          
  @property
  def ghost_pos(self):
    '''Yields the positions of all ghosts'''
    for x, row in enumerate(self.grid):
      for y, val in enumerate(row):
        if val == self.GHOST:
          yield (x, y)
    
  @property
  def pacman_pos(self):
    '''Returns the current pacman position if there is one'''
    for x, row in enumerate(self.grid):
      for y, val in enumerate(row):
        if val == self.PACMAN:
          return (x, y)
        
  def best_path(self, x, y):
    '''BFS search to find the shortest path to the pacman'''
    todo = [] 
    seen = set() 
    todo.append([(x, y)])
    while todo:
      path = todo.pop(0)
      cr, cc = path[-1]
      if (cr, cc) == self.before_move:
        return path
      if (cr, cc) in seen:
        continue
      seen.add((cr, cc))
      for dr, dc in self.DIRS:
        r, c = cr + dr, cc + dc
        if (r, c) not in path and self.grid[r][c] != self.WALL and self.GHOST:
          new_path = path + [(r, c)]
          todo.append(new_path)
  
  def is_valid_pos(self, x, y):
    '''Checks if a move is valid.'''
    if x < len(self.grid):
      if y < len(self.grid[x]):
        if x >= 0 and y >= 0:
          if self.grid[x][y] != self.WALL:
            return True
      
  def move_pacman(self, x, y):
    '''Moves the pacman adding to the score if it eats a pacdot'''
    r, c = self.pacman_pos
    nr, nc = r+x, c+y
    if self.is_valid_pos(nr, nc):
      if self.grid[r][c] != self.GHOST:
        self.grid[r][c] = ' '
      if self.grid[nr][nc] == self.PACDOT:
        self.score += 1
        self.pacdot_pos.remove((nr, nc))
      self.grid[nr][nc] = self.PACMAN
    else:
      pass
    
  def process_commands(self, cmd):
    '''Processes the commnands and checks for win/loss conditions'''
    out = self.COMMANDS.get(cmd)
    if out:
      self.before_move = self.pacman_pos
      self.move_pacman(*out)
      self.after_move = self.pacman_pos
      if self.win_check():
        return True
      if self.lose_check():
        x, y = self.pacman_pos
        self.grid[x][y] = 'X'
        return False
      self.move_ghosts()
      if self.lose_check():
        x, y = self.after_move
        self.grid[x][y] = 'X'
        return False
    else:
      self.show_grid()
      
  def move_ghosts(self):
    '''Loops through all the ghosts and moves each one'''
    next_ghosts = []
    for i, ghost in enumerate(list(self.ghost_pos)):
      path = self.best_path(*ghost)
      next_ghosts.append(path[1])
    
    self.next_ghosts = next_ghosts
    
    for ng, og in zip(next_ghosts, list(self.ghost_pos)):
      self.move_ghost(og, *ng) # (original pos, future pos)
      
  def move_ghost(self, ghost, x, y):
    '''Moves a ghost, ignoring pacdots'''
    r, c = ghost
    if (r, c) in self.pacdot_pos:
      if (r, c) in self.next_ghosts:
        self.grid[r][c] = self.GHOST
      else:
        self.grid[r][c] = self.PACDOT
    else:
      if (r, c) in self.next_ghosts:
        self.grid[r][c] = self.GHOST
      else:
        self.grid[r][c] = ' '
    self.grid[x][y] = self.GHOST 
    
  def win_check(self):
    '''Checks if you have won'''
    return self.score == self.raw.count(self.PACDOT)
  
  def lose_check(self):
    '''Checks if the pacman is dead'''
    return self.afer_move in self.next_ghosts or not self.pacman_pos
    
  def show_grid(self, grid=None):
    ''''Prints out a the grid or a seperate grid if given'''
    grid = grid or self.grid
    print(f'Points: {self.score}')
    for row in grid:
      print(''.join(row))
  
  def input_commands(self):
    '''lol'''
    return input('Commands: ').split()
  
  def start(self):
    '''Takes in input and processes it.'''
    cmds = self.input_commands()
    for cmd in cmds:
      wincon = self.process_commands(cmd)
      if wincon is True:
        print('You won!')
        return self.show_grid()
      if wincon is False:
        print('You died!')
        return self.show_grid()
    self.show_grid()
    
  def vis_path(self, path):
    '''For visualising the path and debugging.'''
    g = copy.deepcopy(self.grid)
    for x, y in path[1:-1]:
      g[x][y] = '+'
    self.show_grid(g)

if __name__ == '__main__':
  maze = Pacman('maze.txt')
  maze.start()

  
