import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


# dictionary of coordinates
grid = {}

# dictionary of area of sections
sections = {}

for line in lines:
    line = line.strip("\n")
    section = int(line.split("#")[1].split(" @ ")[0])
    dfroml = int(line.split(" @ ")[1].split(",")[0])
    dfromt = int(line.split(" @ ")[1].split(",")[1].split(":")[0])
    width = int(line.split(": ")[1].split("x")[0])
    height = int(line.split(": ")[1].split("x")[1])
     
    sections[section] = width * height

 #   print (section, dfroml, dfromt, width, height)

    # 0,0 = X .
    #       . .

    # 0,1 = . X
    #       . .

    # 1,0 = . .
    #       X .

    # 1,1 = . .
    #       X .

    for c in range(dfroml+width):
        for r in range(dfromt+height):
            if (r,c) not in grid.keys():       # if the coordinate is not in the dictionary
                if r < dfromt or c < dfroml:   # and coordinate in margin of section
                    grid[(r,c)] = "."          # insert empty coordinate
                else:
                    grid[(r,c)] = section      # else, if coord not in dictionary, coordinate = section 
            else:                              # if coord in dictionary
                if r < dfromt or c < dfroml:   # and in margin, continue
                    continue
                else:
                    if grid[(r,c)] == ".":     # if cooridinte is empty,
                        grid[(r,c)] = section  # coordinate = section
                    else:                      # esle coordinate is X (multiple sections clamied)
                        grid[(r,c)] = "X"


part1 = 0
counters = [0] * (len(lines)+1)
for key in grid.keys():
#    print(key,grid[key])
    if grid[key] == "X":
        part1 += 1
    else:
        if grid[key] == ".":
            continue
        else:
            counters[grid[key]] += 1 # add 1 to counter array at position section

for key in sections.keys():    # check for counter that has same area as section
    if sections[key] == counters[key]:
        part2 = key
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

