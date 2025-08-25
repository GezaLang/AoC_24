import collections

#deleted the simulate_bytes function as it is not needed anymore, 
#besides that it´s mostly copied from 1 
def load_byte(filename):
    with open(filename, "r") as file:
        return [tuple(map(int, line.strip().split(','))) for line in file if line.strip()]

def bfs_shortest_path(grid, start, end):
    queue = collections.deque([start])
    visited = set()
    visited.add(start)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            #instead of returning steps as in part 1
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False

#part 2 code here
def corrupted_path(byte_positions, grid, grid_size, start, end):
    for i, (x, y) in enumerate(byte_positions):
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = True  # change to corrupted

            if not bfs_shortest_path(grid, start, end):
                return f"{x},{y}"  
    return "No byte prevents reaching the exit."  

def main():
    grid_size = 71  #as we have values reaching from 0 to 70
    start = (0, 0)
    end = (70, 70)
    input_file = "input.txt"
    byte_positions = load_byte(input_file)
    grid = [[False] * grid_size for _ in range(grid_size)]  # False means safe
    print(corrupted_path(byte_positions, grid, grid_size, start, end))

if __name__ == "__main__":
    main()