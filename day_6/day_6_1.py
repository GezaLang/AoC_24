def read_grid(file_path):
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def guard_move(grid):
    """
    -Locates a guard (`^`, `v`, `<`, `>`) in the grid and moves it.
    -The guard follows:
        - If there is an obstacle # directly in front, turn right 90 degrees.
        - Otherwise, take a step forward.
    -Marks visited positions with `X` and stops when the guard leaves the grid.
    This step is not even really necessary, as we will return len(visited) anyway.
    """
    directions = ['^', '>', 'v', '<'] 
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dy, dx)

    rows, cols = len(grid), len(grid[0])
    grid = [list(line) for line in grid] #mutable 
    #guard init pos 
    guard_pos = None
    guard_dir = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] in directions:
                guard_pos = (y, x)
                guard_dir = directions.index(grid[y][x])
                break
        if guard_pos: #found
            break
    #a check whether the guard was found would be reasonable 

    visited = set()
    while True:
        y, x = guard_pos
        visited.add((y, x))
        grid[y][x] = 'X'  # Mark position
        #one step in direction 
        dy, dx = steps[guard_dir] 
        ny, nx = y + dy, x + dx
        """
        Every case: 
        Upward (^): ny becomes -1 → 0 <= ny < rows fails.
        Downward (v): ny becomes rows → 0 <= ny < rows fails.
        Left (<): nx becomes -1 → 0 <= nx < cols fails.
        Right (>): nx becomes cols → 0 <= nx < cols fails.
        -> works
        """
        if not (0 <= ny < rows and 0 <= nx < cols):
            break
        if grid[ny][nx] == '#':
            guard_dir = (guard_dir + 1) % 4 # next dir modulo 4 -> last dir+1 = first dir
        else:
            guard_pos = (ny, nx)
    
    return len(visited)

grid = read_grid()
distinct_steps = guard_move(grid)
print(f"Total distinct positions visited: {distinct_steps}")