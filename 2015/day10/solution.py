import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def expand(line):
    
    l = ""
    numNums = 1
    i = 0

    if len(line) == 1:
        return str(numNums) + line[0]

    for i,c in enumerate(line):
        if i < len(line)-1:
            if line[i]==line[i+1]:
                numNums += 1
            else:
                l += str(numNums) + line[i]
                numNums = 1
        else:
            l += str(numNums) + line[i]
        i += 1
    return l

line = lines[0].strip("\n")        # remove newline character
for i in range (40):
    line = expand(line)
print("Part1: len 40 times:", len(line))

for i in range(10):
    line = expand(line)
print("Part2: len 50 times:", len(line))
