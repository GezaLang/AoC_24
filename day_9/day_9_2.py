
with open('input.txt', 'r') as file:
    input_data = file.read().strip()
lengths = [int(num) for num in input_data if num.isdigit()]
grid = [i // 2 if i % 2 == 0 else '.' for i, num in enumerate(lengths) for _ in range(num)]

# Compaction process: Move files in descending order of file ID
file_id = max(block for block in grid if block != '.')  # Start with the highest file ID
while file_id >= 0:
    file_indices = [i for i, block in enumerate(grid) if block == file_id]
    file_length = len(file_indices)

    moved = False
    for start in range(len(grid) - file_length + 1):
        # Check if there is a continuous free space on the left
        if all(grid[i] == '.' for i in range(start, start + file_length)):
            # Ensure it's to the left of the current file position
            if start < file_indices[0]:
                # Move the file only if there's space to the left
                for idx in file_indices:
                    grid[idx] = '.'  
                for i in range(start, start + file_length):
                    grid[i] = file_id 
                moved = True
                break  # Stop once the file is moved
    file_id -= 1

checksum = sum(i * int(block) for i, block in enumerate(grid) if block != '.')
print(f"Final checksum: {checksum}")