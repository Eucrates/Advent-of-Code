import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")
    part1 = 0
    part2 = 0
    for i,n in enumerate(line):
        diff = (i + 1) % len(line)
        if int(line[i]) == int(line[diff]):
            part1 += int(n)
        diff = (len(line) // 2 + i) % len(line)
        if int(line[i]) == int(line[diff]):
            part2 += int(n)
                
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
