import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <input filename> <gridsize> <steps>")
    sys.exit(1)

file = sys.argv[1]
gridsize = int(sys.argv[2])
steps = int(sys.argv[3])

with open (file) as f:
    lines = f.readlines()[:-1]   # assumes input ends in newline

def initializeGrid():

    # circle the grid with off lights to avoid edge cases
    linearGrid = []
    for i in range(gridsize + 2):    # begin grid with row of .
        linearGrid.append(".")      

    for line in lines:
        line = line.strip("\n")
        linearGrid.append(".")       # begin row with .
        for state in line:
            linearGrid.append(state)
        linearGrid.append(".")       # end row with .

    for i in range(gridsize + 2):
        linearGrid.append(".")       # end grid with row of .

    return linearGrid

def printGrid(grid):
    
    for r in range(1,gridsize + 1):
        for c in range(1,gridsize + 1):
            lightIndex = (c + gridsize + 2) + ((gridsize + 2)*(r-1))
            state = grid[lightIndex]
            print(state,end="")
        print()
    print()

def changeState(state1):
    state2 = ["."] * ((gridsize + 2) ** 2)
    for r in range(1, gridsize + 1):
        for c in range(1,gridsize + 1):
            lightIndex = (c + gridsize + 2) + ((gridsize + 2)*(r-1))
            state = state1[lightIndex]
            _0 = state1[lightIndex - (gridsize + 3)]
            _1 = state1[lightIndex - (gridsize + 2)]
            _2 = state1[lightIndex - (gridsize + 1)]
            _3 = state1[lightIndex - 1]
            _4 = state1[lightIndex + 1]
            _5 = state1[lightIndex + (gridsize + 1)]
            _6 = state1[lightIndex + (gridsize + 2)]
            _7 = state1[lightIndex + (gridsize + 3)]
            neighborStates = [_0,_1,_2,_3,_4,_5,_6,_7]
            if state == "#":
                if neighborStates.count("#") == 2: 
                    state2[lightIndex] = "#"
                elif neighborStates.count("#") == 3:
                    state2[lightIndex] = "#"
                else:
                    state2[lightIndex] = "."
                
            if state == ".":
                if neighborStates.count("#") == 3:
                    state2[lightIndex] = "#"
    return state2

def turnOnCorners(state1):
    state2 = state1
    state2[gridsize + 2 + 1] = "#"
    state2[((gridsize + 2) * 2) - 2] = "#"
    state2[len(linearGrid2) - (gridsize  + 4) - gridsize + 1] = "#"
    state2[len(linearGrid2) - (gridsize + 4)] = "#"
    
    return state2

# because of the way python treats arrays in memory, I had to initialize the two grids separately
linearGrid1 = initializeGrid()
linearGrid2 = initializeGrid()

linearGrid2 = turnOnCorners(linearGrid2)

for i in range(steps):
    linearGrid1 = changeState(linearGrid1)
    linearGrid2 = changeState(linearGrid2)
    linearGrid2 = turnOnCorners(linearGrid2)
    
print(f"Part1: {linearGrid1.count('#')}")
print(f"Part2: {linearGrid2.count('#')}")


