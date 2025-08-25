def read_grid():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

#modified a bit 
def guard_move(grid, obstruction_pos):

    directions = ['^', '>', 'v', '<'] 
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dy, dx)
    rows, cols = len(grid), len(grid[0])
    grid = [list(line) for line in grid]  # mutable
    # guard init pos
    guard_pos = None
    guard_dir = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] in directions:
                guard_pos = (y, x)
                guard_dir = directions.index(grid[y][x])
                break
        if guard_pos: # found
            break

    # a check whether the guard was found would be reasonable
    visited = set()  
    visited_positions = set()  
    #modified code 
    #new obstruction
    y, x = obstruction_pos
    grid[y] = grid[y][:x] + ['O'] + grid[y][x+1:]

    while True:
        y, x = guard_pos
        if (y, x, guard_dir) in visited:
            #true if position has already been visited with the same direction
            return True
        visited.add((y, x, guard_dir))  
        visited_positions.add((y, x)) 
        
        dy, dx = steps[guard_dir]
        ny, nx = y + dy, x + dx
        
        if not (0 <= ny < rows and 0 <= nx < cols):
            return False
        
        if grid[ny][nx] in ('#', 'O'):
            guard_dir = (guard_dir + 1) % 4  
        else:
            guard_pos = (ny, nx)
#new code
def obstructions(grid):
    """
    In this function we will try to add an obstruction at every empty space except the starting position.
    We will then simulate the guard's movement and check if it enters a loop.
    If it does, we will count this position as a valid obstruction.
    """
    rows = len(grid)
    cols = len(grid[0])

    valid_positions = 0
    # Try adding an obstruction at every empty space except the starting position
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '.':
                # copy of the grid to simulate with the new obstruction
                grid_copy = [line[:] for line in grid]
                # simulation with the new obstruction and check for a loop
                if guard_move(grid_copy, (y, x)):
                    valid_positions += 1
    
    return valid_positions

grid = read_grid()
valid_positions = obstructions(grid)
print(f"Total valid positions for obstruction: {valid_positions}")