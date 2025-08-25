def read_grid(file_path) -> list:
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def count_xmas_shapes(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    diagonal_offsets = [
        (-1, -1, 1, 1),  # up-left to down-right
        (-1, 1, 1, -1),  # up-right to down-left
    ]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':  # Center of the potential mas
                valid_xmas = True
                for dx1, dy1, dx2, dy2 in diagonal_offsets:
                    # Positions of "M" and "S" for each diagonal
                    mx1, my1 = i + dx1, j + dy1
                    sx1, sy1 = i - dx1, j - dy1
                    mx2, my2 = i + dx2, j + dy2
                    sx2, sy2 = i - dx2, j - dy2

                    # bound check -> got that with help of LLM 
                    if not all(0 <= nx < rows and 0 <= ny < cols for nx, ny in [(mx1, my1), (sx1, sy1), (mx2, my2), (sx2, sy2)]):
                        valid_xmas = False
                        break

                    diagonal_1 = [grid[mx1][my1], grid[i][j], grid[sx1][sy1]]
                    diagonal_2 = [grid[mx2][my2], grid[i][j], grid[sx2][sy2]]

                    if not (diagonal_1 in [['M', 'A', 'S'], ['S', 'A', 'M']] and
                            diagonal_2 in [['M', 'A', 'S'], ['S', 'A', 'M']]):
                        valid_xmas = False
                        break

                if valid_xmas:
                    count += 1

    return count

path = "input.txt"
grid = read_grid(path)
xmas_count = count_xmas_shapes(grid)
print(f"Total 'X-MAS' shapes found: {xmas_count}")
