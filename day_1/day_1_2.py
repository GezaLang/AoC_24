def read_input_file():
    with open('input.txt', 'r') as file:
        data = file.readlines()
    return [num for line in data for num in line.strip().split()]  # Flatten the input

data = read_input_file()

left_list = data[::2]  # Even-indexed entries
right_list = data[1::2]  # Odd-indexed entries

def calculate_similarity_score(left, right):
    right_counts = {}
    for num in right:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1
    similarity_score = 0
    for num in left:
        count_in_right = right_counts.get(num, 0)  # Get count or 0 if not in the right list
        similarity_score += int(num) * count_in_right  # Multiply number by its count
    return similarity_score

similarity_score = calculate_similarity_score(left_list, right_list)

print("Similarity Score:", similarity_score)

