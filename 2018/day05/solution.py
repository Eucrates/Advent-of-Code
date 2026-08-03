import sys

# Very slow

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    line = f.readline()
    line = line.strip()

def react(line):
    i = 0
    length = len(line)
    while i < length - 1:
        if line[i].isupper() and line[i+1].islower() and line[i+1].upper() == line[i]:
            line = line[:i] + line[i+1+1:]
            i = 0
        elif line[i].islower() and line[i+1].isupper() and line[i+1].lower() == line[i]:
            line = line[:i] + line[i+1+1:]
            i = 0
        else:
            i += 1
        length = len(line)

    return length

print(f"Part 1: {react(line)}")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

part2 = len(line)
for c in alphabet:
    polymer = line.replace(c,'').replace(c.lower(),'')
    length = react(polymer)
    if length < part2:
        part2 = length

print(f"Part 2: {part2}")
