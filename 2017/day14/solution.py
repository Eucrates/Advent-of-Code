import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

# from day 10
def twister(string,sequence,pos,skip):

    for length in sequence:
        indices = [index % len(string) for index in range(pos,pos+length)]
        segment = [string[j] for j in indices]
        segment = segment[::-1]
        for j, val in enumerate(segment):
            string[(j+pos)%len(string)] = val 
        pos += length + skip
        pos = pos % len(string)
        skip += 1
    return string,pos,skip

# from day 10
def calcKnotHash(line):
    pos = 0
    skip = 0
    string = [i for i in range(256)]
    sequence = [ord(c) for c in base]
    for i in [17,31,73,47,23]:
        sequence.append(i)
    for _ in range(64):
        string,pos,skip = twister(string,sequence,pos,skip)

    denseHash = []
    for i in range(0,len(string),16):
        d = string[i:i+16]
        dense = d[0]
        for j in d[1:]:
            dense ^= j
        
        denseHash.append(dense)
    knotHash = "".join(f"{d:02x}" for d in denseHash)
    return knotHash

for line in lines:
    grid = []
    line = line.strip("\n")
    part1 = 0
    for i in range(128):
        base = line + "-" + str(i)
        base = "".join(base)

        knotHash = calcKnotHash(base)

        binKnot = "".join([format(int(c,16), '04b') for c in knotHash])

        part1 += binKnot.count('1')
        
        # pad sides with 0's to avoid edge cases
        grid.append("0" + binKnot + "0")

print(f"Part 1: {part1}")

# pad top and bottom with 0's to avoid edge cases
grid.insert(0, "0" * 130)
grid.append("0" * 130)

# turn rows into lists for indexability
for r,row in enumerate(grid):
    grid[r] = [c for c in row]

# recursive function to count all adjacent used squares
def findRegion(r,c,count,grid):

    # check top and bottom
    if grid[r-1][c] == '1':
        grid[r-1][c] = count
        grid = findRegion(r-1,c,count,grid)
    if grid[r+1][c] == '1':
        grid[r+1][c] = count
        grid = findRegion(r+1,c,count,grid)
    
    # check sides
    if grid[r][c-1] == '1':
        grid[r][c-1] = count
        grid = findRegion(r,c-1,count, grid)
    if grid[r][c+1] == '1':
        grid[r][c+1] = count
        grid = findRegion(r,c+1,count,grid)

    return grid

# I used Claude to help troubleshoot here; I had an off by 1 error
# in my enumerations; by adding start=1 the indices are correct
# when I send r and c to the findRegion function
count = 0
for r, row in enumerate(grid[1:-1], start=1):
    for c,col in enumerate(row[1:-1], start=1):
        if grid[r][c] == '1':
            grid[r][c] = count
            grid = findRegion(r,c,count,grid)
            count +=  1

print(f"Part 2: {count}")



