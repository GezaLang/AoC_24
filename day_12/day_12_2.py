import sys
from collections import deque
import pyperclip as pc

def read_input():
    infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
    data = open(infile).read().strip()
    return data.split('\n')

def initialize_seen(rows, cols):
    """Initializes the SEEN set."""
    return set()

def bfs_area_and_perimeter(grid, r, c, rows, cols, seen, dirs):
    """Performs BFS to calculate area and perimeter of a region."""
    queue = deque([(r, c)])
    area = 0
    perimeter = 0
    perimeter_map = dict()

    while queue:
        r2, c2 = queue.popleft()
        if (r2, c2) in seen:
            continue
        seen.add((r2, c2))
        area += 1

        for dr, dc in dirs:
            rr, cc = r2 + dr, c2 + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == grid[r2][c2]:
                queue.append((rr, cc))
            else:
                perimeter += 1
                if (dr, dc) not in perimeter_map:
                    perimeter_map[(dr, dc)] = set()
                perimeter_map[(dr, dc)].add((r2, c2))

    return area, perimeter, perimeter_map

def calculate_sides(perimeter_map, dirs):
    """Calculates the number of sides of the perimeter."""
    sides = 0
    for _, vs in perimeter_map.items():
        seen_perim = set()
        for pr, pc in vs:
            if (pr, pc) in seen_perim:
                continue
            sides += 1
            queue = deque([(pr, pc)])
            while queue:
                r2, c2 = queue.popleft()
                if (r2, c2) in seen_perim:
                    continue
                seen_perim.add((r2, c2))

                for dr, dc in dirs:
                    rr, cc = r2 + dr, c2 + dc
                    if (rr, cc) in vs:
                        queue.append((rr, cc))
    return sides

def process_grid(grid, rows, cols, dirs):
    """Processes the entire grid to calculate p1 and p2."""
    seen = initialize_seen(rows, cols)
    p1 = 0
    p2 = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue

            area, perimeter, perimeter_map = bfs_area_and_perimeter(grid, r, c, rows, cols, seen, dirs)
            sides = calculate_sides(perimeter_map, dirs)
            p1 += area * perimeter
            p2 += area * sides

    return p1, p2

def main():
    sys.setrecursionlimit(10**6)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    grid = read_input()
    rows = len(grid)
    cols = len(grid[0])
    p1, p2 = process_grid(grid, rows, cols, dirs)
    #print(p1)
    print(p2)


if __name__ == "__main__":
    main()