from typing import List

def read_input(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read().strip()

def parse_shapes(data: str): #-> (List[str], List[str]):
    shapes = data.split('\n\n')
    keys, locks = [], []
    for shape in shapes:
        G = shape.split('\n')
        R, C = len(G), len(G[0])
        is_key = all(G[0][c] != '#' for c in range(C))
        if is_key:
            keys.append(shape)
        else:
            locks.append(shape)
    return keys, locks

def fits(key: List[str], lock: List[str]) -> bool:
    R, C = len(key), len(key[0])
    assert R == len(lock) and C == len(lock[0])
    for r in range(R):
        for c in range(C):
            if key[r][c] == '#' and lock[r][c] == '#':
                return False
    return True

def solver(file_path: str) -> int:
    data = read_input(file_path)
    keys, locks = parse_shapes(data)
    count = 0
    for key in keys:
        for lock in locks:
            if fits(key.split('\n'), lock.split('\n')):
                count += 1
    return count

if __name__ == "__main__":
    input_file = 'input.txt' 
    result = solver(input_file)
    print(result)