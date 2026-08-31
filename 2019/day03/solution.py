import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

wire1 = lines[0].strip("\n")
wire1 = wire1.split(",")
wire2 = lines[1].strip("\n")
wire2 = wire2.split(",")


wire1 = [[x[0],int(x[1:])] for x in wire1]
wire2 = [[x[0],int(x[1:])] for x in wire2]

def get_path(wire):
    coord = (0,0)
    coords = {coord} # y,x
    for d in wire:
        match d[0]:
            case "U":
                for _ in range(d[1]):
                    coord = (coord[0]-1,coord[1])
                    coords.add(coord)
            case "D":
                for _ in range(d[1]):
                    coord = (coord[0]+1,coord[1])
                    coords.add(coord)
            case "L":
                for _ in range(d[1]):
                    coord = (coord[0],coord[1]-1)
                    coords.add(coord)
            case "R":
                for _ in range(d[1]):
                    coord = (coord[0],coord[1]+1)
                    coords.add(coord)
    return coords

def manhattan(coord):

    dist = abs(coord[0]-0) + abs(coord[1]-0)
    return dist

def walk_path(wire,intersection):
    coord = (0,0)
    coords = {coord} # y,x
    steps = 0
    for d in wire:
        match d[0]:
            case "U":
                for _ in range(d[1]):
                    coord = (coord[0]-1,coord[1])
                    steps += 1
                    if coord == intersection:
                        return steps
            case "D":
                for _ in range(d[1]):
                    coord = (coord[0]+1,coord[1])
                    steps += 1
                    if coord == intersection:
                        return steps
            case "L":
                for _ in range(d[1]):
                    coord = (coord[0],coord[1]-1)
                    steps += 1
                    if coord == intersection:
                        return steps
            case "R":
                for _ in range(d[1]):
                    coord = (coord[0],coord[1]+1)
                    steps += 1
                    if coord == intersection:
                        return steps

path1 = get_path(wire1)
path2 = get_path(wire2)
intersections = path1 & path2
intersections.remove((0,0))

minDist = sys.maxsize
for intersection in intersections:
    minDist = min(minDist,manhattan(intersection))

print(f"Part 1: {minDist}")

min_steps = sys.maxsize
for intersection in intersections:
    steps = walk_path(wire1,intersection) + walk_path(wire2,intersection)
    min_steps = min(min_steps, steps)

print(f"Part 2: {min_steps}")

