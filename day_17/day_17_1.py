def run_program(registers, program):
    """
    Simulates the 3-bit computer program.
    """
    A, B, C = registers['A'], registers['B'], registers['C']
    instruction_pointer = 0
    output = []
    def oper(operand):
        if operand in [0, 1, 2, 3]:
            return operand  #values
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

    # Main simulation loop
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv
            denominator = 2 ** oper(operand)
            A = A // denominator
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = oper(operand) % 8
        elif opcode == 3: # jnz
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(oper(operand) % 8)
        elif opcode == 6:  # bdv
            denominator = 2 ** oper(operand)
            B = A // denominator
        elif opcode == 7:  # cdv
            denominator = 2 ** oper(operand)
            C = A // denominator
        else:
            raise ValueError(f"Unknown opcode {opcode} encountered!")
        instruction_pointer += 2  
    return ",".join(map(str, output))

if __name__ == "__main__":
     with open("input.txt") as f:
        lines = f.readlines()
        A = int(lines[0].split(":")[1].strip())
        B = int(lines[1].split(":")[1].strip())
        C = int(lines[2].split(":")[1].strip())
        program = list(map(int, lines[4].split(":")[1].strip().split(",")))
        registers = {'A': A, 'B': B, 'C': C}
        output = run_program(registers, program)
        print("Output:", output)