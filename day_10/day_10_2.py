from collections import deque

def read_input():
    input_path = "input.txt"
    with open(input_path, "r") as f:
        data = f.read().strip()
    return [[int(x) for x in row] for row in data.split("\n")]

def dp_trailhead_rating(grid, r, c, rows, cols, memo):
    """using memoized recursion."""
    if grid[r][c] == 9:
        return 1
    if (r, c) in memo:
        return memo[(r, c)]
    count = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == grid[r][c] + 1:
            count += dp_trailhead_rating(grid, rr, cc, rows, cols, memo)

    memo[(r, c)] = count
    return count

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    total_rating = 0
    memo = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += dp_trailhead_rating(grid, r, c, rows, cols, memo)
    return total_rating

if __name__ == "__main__":
    grid = read_input()
    result = solve(grid)
    print(f"Solution: {result}")