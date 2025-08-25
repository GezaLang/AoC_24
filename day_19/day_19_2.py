def process_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    parts = content.strip().split("\n\n")
    patterns = parts[0].split(", ")
    designs = parts[1].split("\n")
    return patterns, designs

#pretty similar to can_make_design, changed a bit
def count_arrangements(design, patterns):
    memo = {}
    def helper(sub_design):
        if not sub_design: #Base case
            return 1 # instead of True as in first assignment 

        if sub_design in memo:
            return memo[sub_design]

        #the next part differs a bit from the first part 
        # Calculate the total number of ways for the current sub-design
        total_ways = 0
        for pattern in patterns:
            if sub_design.startswith(pattern):
                # Recursively calculate arrangements for the remaining substring
                total_ways += helper(sub_design[len(pattern):])

        memo[sub_design] = total_ways
        return total_ways

    return helper(design)


def total_arrangements(patterns, designs):
    total = 0
    for design in designs:
        total += count_arrangements(design, patterns)
    return total

if __name__ == "__main__":
    file_path = "input.txt"  
    patterns, designs = process_input_file(file_path)

    total = total_arrangements(patterns, designs)
    print(f"Total number of arrangements: {total}")