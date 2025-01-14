import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

tot = 0
mem = 0
enc = 0
for line in lines:
    line = line.strip("\n")
    # do something
    # print(line)
    i = 0
    m = 0
    e = 0
    while i < len(line):
        if line[i] == "\"":
            e += 2
        if line[i] == "\\":
            e += 2
            if i < len(line) - 1:
                if line[i+1] == "x":
                    e += 2 
                    i += 3
                    m += 1
                elif line[i+1] == "\\" or line[i+1] == "\"":
                    e += 1
                    i += 1
                    m += 1
        else:
            m += 1
        
        e += 1
        i += 1
    m -= 2          # don't count first and last quotation marks   
    mem += m
    tot += len(line)
    enc = enc + e



print("Part1: Total - memory:",tot - mem)
print("Part2: Encoded - total:", enc - tot)
