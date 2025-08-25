def run_program(registers, program, part2=False):
    """
    Part 2 was quite tricky to solve. Simple brute-forcing was not really possible due to the huge 
    problem size. I had to combine analysis and brute-forcing to find the correct value of register A. 
    It is essential to see the commonalities between the opcodes (base 8) and that basically only the 
    first few bits of A are important. So we can analyze A and guess the first few bits according 
    to the output (after 2-3 common iterations it is assumed that the bits are correct). 
    If we then have 8 bits, we can brute force the rest pretty fast. (Note that 8 worked for me after two 
    steps, more bits are of course always better :D)
    Also note that the bits obviously depend on the input.
    """
    # Basically all copied from 1st part 
    A, B, C = registers['A'], registers['B'], registers['C']
    instruction_pointer = 0
    output = []

    def oper(operand):
        if operand in [0, 1, 2, 3]:
            return operand  # values
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand == 7:  
            raise ValueError("Invalid operand 7 encountered!")
        else:
            raise ValueError(f"Unexpected operand {operand}")

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
    #here we just go trough the instructions
        if opcode == 0:  # adv
            denominator = 2 ** oper(operand)
            A = A // denominator
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = oper(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(oper(operand) % 8)
        ####Change from 1st part -> early termination check 
            if part2 and output[-1] != program[len(output) - 1]:
                return output
        elif opcode == 6:  # bdv
            denominator = 2 ** oper(operand)
            B = A // denominator
        elif opcode == 7:  # cdv
            denominator = 2 ** oper(operand)
            C = A // denominator
        else:
            raise ValueError(f"Unknown opcode {opcode} encountered!")
        instruction_pointer += 2  
    return output

#Part 2 code 
def find_correct_register_A(program, analysis_offset):

    A_helper = 0
    best_output_length = 0

    while True:
        A_helper += 1
        #first step (5 bits):
        #A_candidate = A_helper * 8**5 + analysis_offset_old
        #second step (8 bits):
        A_candidate = A_helper * 8**8 + analysis_offset
        registers = {'A': A_candidate, 'B': 0, 'C': 0}

        output = run_program(registers, program, part2=True)
        if output == program:
            print(f"Solution found: A = {A_candidate} (octal: {oct(A_candidate)})")
            return A_candidate

        #for analysis
        elif len(output) > best_output_length:
            best_output_length = len(output)
            print(f"New best output length: {best_output_length}")
            print(f"A candidate: {A_candidate} (octal: {oct(A_candidate)})")
            print(f"Output so far: {output}")

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        A = int(lines[0].split(":")[1].strip())
        B = int(lines[1].split(":")[1].strip())
        C = int(lines[2].split(":")[1].strip())
        program = list(map(int, lines[4].split(":")[1].strip().split(",")))
        #registers = {'A': A, 'B': B, 'C': C}
        #output = run_program(registers, program)
        #print("Output:", output)

    # Part 2
    analysis_offset_old = 0o36764  
    analysis_offset = 0o65136764  #octal offset
    correct_A = find_correct_register_A(program, analysis_offset)
    print("----------------")
    print("Correct value for register A:", correct_A)