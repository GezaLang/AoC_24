import sys
import z3
import re
import pyperclip as pc

"""
z3: https://z3prover.github.io/api/html/z3.z3.html
inspired by: https://github.com/jonathanpaulson
"""

def pr(s):
    print(s)
    pc.copy(s)

# Parse integers from a string
def ints(s):
    return [int(x) for x in re.findall(r'\d+', s)]

# Solve for the minimum tokens to win a prize on a machine
def solve(ax, ay, bx, by, px, py, part2):
    """
    Solve the claw machine problem using Z3 for Part 2.
    """
    px += 0 if not part2 else 10000000000000
    py += 0 if not part2 else 10000000000000

    t1 = z3.Int('t1')
    t2 = z3.Int('t2')
    solver = z3.Solver()
    solver.add(t1 > 0, t2 > 0)
    solver.add(t1 * ax + t2 * bx == px)
    solver.add(t1 * ay + t2 * by == py)

    if solver.check() == z3.sat:
        model = solver.model()
        return model.eval(3 * t1 + t2).as_long()
    else:
        return 0

if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
    data = open(infile).read().strip()

    p2 = 0
    machines = data.split("\n\n")
    
    for machine in machines:
        ax, ay, bx, by, px, py = ints(machine)
        p2 += solve(ax, ay, bx, by, px, py, part2=True)

    print(p2)