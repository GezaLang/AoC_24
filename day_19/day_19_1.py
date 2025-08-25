def process_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    parts = content.strip().split("\n\n")
    patterns = parts[0].split(", ")
    designs = parts[1].split("\n")
    return patterns, designs

def can_make_design(design, patterns):
    """
    Determines if a design can be made using the available patterns.
    """
    # Create a memoization dictionary to store results of subproblems
    memo = {}
    def helper(sub_design):
        # Base case: If the sub-design is empty, it's possible
        if not sub_design:
            return True
        # Check memoization to avoid redundant computation
        if sub_design in memo:
            return memo[sub_design]
        # Try to match the beginning of the sub-design with any pattern
        for pattern in patterns:
            if sub_design.startswith(pattern):
                # Recursively check the remaining substring
                if helper(sub_design[len(pattern):]):
                    memo[sub_design] = True
                    return True
        # If no pattern matches, the design is impossible
        memo[sub_design] = False
        return False

    return helper(design)

def count_possible_designs(patterns, designs):
    possible_count = sum(1 for design in designs if can_make_design(design, patterns))
    return possible_count

if __name__ == "__main__":
    file_path = "input.txt" 
    patterns, designs = process_input_file(file_path)
    possible_designs_count = count_possible_designs(patterns, designs)
    print(f"Number of possible designs: {possible_designs_count}")