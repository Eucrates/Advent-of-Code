import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

directions = []
for line in lines:
    line = line.strip("\n")
    directions.append((line[0],int(line[1:])))

dial = 50
password = 0
passthru = 0

for d in directions:
    if d[0] == 'R':
        for i in range(d[1]):
            dial += 1
            dial %= 100
            if dial == 0:
                passthru += 1
    else:
        for i in range(d[1]):
            dial -= 1
            dial %= 100
            if dial == 0:
                passthru += 1
    if dial == 0:
        password += 1

print(f"Part1: {password}")
print(f"Part2: {passthru}")
