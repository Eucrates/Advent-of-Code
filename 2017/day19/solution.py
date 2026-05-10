import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

path = []
for line in lines:
    line = line.strip("\n")
    # do something
    row = []
    for c in line:
        row.append(c)
    row.insert(0,' ')
    row.append(' ')
    path.append(row)

for i in range(len(path[0])):
    if path[0][i] == "|":
        break
buff = [' '] * len(path[0])
path.insert(0,buff)
path.append(buff)

#for row in path: print(row)

#        row, col, dir
coord =  [1,  i,   "d"]
letters = []
steps = 0
while True:

    c = path[coord[0]][coord[1]]
    #print(coord,c)
    match c:
        case "|":
            pass
        case "-":
            pass
        case "+":
            match coord[2]:
                case "u":
                    # look left and right
                    if path[coord[0]][coord[1]-1] == " ":
                        coord[2] = "r"
                    else:
                        coord[2] = "l"
                    # look left and right
                case "d":
                    if path[coord[0]][coord[1]-1] == " ":
                        coord[2] = "r"
                    else:
                        coord[2] = "l"
                case "l":
                    # look up and down
                    if path[coord[0]-1][coord[1]] == " ":
                        coord[2] = "d"
                    else:
                        coord[2] = "u"
                case "r":
                    # look up and down
                    if path[coord[0]-1][coord[1]] == " ":
                        coord[2] = "d"
                    else:
                        coord[2] = "u"
        case " ":
            break
        case _:
            letters.append(c)
    match (coord[2]):
        case "u":
            coord[0] -= 1
            steps += 1
        case "d":
            coord[0] += 1
            steps += 1
        case "l":
            coord[1] -= 1
            steps += 1
        case "r":
            coord[1] += 1
            steps += 1
                           


print(f"Part 1: {''.join(letters)}")
print(f"Part 2: {steps}")
