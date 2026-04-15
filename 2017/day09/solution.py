import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = list(line.strip("\n"))

    # strip cancelled characters
    for i,c in enumerate(line):
        if c == '!':
            line[i] = ''
            line[i+1] = ''

    part2 = 0
    for i,c in enumerate(line):
        if c == '<':
            line[i] = ''
            j = i
            while c != '>':
                if line[j] == '>': part2 -= 1
                if line[j] != '': part2 += 1    # skip empty indices
                line[j] = ''
                j += 1
                c = line[j]
            if c == '>': 
                line[j] = ''
    
    line = ''.join(line)
    openbracket = 0
    part1 = 0
    for c in line:
        if c == '{':
            openbracket += 1
        if c == '}':
            groupvalue = openbracket
            part1 += groupvalue
            openbracket -=1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

