import sys

if len(sys.argv) < 2:
    #print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

instructions = []
for line in lines:
    line = line.strip("\n")
    instructions.append(int(line))

instructions2 = []  #copy instruction set; copies of lists are handled weird in memory
for i in instructions:
    instructions2.append(i)

part1 = 0
ptr = 0
while True:
    try:
        currinst = ptr
        ptr += instructions[ptr]
        instructions[currinst] += 1
        part1 += 1
    except Exception as e:
        print(e)
        break

print(f"Part 1: {part1}")


part2 = 0
ptr = 0
while True:
    try:
        currinst = ptr
        ptr += instructions2[ptr]
        if instructions2[currinst] >= 3:
            instructions2[currinst] -= 1
        else:
            instructions2[currinst] += 1
        part2 += 1
    except Exception as e:
        print(e)
        break

print(f"Part 2: {part2}")
