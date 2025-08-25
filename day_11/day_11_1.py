from typing import List

def import_data(filepath: str) -> List[int]:
    with open(filepath) as file:
        return [int(x) for x in file.read().strip().split()]

def simulate_stone_evolution(x: int, t: int) -> int:
    """Calculates the resulting length of the list after evolving stone x for t steps without memoization."""
    if t == 0:
        return 1
    elif x == 0:
        return simulate_stone_evolution(1, t - 1)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left, right = int(dstr[:len(dstr) // 2]), int(dstr[len(dstr) // 2:])
        return simulate_stone_evolution(left, t - 1) + simulate_stone_evolution(right, t - 1)
    else:
        return simulate_stone_evolution(x * 2024, t - 1)

def solve(D: List[int], t: int) -> int:
    return sum(simulate_stone_evolution(x, t) for x in D)

if __name__ == "__main__":
    infile = 'input.txt'
    stones = import_data(infile)
    result = solve(stones, 25)
    print(result)