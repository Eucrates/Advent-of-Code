import sys
# grid calculation from MUY Belgium's anser here
# https://stackoverflow.com/questions/11373122/best-way-to-store-a-triangular-hexagonal-grid-in-python
# distance calculations from
# https://www.redblobgames.com/grids/hexagons/#distances

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n").split(",")


    steps = 0
    coords = [0,0,0]
    maxSteps = 0
    for i, direction in enumerate(line):
        match direction:
            case "n":
                coords[1] += 1
            case "s":
                coords[1] -= 1
            case "ne":
                coords[0] += 1
            case "se":
                coords[0] += 1
                coords[1] -= 1
            case "nw":
                coords[0] -= 1
                coords[1] += 1
            case "sw":
                coords[0] -= 1

        coords[2] = -coords[0] - coords[1]
        maxSteps = max(maxSteps, max(abs(coords[0]), abs(coords[1]), abs(coords[2])))
    distance = max(abs(coords[0]), abs(coords[1]), abs(coords[2]))
    print(f"Part 1: {distance}")
    print(f"Part 2: {maxSteps}")

