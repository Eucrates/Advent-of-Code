import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


rows = 1000
cols = 1000

def part1(lines):

    grid = [[-1 for _ in range(cols)] for _ in range(rows)]

    for line in lines:
        line = line.strip("\n")
    
        if "on" in line:
            instruction = "turn on"
        elif "off" in line:
            instruction = "turn off"
        elif "toggle" in line:
            instruction = "toggle"
        
        corner1 = line.split(instruction + " " )[1].split(" ")[0]
        corner2 = line.split(" ")[-1]

        row1 = int(corner1.split(",")[0])
        col1 = int(corner1.split(",")[1])

        row2 = int(corner2.split(",")[0])
        col2 = int(corner2.split(",")[1])
    
        r1 = min(row1,row2)
        r2 = max(row1,row2)
        c1 = min(col1,col2)
        c2 = max(col1,col2)

        match instruction:
            case "turn on":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] = 1
            case "turn off":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] = -1
            case "toggle":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] *= -1
            case _:
                print("unexpected instruction:", instruction)
                sys.exit(1)

    
    on = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                on += 1

    print("Part1 lights on: ", on)

def part2(lines):

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in lines:
        line = line.strip("\n")
    
        if "on" in line:
            instruction = "turn on"
        elif "off" in line:
            instruction = "turn off"
        elif "toggle" in line:
            instruction = "toggle"
        
        corner1 = line.split(instruction + " " )[1].split(" ")[0]
        corner2 = line.split(" ")[-1]

        row1 = int(corner1.split(",")[0])
        col1 = int(corner1.split(",")[1])

        row2 = int(corner2.split(",")[0])
        col2 = int(corner2.split(",")[1])
    
        r1 = min(row1,row2)
        r2 = max(row1,row2)
        c1 = min(col1,col2)
        c2 = max(col1,col2)

        match instruction:
            case "turn on":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] += 1
            case "turn off":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] -= 1
                        if grid[i][j] <= 0: grid[i][j] = 0
            case "toggle":
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        grid[i][j] += 2 
            case _:
                print("unexpected instruction:", instruction)
                sys.exit(1)


    brightness = 0
    for i in range(rows):
        for j in range(cols):
            brightness += grid[i][j] 

    print("Part2 lights on: ", brightness)


part1(lines)
part2(lines)
