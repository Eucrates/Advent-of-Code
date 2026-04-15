import sys
import operator

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

ops = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne
        }

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

registers = {}
max_register = ['',0]
for line in lines:
    line = line.strip("\n")
    instruction = line.split()
    register = instruction[0]
    incdec = instruction[1]
    offset = int(instruction[2])
    conditional_register = instruction[4]
    op = instruction[5]
    threshold = int(instruction[6])
    if register not in registers.keys():
        registers[register] = 0
    if conditional_register not in registers.keys():
        registers[conditional_register] = 0
    if ops[op](registers[conditional_register], float(threshold)):
        if incdec == "inc":
            registers[register] = registers[register] + offset
        else:
            registers[register] = registers[register] - offset
    if registers[register] > max_register[1]:
        max_register = [register, registers[register]]

print(f"Part 1: {max(registers.values())}")
print(f"Part 2: {max_register[1]}")

