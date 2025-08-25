def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        data = file.readlines()
    return [num for line in data for num in line.strip().split()]

data = read_input_file()
print(data)

left_list = data[::2]  
right_list = data[1::2] 

#print("Even-indexed entries:", left_list)
#print("Odd-indexed entries:", right_list)

#distance
def get_distance(): 
    left_list.sort()
    right_list.sort()
    distances_individual = []
    for i in range(len(left_list)):
        distances_individual.append(abs(int(left_list[i]) - int(right_list[i])))
    distance = sum(distances_individual)
    return distance

distance = get_distance()
print("Distance:", distance)