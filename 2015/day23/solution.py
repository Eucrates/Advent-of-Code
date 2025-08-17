import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline



instructions = []
for line in lines:
    line = line.strip("\n")
    # do something
    # print(line)

    
    if len(line.split()) == 2:
        inst, reg = line.split()
        if inst == "jmp":
            reg = int(reg)
        instructions.append([inst, reg])
    else:
        inst, reg, offset = line.split()
        offset = int(offset)
        reg = reg[:1]
        instructions.append([inst, reg, offset])

def run_code(part):
    b = 0
    if part == 1:
        a = 0
    else:
        a = 1

    i = 0
    while True:
        if i == len(instructions):
            break
#        print(i, instructions[i], a, b)
        match instructions[i][0]:
            case "hlf":
                if instructions[i][1] == "a":
                    a /= 2
                else:
                    b /= 2
            case "tpl":
                if instructions[i][1] == "a":
                    a *= 3
                else:
                    b *= 3
            case "inc":
                if instructions[i][1] == "a":
                    a += 1
                else:
                    b += 1
            case "jmp":
                i += instructions[i][1]
                continue
            case "jie":
                if instructions[i][1] == "a":
                    reg = a
                else:
                    reg = b
                if reg % 2 == 0:
                    i += instructions[i][2]
                    continue
            case "jio":
                if instructions[i][1] == "a":
                    reg = a
                else:
                    reg = b
                if reg == 1:
                    i += instructions[i][2]
                    continue
        i += 1

    print(f"Part {part}:", b)

run_code(1)
run_code(2)
