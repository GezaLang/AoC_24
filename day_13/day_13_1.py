import re

def read_input(file_path):
    file_path = file_path
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def extract_coordinates(data):
    """
    Extracts lists A, B, and Prize from the input data.
    """
    pattern_a = r"Button A: X\+(\d+), Y\+(\d+)"
    pattern_b = r"Button B: X\+(\d+), Y\+(\d+)"
    pattern_prize = r"Prize: X=(\d+), Y=(\d+)"
    # Extract data using regex
    list_a = re.findall(pattern_a, data)
    list_b = re.findall(pattern_b, data)
    list_prize = re.findall(pattern_prize, data)

    list_a = [(int(x), int(y)) for x, y in list_a]
    list_b = [(int(x), int(y)) for x, y in list_b]
    list_prize = [(int(x), int(y)) for x, y in list_prize]
    
    return list_a, list_b, list_prize

def gcd_extended(a, b):
    """
    Extended Euclidean algorithm.
    Returns gcd(a, b) and the coefficients x, y of the equation a*x + b*y = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

def find_min_cost(a_move, b_move, prize):
    x_A, y_A = a_move
    x_B, y_B = b_move
    x_prize, y_prize = prize
    # Check if solution exists for both x and y axes
    gcd_x, x_coef, y_coef = gcd_extended(x_A, x_B)
    gcd_y, x_coef_y, y_coef_y = gcd_extended(y_A, y_B)
    # If the prize coordinates are not divisible by the gcds, no solution exists
    if x_prize % gcd_x != 0 or y_prize % gcd_y != 0:
        return float('inf'), 0, 0  # Impossible to win this prize
    # Scale the coefficients
    x_coef *= x_prize // gcd_x
    y_coef *= y_prize // gcd_y
    # Try all combinations of n_A and n_B within 0 to 100
    min_cost = float('inf')
    best_n_A, best_n_B = 0, 0
    for n_A in range(101):
        for n_B in range(101):
            new_x = n_A * x_A + n_B * x_B
            new_y = n_A * y_A + n_B * y_B
            if new_x == x_prize and new_y == y_prize:
                cost = 3 * n_A + n_B
                if cost < min_cost:
                    min_cost = cost
                    best_n_A, best_n_B = n_A, n_B

    return min_cost, best_n_A, best_n_B

file_path = "input.txt"
input_data = read_input(file_path)
list_a, list_b, list_prize = extract_coordinates(input_data)
total_cost = 0
prizes_won = 0

for a_move, b_move, prize in zip(list_a, list_b, list_prize):
    cost, n_A, n_B = find_min_cost(a_move, b_move, prize)
    if cost != float('inf'):
        total_cost += cost
        prizes_won += 1
        print(f"Machine solved with cost {cost}: A={n_A}, B={n_B}")

print(f"Total prizes won: {prizes_won}")
print(f"Minimum tokens spent: {total_cost}")
