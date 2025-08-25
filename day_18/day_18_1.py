import collections

def load_byte(filename):
    with open(filename, "r") as file:
        return [tuple(map(int, line.strip().split(','))) for line in file if line.strip()]

def simulate_bytes(byte_positions, steps, grid_size):
    grid = [[False] * grid_size for _ in range(grid_size)]  # False means safe
    for i in range(min(steps, len(byte_positions))):
        x, y = byte_positions[i]
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = True  # Corrupted position
    return grid

def bfs_shortest_path(grid, start, end):
    queue = collections.deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # No valid path

def main():
    grid_size = 71  # as we have values reaching from 0 to 70
    start = (0, 0)
    end = (70, 70)
    steps_to_simulate = 1024  #first kilobyte :D 
    input_file = "input.txt"
    byte_positions = load_byte(input_file)

    grid = simulate_bytes(byte_positions, steps_to_simulate, grid_size)
    shortest = bfs_shortest_path(grid, start, end)
    if shortest != -1:
        print(f"The minimum number of steps to reach {end} is: {result}")
    else:
        print("No valid path to the destination.")

if __name__ == "__main__":
    main()