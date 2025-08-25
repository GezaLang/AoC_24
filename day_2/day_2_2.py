"""
Remark: removing one is probably a bit ineffficient but as the length of the lists is small it aint a problem
"""
def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        data = file.readlines()
    return [line.strip().split() for line in data]

def count_safe_rows(data):
    safe_count = 0
    
    for row in data:
        numbers = list(map(int, row))

        if is_safe_row(numbers):
            safe_count += 1
        else:
            # If the row is unsafe, try removing one element and checking again
            for i in range(len(numbers)):
                modified_row = numbers[:i] + numbers[i+1:]  
                if is_safe_row(modified_row):
                    safe_count += 1
                    break
    
    return safe_count

def is_safe_row(numbers):
    direction = None  #increase or decrease
    
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        
        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:  # Increasing
            if direction is None:
                direction = 'increase'
            elif direction == 'decrease': 
                return False
        elif diff < 0:  # Decreasing
            if direction is None:
                direction = 'decrease'
            elif direction == 'increase': 
                return False
                
    return True

data = read_input_file()
safe_rows = count_safe_rows(data)
print(f"Number of safe rows: {safe_rows}")
