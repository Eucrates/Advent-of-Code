import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def calculate(states,inp):
    pos = 0
    relative_base = 0
    output = []

    while True:
        inst = str(states[pos]).rjust(5,"0")
        op = int(inst[-2:])
        params = inst[:-2][::-1]
        if op == 99:
            #print("End program")
            return output

        def get_param_address(idx):
            mode = params[idx]
            param_val = states[pos+1+idx]
            if mode == "0":
                ret = param_val
            elif mode == "1":
                ret =  pos + 1 + idx
            elif mode == "2":
                ret = relative_base + param_val

            while ret + 1> len(states):
                states.append(0)

            return ret

        if op in (1, 2, 5, 6, 7, 8):
            operand1 = states[get_param_address(0)]
            operand2 = states[get_param_address(1)]
            location = get_param_address(2)

            if op == 1:
                states[location] = operand1 + operand2
                pos += 4
            elif op == 2:
                val = operand1*operand2
                states[location] = operand1 * operand2
                pos += 4
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
            location = get_param_address(0)
            states[location] = inp
            pos += 2
        elif op == 4:
            location = get_param_address(0)
            out = states[location]
            print("Out:",out)
            output.append(out)
            if out != 0:
                print("Fail")
            pos += 2
        elif op == 9:
            offset = states[get_param_address(0)]
            relative_base += offset
            pos += 2
        else:

            print("Unknown state:",op, params)
            return ([0,0])
    return states


for line in lines:
    line = line.strip("\n")
    states = line.split(",")

    orig_states = [int(x) for x in states]
    

states = [x for x in orig_states]
part1 = calculate(states,1)[0]
print(f"Part 1: {part1}")
states = [x for x in orig_states]
part2 = calculate(states,2)[0]
print(f"Part 2: {part2}")


