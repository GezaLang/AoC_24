def import_data(filename):
    with open(filename, "r") as file:
        return file.read().strip().split("\n")

def prune(value):
    return value % 16777216

def mix(value1, value2):
    return value1 ^ value2 # XOR operation

def generate_prices(initial):
    """Generates a list of 2000 pseudorandom prices."""
    prices = [initial]
    for _ in range(2000):
        current = prices[-1]
        current = prune(mix(current, 64 * current))
        current = prune(mix(current, current // 32))
        current = prune(mix(current, current * 2048))
        prices.append(current)
    return prices

def solve_part1(data):
    total = sum(generate_prices(int(line))[-1] for line in data)
    return total

if __name__ == "__main__":
    input_file = "input.txt"
    data = import_data(input_file)
    result = solve_part1(data)
    print(result)
