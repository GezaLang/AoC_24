import sys
import re
from collections import deque

# up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def read_input(file_path='input.txt'):
    with open(file_path) as f:
        data = f.read().strip()
    grid_data, instructions = data.split('\n\n')
    grid = grid_data.split('\n')
    return grid, instructions

def solve_part2(grid, instructions):
    R, C = len(grid), len(grid[0])
    G = [[grid[r][c] for c in range(C)] for r in range(R)]
    BIG_G = []
    for r in range(R):
        row = []
        for c in range(C):
            if G[r][c] == '#':
                row.extend(['#', '#'])
            elif G[r][c] == 'O':
                row.extend(['[', ']'])
            elif G[r][c] == '.':
                row.extend(['.', '.'])
            elif G[r][c] == '@':
                row.extend(['@', '.'])
        BIG_G.append(row)
    G = BIG_G
    C *= 2

    for r in range(len(G)):
        for c in range(len(G[r])):
            if G[r][c] == '@':
                sr, sc = r, c
                G[r][c] = '.'

    r, c = sr, sc
    for inst in instructions:
        if inst == '\n':
            continue
        dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[inst]
        rr, cc = r + dr, c + dc

        if G[rr][cc] == '#':
            continue
        elif G[rr][cc] == '.':
            r, c = rr, cc
        elif G[rr][cc] in ['[', ']', 'O']:
            # Push 
            Q = deque([(r, c)])
            SEEN = set()
            ok = True

            while Q:
                rr, cc = Q.popleft()
                if (rr, cc) in SEEN:
                    continue
                SEEN.add((rr, cc))

                rrr, ccc = rr + dr, cc + dc
                if G[rrr][ccc] == '#':
                    ok = False
                    break
                if G[rrr][ccc] == 'O':
                    Q.append((rrr, ccc))
                elif G[rrr][ccc] == '[':
                    Q.append((rrr, ccc))
                    assert G[rrr][ccc + 1] == ']'
                    Q.append((rrr, ccc + 1))
                elif G[rrr][ccc] == ']':
                    Q.append((rrr, ccc))
                    assert G[rrr][ccc - 1] == '['
                    Q.append((rrr, ccc - 1))

            if not ok:
                continue

            # Apply the push
            while len(SEEN) > 0:
                for rr, cc in sorted(SEEN):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in SEEN:
                        assert G[rrr][ccc] == '.'
                        G[rrr][ccc] = G[rr][cc]
                        G[rr][cc] = '.'
                        SEEN.remove((rr, cc))
            r, c = r + dr, c + dc

    ans = 0
    for r in range(len(G)):
        for c in range(len(G[r])):
            if G[r][c] in ['[', 'O']:
                ans += 100 * r + c
    return ans

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    grid, instructions = read_input(input_file)
    result = solve_part2(grid, instructions)
    print(result)