def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        data = file.readlines()
    return [line.strip().split() for line in data]

def count_safe_rows(data):
    safe_count = 0
    
    for row in data:
        numbers = list(map(int, row))
        is_safe = True
        direction = None  # increase or decrease
        
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            if not (1 <= abs(diff) <= 3):
                is_safe = False
                break
            if diff > 0:  # Increasing
                if direction is None:
                    direction = 'increase'
                elif direction == 'decrease':  
                    is_safe = False
                    break
            elif diff < 0:  # Decreasing
                if direction is None:
                    direction = 'decrease'
                elif direction == 'increase':  
                    is_safe = False
                    break
        
        if is_safe:
            safe_count += 1
    
    return safe_count

data = read_input_file()
safe_rows = count_safe_rows(data)
print(f"Number of safe rows: {safe_rows}")