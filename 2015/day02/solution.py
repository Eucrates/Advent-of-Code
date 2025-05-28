import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(0)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1]


paper = 0
ribbon = 0
for i,line in enumerate(lines):
    line = line.split("x")
    if len(line) != 3:
        print("Line", i+1, "doesn't have three dimensions")
    for i in range(len(line)):
        line[i] = int(line[i])
    # line[0] = length
    # line[1] = width
    # line[2] = height
    side1area = line[0]*line[1]
    side2area = line[1]*line[2]
    side3area = line[2]*line[0] 
    area = 2*side1area + 2*side2area + 2*side3area
    paperslack = min(side1area,side2area,side3area)
    paper += area + paperslack
    
    side1perim = line[0]*2 + line[1]*2
    side2perim = line[1]*2 + line[2]*2
    side3perim = line[2]*2 + line[0]*2
    perim = min(side1perim, side2perim, side3perim)
    ribbonslack = line[0]*line[1]*line[2]
    ribbon += perim + ribbonslack


print ("Part1 Total Paper:\t", paper)
print ("Part2 Total Ribbon:\t", ribbon)
