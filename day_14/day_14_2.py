import re
from collections import deque

def load_robot_data(file_path):
    with open(file_path) as file:
        lines = file.read().strip().splitlines()
    robots = [tuple(map(int, re.findall(r'-?\d+', line))) for line in lines]
    return robots

def count_connected_components(grid, width, height):
        """Count connected components of '#' in the grid using BFS."""
        seen = set()
        components = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, right, down, left

        for y in range(height):
            for x in range(width):
                if grid[y][x] == '#' and (x, y) not in seen:
                    components += 1
                    queue = deque([(x, y)])
                    while queue:
                        cx, cy = queue.popleft()
                        if (cx, cy) in seen:
                            continue
                        seen.add((cx, cy))
                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '#':
                                queue.append((nx, ny))
        return components

def find_easter_egg(robots, grid_width=101, grid_height=103, max_components=200):
    time_step = 1

    while True:
        grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]

        for i, (px, py, vx, vy) in enumerate(robots):
            px = (px + vx) % grid_width
            py = (py + vy) % grid_height
            robots[i] = (px, py, vx, vy)
            grid[py][px] = '#'

        components = count_connected_components(grid, grid_width, grid_height)
        if components <= max_components:
            print(f"Time: {time_step}") 
            print("\n".join("".join(row) for row in grid))
            return time_step  #elapsed time

        time_step += 1

if __name__ == "__main__":
    file_path = "input.txt"  
    robots = load_robot_data(file_path)
    time_to_tree = find_easter_egg(robots)
    print("Time to tree pattern:", time_to_tree)