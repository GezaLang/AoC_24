from collections import defaultdict

def import_data(filename):
    with open(filename, "r") as file:
        return file.read().strip().split("\n")

def prune(value):
    return value % 16777216

def mix(value1, value2):
    return value1 ^ value2

def generate_prices(initial):
    prices = [initial]
    for _ in range(2000):
        current = prices[-1]
        current = prune(mix(current, 64 * current))
        current = prune(mix(current, current // 32))
        current = prune(mix(current, current * 2048))
        prices.append(current)
    return prices

def price_changes(prices):
    return [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

def compute_scores(prices, changes):
    scores = {}
    for i in range(len(changes) - 3):
        pattern = tuple(changes[i : i + 4])
        if pattern not in scores:
            scores[pattern] = prices[i + 4]
    return scores

def solve_part2(data):
    """maximum bananas achievable."""
    overall_scores = defaultdict(int)
    for line in data:
        prices = generate_prices(int(line))
        price_last_digit = [price % 10 for price in prices]
        changes = price_changes(price_last_digit)
        scores = compute_scores(price_last_digit, changes)
        for pattern, score in scores.items():
            overall_scores[pattern] += score
    return max(overall_scores.values())

if __name__ == "__main__":
    input_file = "input.txt"
    data = import_data(input_file)
    result = solve_part2(data)
    print(result)
