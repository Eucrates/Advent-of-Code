import sys
import numpy as np

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def printGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col],end="")
        print()
    
    print()

r = 6
c = 50

grid = [[' ' for _ in range(c)] for _ in range(r)] 

#grid = [['.'] * c] * r

#for row in range(2):
#    for col in range(3):
#        grid[row][col] = '#'
#printGrid(grid)

#This left me with 
# ###....
# ###....
# ###....
# instead of 
# ###....
# ###....
# .......

# Google AI:
#This behavior typically occurs when the inner lists within a 2D array are actually references to the same list object, rather than independent list objects. This often happens when initializing a 2D array using multiplication with a list, like my_array = [[0]] * 3. In this case, my_array becomes [[0], [0], [0]], but all three inner lists are the exact same list in memory. Modifying an element in one inner list will therefore be reflected in all other inner lists because they are all pointing to the same underlying object.



instructions = []
for line in lines:
    line = line.strip("\n")
    # do something
    instruction = line.split()
    if instruction[0] == 'rect':
        A,B = instruction[1].split('x')
        A = int(A)
        B = int(B)
        for row in range(B):
            for col in range(A):
                grid[row][col] = "#"
    else: # instruction[0] = rotate
        if instruction[1] == "row":
            A = int(instruction[2].split('=')[1])
            B = int(instruction[4])
            row = grid[A]
            newRow = ['-'] * len(row)
            for i in range(len(row)):
                newRow[(i+B)%len(row)] = row[i]
            grid[A] = newRow
        else: # instruction[1] == "column"
            A = int(instruction[2].split('=')[1])
            B = int(instruction[4])
            col = ['-'] * len(grid)
            newCol = ['-'] * len(grid)
            for row in range(len(grid)):
                col[row] = grid[row][A]
            for i in range(len(col)):
                newCol[(i+B)%len(col)] = col[i]
            for i in range(len(grid)):
                grid[i][A] = newCol[i]
on = 0
for row in grid:
    for elem in row:
        if elem == "#":
            on += 1

print (f"Part 1: {on}")
print (f"Part 2: ")
printGrid(grid)

