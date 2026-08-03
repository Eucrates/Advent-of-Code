import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

part1 = 0
part2 = None

freqList = set()
freqList.add(part1)

for line in lines:
    line = line.strip("\n")
    if line[0] == '+':
        change = int(line[1:])
    else:
        change = -int(line[1:])
    part1 += change
    if part1 in freqList:
        part2 = part1
    freqList.add(part1)

print(f"Part 1: {part1}")

while True:
    for line in lines:
        line = line.strip("\n")

        if line[0] == '+':
            change = int(line[1:])
        else:
            change = -int(line[1:])
        part1 += change
        if part1 in freqList:
            print(f"Part 2: {part1}")
            exit(1)
        else:
            freqList.add(part1)



