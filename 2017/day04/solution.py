import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def checkanagram(line):                 # sort each word and compare; if one equals another, return 0                              
    while len(line) > 0:                # else return 1 for valid passphrase
        w1 = line.pop()
        w1 = ''.join(sorted(w1))
        for w2 in line:
            w2 = ''.join(sorted(w2))
            if w1 == w2:
                return 0
    return 1

part1 = 0
part2 = 0
for line in lines:
    line = line.strip("\n")
    phrases = line.split()
    valid = True
    while len(phrases) > 0:              # pop phrase from the end, compare to each other phrase; if there's a match
        phrase = phrases.pop()           # set valid to false and break loop
        if phrase in phrases:
            valid = False
            break
    if valid:                            # if the phrase is valid, add to total
        part1 += 1
    part2 += checkanagram(line.split())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
