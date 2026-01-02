import sys
from functools import cache
if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

part1 = 0

beams = set()                      # column of beam is unique in a row
for i,line in enumerate(lines):
    line = line.strip("\n")
    for j,c in enumerate(line):    
        if c == "S":
            beams.add(j)           # Starting beam column number
        elif c == "^":
            if j in beams:         # if there's a splitter and a beam above it, add 1
                part1 += 1         # add one to the number of times the beam is split
                beams.remove(j)    # beam has split, remove current beam
                beams.add(j+1)     # add beam to left and right
                beams.add(j-1)

print(f"Part 1: {part1}")

# part 2 from https://www.youtube.com/watch?v=UiV7V1dTwZ8@cache
@cache
def part2(r, c):  # recursive, memoized function that returns the number of times the row is split
    if r >= len(lines): return 1  # if row is greater than or equal to the number of lines, there are no more splitters so return 1 path

    if lines[r][c] == "." or lines[r][c] == "S":   # if no splitter, return the next row's value
        return part2(r+1, c)
    elif lines[r][c] == "^":                       # if there's a splitter, return the left and right values
        return part2(r, c-1) + part2(r,c+1)

# get position of S in first line 
start = lines[0].index("S")

print(f"Part 2: {part2(0,start)}")

