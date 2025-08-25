import heapq
# Directions: East (0), South (1), West (2), North (3)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_position(grid, char):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == char:
                return (r, c)
    return None

def is_valid_move(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

def dijkstra_min_score(grid):
    start = find_position(grid, 'S')
    end = find_position(grid, 'E')
    if not start or not end:
        raise ValueError("Start (S) or End (E) not found in the grid.")

    # Priority queue: (cost, row, col, direction)
    pq = [(0, start[0], start[1], 0)]  # Start facing East (direction 0)
    visited = set()

    while pq:
        cost, r, c, direction = heapq.heappop(pq)

        if (r, c) == end:
            return cost
        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

        for new_dir, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = r + dr, c + dc
            if is_valid_move(grid, nr, nc):
                rotation_cost = min(abs(new_dir - direction), 4 - abs(new_dir - direction)) * 1000
                new_cost = cost + 1 + rotation_cost
                heapq.heappush(pq, (new_cost, nr, nc, new_dir))

    return -1  #no path is found

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]
    result = dijkstra_min_score(grid)
    print("Minimum score to reach the end:", result)