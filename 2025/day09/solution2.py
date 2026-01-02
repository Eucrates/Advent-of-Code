import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

vertices = []
maxrow = 0
maxcol = 0
for line in lines:
    line = line.strip("\n")
    col,row = [int(x) for x in line.split(",")]
    vertices.append((col,row))
    if row > maxrow: maxrow = row
    if col > maxcol: maxcol = col



part1 = 0
grid = []
for i in range(maxrow):
    grid.append(["."] * maxcol)


for v1 in range(len(vertices)):
    row = vertices[v1][1] - 1
    col = vertices[v1][0] - 1
    grid[row][col] = "#"
    for v2 in range(v1+1,len(vertices)):
        
        tot = (abs(vertices[v1][0]-vertices[v2][0])+ 1) * (abs(vertices[v1][1] - vertices[v2][1]) +1)
        if tot > part1:
            part1 = tot

        if vertices[v1][1] == vertices[v2][1]:
         
            row   = vertices[v1][1] - 1
            start = min([vertices[v1][0],vertices[v2][0]])
            end   = max([vertices[v1][0],vertices[v2][0]])
            for col in range(start,end):
                if grid[row][col] == ".":
                    grid[row][col] = "X"

        if vertices[v1][0] == vertices[v2][0]:
            col   = vertices[v1][0] - 1
            start = min([vertices[v1][1],vertices[v2][1]])
            end   = max([vertices[v1][1],vertices[v2][1]])
            for row in range(start,end):
                if grid[row][col] == ".":
                    grid[row][col] = "X"

for row in grid:
    print(row)

print(f"Part 1: {part1}")


    


