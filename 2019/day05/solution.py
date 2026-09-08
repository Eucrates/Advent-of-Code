import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def calculate(states,i,j):

    pos = 0
    while pos < len(states):
        inst = str(states[pos]).rjust(5,"0")
        op = int(inst[-2:])
        params = inst[:-2][::-1]
        if op == 99:
            #print("End program")
            break
        if op == 1 or op == 2 or (op > 4 and op <= 8):
            if params[0] == "0":
                operand1 = states[states[pos+1]]
            else:
                operand1 = states[pos+1]
            if params[1] == "0":
                operand2 = states[states[pos+2]]
            else:
                operand2 = states[pos+2]
            location = states[pos+3]
            if op == 1:
                val = operand1+operand2
                pos += 4
                states[location] = val
            elif op == 2:
                val = operand1*operand2
                pos += 4
                states[location] = val
            elif op == 5:
                if operand1 != 0:
                    pos = operand2
                else:
                    pos += 3
            elif op == 6:
                if operand1 == 0:
                    pos = operand2
                else:
                    pos += 3
            elif op == 7:
                if operand1 < operand2:
                    states[location] = 1
                else:
                    states[location] = 0
                pos += 4
            elif op == 8:
                if operand1 == operand2:
                    states[location] = 1
                else:
                    states[location] = 0
                pos += 4
        elif op == 3:
            inp = int(input("Input: "))
            location = states[pos+1]
            states[location] = inp
            pos += 2
        elif op == 4:
            if params[0] == "0":
                location = states[pos+1]
                out = states[location]
            else:
                out = states[pos+1]

            print("Out:",out)
            if out != 0:
                print("Fail")
            pos += 2
        else:

            print("Unknown state:",op, params)
            return ([0,0])
    return states


for line in lines:
    line = line.strip("\n")
    states = line.split(",")

    states = [int(x) for x in states]

#orig_states = [x for x in states]
states = calculate(states,12,2)


