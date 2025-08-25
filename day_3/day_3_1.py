import re

def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        data = file.read()
    return data

text = read_input_file()
#print(data)

mul_pattern = re.compile(r'\b\w*mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)') #That had to be looked up online :D
results = []

for match in mul_pattern.finditer(text):
    num1, num2 = int(match.group(1)), int(match.group(2)) #extraction 
    result = num1 * num2 #actually calc. mul
    results.append((f"mul({num1}, {num2})", result)) #append to results

print("Extracted and Executed Calls:")
total_sum = 0
for func_call, value in results:
    print(f"{func_call} = {value}")
    total_sum += value

print(f"Total Sum: {total_sum}")
