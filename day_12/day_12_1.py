from collections import deque

def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_neighbors(x, y, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def compute_cost(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_cost = 0

    def bfs(x, y):
        """Perform BFS to find a region's area and perimeter."""
        queue = deque([(x, y)])
        visited[x][y] = True
        region_char = grid[x][y]
        area = 0
        perimeter = 0

        while queue:
            cx, cy = queue.popleft()
            area += 1
            local_perimeter = 4  # each cell starts with 4 sides
            for nx, ny in get_neighbors(cx, cy, rows, cols):
                if grid[nx][ny] == region_char:  # same region
                    local_perimeter -= 1
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            perimeter += local_perimeter
        return area, perimeter

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, perimeter = bfs(i, j)
                total_cost += area * perimeter

    return total_cost

data = read_input_file()
grid = [list(line) for line in data]
cost = compute_cost(grid)
print(f"Final cost: {cost}")