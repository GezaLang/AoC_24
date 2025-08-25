with open('input.txt', 'r') as file:
    input_data = file.read().strip()

# Process each character as an integer directly if possible
# This assumes each digit in the file is meant to be a separate number
lengths = [int(num) for num in input_data if num.isdigit()]
grid = [i // 2 if i % 2 == 0 else '.' for i, num in enumerate(lengths) for _ in range(num)]

while '.' in grid:
    if grid[-1] == '.':
        grid.pop()
    else:
        index = grid.index('.')
        grid[index] = grid.pop()

answer = sum(i * num for i, num in enumerate(grid))
print(answer)