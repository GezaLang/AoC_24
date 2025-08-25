def read_grid():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def find_trailhead_scores(data): #A trailhead´s score is the number of distinct '9' positions reachable via hiking trails.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    trailhead_scores = {}

    def dfs(x, y, visited, reachable_nines): #depth first search
        visited.add((x, y))
        if data[x][y] == '9':
            reachable_nines.add((x, y))
        
        next_num = int(data[x][y]) + 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows and 0 <= ny < cols and
                (nx, ny) not in visited and
                data[nx][ny].isdigit() and int(data[nx][ny]) == next_num
            ):
                dfs(nx, ny, visited, reachable_nines)

    # Start searching from all trailheads
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '0':  # Found a trailhead
                reachable_nines = set()
                dfs(i, j, set(), reachable_nines)
                trailhead_scores[(i, j)] = len(reachable_nines)
    
    return trailhead_scores

data = read_grid()
trailhead_scores = find_trailhead_scores(data)
total_score = sum(trailhead_scores.values())
print(f"The total sum of all trailhead scores is: {total_score}")