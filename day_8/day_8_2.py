def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

data = read_input_file()

def parse_map(data):
    freq_positions = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != '.':
                if char not in freq_positions:
                    freq_positions[char] = []
                freq_positions[char].append((row, col))
    return freq_positions

def generate_antinodes(freq_positions, max_rows, max_cols):
    antinodes = set()
    for freq, positions in freq_positions.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate possible antinodes
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                # Distance and direction between antennas
                dr, dc = r2 - r1, c2 - c1
                # Generate all intermediate antinodes in line between antennas
                k = 1
                while True:
                    antinode = (r1 + k * dr, c1 + k * dc)
                    if 0 <= antinode[0] < max_rows and 0 <= antinode[1] < max_cols:
                        antinodes.add(antinode)
                    else:
                        break
                    k += 1
                
                k = 1
                while True:
                    antinode = (r1 - k * dr, c1 - k * dc)
                    if 0 <= antinode[0] < max_rows and 0 <= antinode[1] < max_cols:
                        antinodes.add(antinode)
                    else:
                        break
                    k += 1

                # Add the positions of the antennas themselves if they are in line
                antinodes.add((r1, c1))
                antinodes.add((r2, c2))
    return antinodes

def count_unique_antinodes(data):
    max_rows = len(data)
    max_cols = len(data[0])
    freq_positions = parse_map(data)
    antinodes = generate_antinodes(freq_positions, max_rows, max_cols)
    return len(antinodes)

print(count_unique_antinodes(data))