import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")
    line = line.strip()

instructions = line.split(",")

for i,instruction in enumerate(instructions):
    instructions[i] = [instruction.strip()[:1],int(instruction.strip()[1:])]


''' 0 = north
    1 = east
    2 = south
    3 = west
'''

d = 0
ns = 0
ew = 0

locations = [(0,0)]
for instruction in instructions:
    if instruction[0] == "R":
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

    match d:        # add each spot visitied to locations array
        case 0:
            for i in range(instruction[1]):
                ns += 1
                locations.append((ns,ew))
        case 1:
            for i in range(instruction[1]):
                ew += 1
                locations.append((ns,ew))
        case 2:
            for i in range(instruction[1]):
                ns -= 1
                locations.append((ns,ew))
        case 3:
            for i in range(instruction[1]):
                ew -= 1
                locations.append((ns,ew))

# final distance is the sum of the absolute values of the distance away from the origin    
print("Part 1:", abs(ns) + abs(ew))

# check each location in the array, stop when one is repeated in the remaining array
for i,location in enumerate(locations):
    if location in locations[i+1:]:
        part2 = abs(location[0]) + abs(location[1])
        break
print("Part 2:", part2)
