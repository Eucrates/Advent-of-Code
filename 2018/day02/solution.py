import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

chars = set()
_2s = 0
_3s = 0
for line in lines:
    _2 = 0
    _3 = 0
    line = line.strip("\n")
    for c in line:
        chars.add(c)
    for char in chars:
        if line.count(char) == 2:
            _2 = 1
        if line.count(char) == 3:
            _3 = 1
    # do something
    # print(line, chars, _2s, _3s)
    _2s += _2
    _3s += _3
print(f"Part 1: {_2s * _3s}")


i = 0
j = 0
while i < len(lines) - 1:

    j = 0 
    while j < len(lines) - 1:
        j += 1
        diffs = 0
        line1 = lines[i].strip("\n")
        line2 = lines[j].strip("\n")
        for k in range(len(line1)):
            if line1[k] == line2[k]:
                continue
            else:
                diffs += 1
        if diffs == 1:
            break
    if diffs == 1:
        break
    i += 1
    
part2 = ''
for i in range(len(line1)):
    if line1[i] != line2[i]:
        part2 += line1[:i]
        part2 += line2[i+1:]
        break
print(f"Part 2: {part2}")

