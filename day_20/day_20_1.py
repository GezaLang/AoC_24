def load_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def locate_start_and_end(grid):
    start, end = None, None
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                start = (row_idx, col_idx)
            elif cell == 'E':
                end = (row_idx, col_idx)
    return start, end

def bfs(grid, start, include_walls=False, max_depth=float('inf')):
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {start: 0}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        current_distance = visited[current]
        if current_distance >= max_depth:
            continue

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                cell = grid[neighbor[0]][neighbor[1]]
                if neighbor not in visited and (cell in '.SE' or include_walls):
                    visited[neighbor] = current_distance + 1
                    queue.append(neighbor)
    return visited

def solve_part_one(input_file):
    grid = load_input(input_file)
    start, end = locate_start_and_end(grid)

    from_start = bfs(grid, start)
    from_end = bfs(grid, end)

    if end not in from_start:
        return 0

    default_length = from_start[end]
    results = []

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell not in '.SE':
                continue
            current = (row_idx, col_idx)
            if current not in from_start:
                continue
            distance_to_start = from_start[current]
            reachable_nodes = bfs(grid, current, include_walls=True, max_depth=2)
            for node, steps in reachable_nodes.items():
                if grid[node[0]][node[1]] not in '.SE':
                    continue
                if node not in from_end:
                    continue
                distance_to_end = from_end[node]
                total_time = distance_to_start + steps + distance_to_end
                time_gain = default_length - total_time
                if time_gain >= 100:
                    results.append(time_gain)
    return len(results)

if __name__ == "__main__":
    input_file = "input.txt"
    print("Part One:", solve_part_one(input_file))


