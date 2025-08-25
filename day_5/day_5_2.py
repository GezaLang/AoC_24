from collections import defaultdict

def parse_input():
    file_path = "input.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    ordering_rules = []
    updates = []
    for line in lines:
        line = line.strip()
        if "|" in line:
            # Parse ordering rules
            a, b = map(int, line.split("|"))
            ordering_rules.append((a,b))
        elif line:
            # Parse update lists
            updates.append(list(map(int, line.split(","))))
    
    return ordering_rules, updates

def validate_update(ordering_rules, update):
    positions = {value: idx for idx, value in enumerate(update)}
    for a, b in ordering_rules:
        if a in positions and b in positions:
            if positions[a] > positions[b]:
                return False
                break 
    return True

#new code 
def order_update(ordering_rules, update):#Reorders an update list to satisfy the ordering rules.
    # Create a graph from the update list and ordering rules
    graph = defaultdict(list) #from stack overflow
    in_degree = {value: 0 for value in update}
    for a, b in ordering_rules:
        if a in update and b in update:
            graph[a].append(b)
            in_degree[b] += 1
    # Perform sorting
    sorted_update = []
    queue = [node for node in update if in_degree[node] == 0]
    while queue:
        current = queue.pop(0)
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

def sum_of_middle_entries(ordering_rules, updates, reorder=False):
    middle_sum = 0
    for update in updates:
        if not validate_update(ordering_rules, update):
            # Reorder the invalid update
            sorted_update = order_update(ordering_rules, update)
            # Add the middle entry of the reordered update
            middle_sum += sorted_update[len(sorted_update) // 2]
    return middle_sum

ordering_rules, updates = parse_input()
middle_sum = sum_of_middle_entries(ordering_rules, updates, reorder=True)
print(f"Sum of middle entries after reordering invalid updates: {middle_sum}")