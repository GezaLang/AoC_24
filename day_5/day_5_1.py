def parse_input()-> tuple:
    file_path = "input.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    ordering_rules = []
    updates = []
    for line in lines:
        line = line.strip()
        if "|" in line:
            a, b = map(int, line.split("|"))
            ordering_rules.append((a,b))
        elif line:
            updates.append(list(map(int, line.split(","))))
    return ordering_rules, updates

def validate_update(ordering_rules, update)->bool:
    positions = {value: idx for idx, value in enumerate(update)}
    for a, b in ordering_rules:
        if a in positions and b in positions:
            if positions[a] > positions[b]:
                return False
                break 
    return True

def sum_medians(ordering_rules, updates)-> int:
    middle_sum = 0
    for update in updates:
        if validate_update(ordering_rules, update):
            middle_sum += update[len(update) // 2] # Add the middle entry of the valid update
    return middle_sum

ordering_rules, updates = parse_input()
result = sum_medians(ordering_rules, updates)
print(f"Sum of medians of valid updates: {result}")