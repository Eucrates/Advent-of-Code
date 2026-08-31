import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def calculate(states,i,j):

    states[1] = i
    states[2] = j
    pos = 0
    while pos < len(states):
        op = states[pos]
        if op == 99:
            #print("End program")
            break
        operand1 = states[states[pos+1]]
        operand2 = states[states[pos+2]]
        location = states[pos+3]
        if op == 1:
            val = operand1+operand2
        elif op == 2:
            val = operand1*operand2
        else:
            print("Unknown state")
            return ([0,0])
        states[location] = val
        pos += 4
    return states


for line in lines:
    line = line.strip("\n")
    # do something
    states = line.split(",")

    states = [int(x) for x in states]

orig_states = [x for x in states]
states = calculate(states,12,2)

print(f"Part 1: {states[0]}")

for i in range(100):
    for j in range(100):
        states = orig_states.copy()
        states = calculate(states,i,j)

        if states[0] == 19690720:
            print(f"Part 2: {100 * i + j}")
            exit(0)
