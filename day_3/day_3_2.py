import re

def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        data = file.read()
    return data
text = read_input_file()

def extract_and_execute(text):
    # Regex patterns for mul, do, don't
    mul_pattern = re.compile(r'\b\w*mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    #do_pattern = re.compile(r"\bdo\(\)")      # 'do()'
    #dont_pattern = re.compile(r"\bdon't\(\)") #'don't()'

    is_enabled = True  # Default 
    results = []
    #character by character
    pos = 0
    while pos < len(text):
        if text[pos:pos+4] == "do()":
            is_enabled = True
            # print("State changed to ENABLED after do()") #Debugging
            pos += 4
        elif text[pos:pos+7] == "don't()":
            is_enabled = False
            # print("State changed to DISABLED after don't()") #Debugging
            pos += 6
        #more or less the same as in 1st part
        elif is_enabled and mul_pattern.match(text, pos):
            match = mul_pattern.match(text, pos)
            num1, num2 = int(match.group(1)), int(match.group(2))
            results.append((f"mul({num1}, {num2})", num1 * num2))
            print(f"mul({num1}, {num2}) executed, result = {num1 * num2}")
            pos = match.end()  # Move position to the end of the match
        else:
            pos += 1  

    print("Extracted and Executed Calls:")
    total_sum = 0
    for func_call, value in results:
        print(f"{func_call} = {value}")
        total_sum += value

    print(f"Total Sum: {total_sum}")

extract_and_execute(text)  