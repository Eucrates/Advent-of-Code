import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

registers = {}
instructions = []
for line in lines:
    instruction = line.strip("\n").split(" ")
    # instruction 2 could be int or register
    # instruction 1 could be an int if instruction is jgz
    for i,inst in enumerate(instruction): 
        if inst.isdigit() or inst.startswith('-'):
            instruction[i] = int(instruction[i])
    # set initial registers to 0
    if type(instruction[1]) != int and instruction[1] not in registers.keys():
        registers[instruction[1]] = 0
    instructions.append(instruction)

#  set registers for part 2: cannot just copy dictionaries;
#  it will point to the same object
a = {}
b = {}
for key in registers.keys():
    a[key] = registers[key]
    b[key] = registers[key]

registers["instruction"] = 0
registers["sent"] = 0
registers["term"] = False

a["instruction"] = 0
a["snd"] = []
a["sent"] = 0
a["p"] = 0
a["term"] = False

b["instruction"] = 0
b["snd"] = []
b["sent"] = 0
b["p"] = 1
b["term"] = False

def process(regs,q1,q2):
    i = regs["instruction"]
    if len(instructions[i]) == 3:
        x,y = instructions[i][1],instructions[i][2]
        if type(y) != int:
            y = regs[y]
    else:
        x = instructions[i][1]
        y = ''
    match instructions[i][0]:
        case "snd":
            if type(x) != int:
                q2.append(regs[x])
                regs["last"] = regs[x]
            else:
                q2.append(x)
                regs["last"] = x
            regs["sent"] += 1
        case "set":
            regs[x] = y
        case "add":
            regs[x] += y
        case "mul":
            regs[x] *= y
        case "mod":
            regs[x] %= y
        case "rcv":
            if len(q1) > 0:
                regs[x] = q1.pop(0)
            else:
                i -= 1
            if len(q1) == 0:
                regs["term"] = True
            else:
                regs["term"] = False
        case "jgz":
            if type(x) != int:
                x = regs[x]
            if x > 0:
                i += y - 1 
    i += 1
    regs["instruction"] = i
    return regs,q1,q2


# Part 1
while 0 <= registers["instruction"] < len(instructions):
    registers,_,_ = process(registers,[],[])
    if registers["term"]:
        break

print(f"Part 1: {registers["last"]}")

# Part 2
while not a["term"] or not b["term"]:

    a,a["snd"],b["snd"] = process(a,a["snd"],b["snd"])
    b,b["snd"],a["snd"] = process(b,b["snd"],a["snd"])
    if 0 > a["instruction"] >= len(instructions):
        a["term"] = True
    if 0 > b["instruction"] >= len(instructions):
        b["term"] = True

print(f"Part 2: {b["sent"]}")


