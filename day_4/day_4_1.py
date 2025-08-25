def find_xmas_in_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0
    directions = [
        (0, 1),  # right
        (0, -1), # left
        (1, 0),  # down
        (-1, 0), # up
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:  # Start of "XMAS"
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        count += 1

    return count

path = "input.txt"
xmas_count = find_xmas_in_file(path)
print(f"Total 'XMAS' found: {xmas_count}")
