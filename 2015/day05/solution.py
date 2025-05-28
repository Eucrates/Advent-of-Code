import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def checkVowels(line):

    vowels = 0
    for c in line:
        if c in "aeiou":
            vowels += 1
            if vowels >= 3:
                return True

    return False

def checkDoubles(line):
    i = 0
    while i < len(line) - 1:
        if line[i] == line[i+1]:
            return True
        i += 1

    return False

def excluded(line):
    
    excluded = ["ab", "cd", "pq", "xy"]

    for sub in excluded:
        if sub in line:
            return True

    return False

def checkDoublePair(line):

    for i in range(len(line)-1):
        if line[i]+line[i+1] in line[i+2:]:
            return True

    return False

def checkRepeatWithSpace(line):

    for i in range(len(line)-2):
        if line[i] == line [i+2]:
            return True

    return False


part1Tot = 0
for line in lines:
    line = line.strip("\n")

    nice = False

    if not checkVowels(line):
        continue

    if not checkDoubles(line):
        continue

    if excluded(line):
        continue
    
    part1Tot += 1


part2Tot = 0
for line in lines:
    line = line.strip("\n")
    
    nice = False

    if not checkDoublePair(line):
        continue

    if not checkRepeatWithSpace(line):
        continue

    part2Tot += 1

print("Part1 total nice strings:", part1Tot)
print("Part2 total nice strings:", part2Tot)



        


