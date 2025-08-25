from typing import List
"""
This solution uses memoization to avoid recalculating the same values multiple times.
"""
def import_data(filepath: str) -> List[int]:
    with open(filepath) as file:
        return [int(x) for x in file.read().strip().split()]

def simulate_stone_evolution_memo(x: int, t: int, memo: dict) -> int:
    """Calculates the resulting length of the list after evolving stone x for t steps with memoization."""
    if (x, t) in memo:
        return memo[(x, t)]

    if t == 0:
        result = 1
    elif x == 0:
        result = simulate_stone_evolution_memo(1, t - 1, memo)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left, right = int(dstr[:len(dstr) // 2]), int(dstr[len(dstr) // 2:])
        result = simulate_stone_evolution_memo(left, t - 1, memo) + simulate_stone_evolution_memo(right, t - 1, memo)
    else:
        result = simulate_stone_evolution_memo(x * 2024, t - 1, memo)

    memo[(x, t)] = result
    return result

def solve(D: List[int], t: int) -> int:
    memo = {}
    return sum(simulate_stone_evolution_memo(x, t, memo) for x in D)

if __name__ == "__main__":
    infile = 'input.txt'
    stones = import_data(infile)
    result = solve(stones, 75)
    print(result)
