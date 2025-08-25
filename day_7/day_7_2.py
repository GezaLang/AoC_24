import itertools
def read_input_file():
    path = "input.txt"
    with open(path, 'r') as file:
        return file.readlines()

def splitting_lhs_rhs(data):
    parsed_data = []
    for line in data:
        lhs, rhs = line.split(':', 1)  #lhs ans rhs
        lhs = int(lhs.strip())  
        rhs = [int(x.strip()) for x in rhs.split()]  # list of integers
        parsed_data.append((lhs, rhs))  
    return parsed_data

def evaluate_row(lhs, rhs):
    """
    Evaluate all possible operator combinations for a given row.
    Return True if any combination matches the LHS.
    """
    n = len(rhs) - 1  
    operators = ['+', '*', '||']  
    for ops in itertools.product(operators, repeat=n):
        result = rhs[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += rhs[i + 1]
            elif op == '*':
                result *= rhs[i + 1]
            elif op == '||':
                result = int(str(result) + str(rhs[i + 1]))
        if result == lhs:
            return True
    return False

def equation_match(parsed_data):
    valid_lhs_sum = 0
    for lhs, rhs in parsed_data:
        if evaluate_row(lhs, rhs):
            valid_lhs_sum += lhs
    return valid_lhs_sum

data = read_input_file()  
parsed_data = splitting_lhs_rhs(data)  
result = equation_match(parsed_data) 
print("Sum of valid LHS values:", result)

