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
    #added the start_distance, but besides that it is copied from the 1st task
    start_distance = {}

    while pq:
        cost, r, c, direction = heapq.heappop(pq)

        if (r, c, direction) not in start_distance:
            start_distance[(r, c, direction)] = cost
        if (r, c) == end:
            return cost, start_distance
        # if we have visited this state
        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

        # all possible movements
        for new_dir, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = r + dr, c + dc
            if is_valid_move(grid, nr, nc):
                rotation_cost = min(abs(new_dir - direction), 4 - abs(new_dir - direction)) * 1000
                new_cost = cost + 1 + rotation_cost
                heapq.heappush(pq, (new_cost, nr, nc, new_dir))

    return -1, {}  # no path 
#part 2 code 
def compute_optimal_paths(grid, end, start_distance, best_cost):
    """
    Compute all tiles on optimal paths using a modified Dijkstra.
    """
    # Priority queue: (cost, row, col, direction)
    pq = [(0, end[0], end[1], d) for d in range(4)]  # Start at end with all directions
    visited = set()
    end_distance = {}

    while pq:
        cost, r, c, direction = heapq.heappop(pq)
        # shortest distance to each state
        if (r, c, direction) not in end_distance:
            end_distance[(r, c, direction)] = cost
        # already visited
        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))
        dr, dc = DIRECTIONS[(direction+2)%4]
        rr, cc = r + dr, c + dc

        nr, nc = r + dr, c + dc
        if is_valid_move(grid, nr, nc):
            heapq.heappush(pq, (cost + 1, nr, nc, direction))
        # Add rotation states (similar logic as in Part 1)
        heapq.heappush(pq, (cost + 1000, r, c, (direction + 1) % 4))
        heapq.heappush(pq, (cost + 1000, r, c, (direction + 3) % 4))

    optimal_tiles = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            for direction in range(4):
                if (r, c, direction) in start_distance and (r, c, direction) in end_distance:
                    total_cost = start_distance[(r, c, direction)] + end_distance[(r, c, direction)]
                    if total_cost == best_cost:
                        optimal_tiles.add((r, c))

    return len(optimal_tiles)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]
    best_cost, start_distance = dijkstra_min_score(grid)
    end = find_position(grid, 'E')
    optimal_tiles_count = compute_optimal_paths(grid, end, start_distance, best_cost)
    print("Number of tiles on optimal paths:", optimal_tiles_count)