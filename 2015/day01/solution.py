import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(0)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1]

for line in lines:
    basement = 0
    character = 1
    line = line.strip("\n")
    floor = 0
    for c in line:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            print("Error, unexpected token")
            sys.exit(1)
        if basement == 0:
            if floor == -1:
                basement = character
            else:
                character += 1
           
    print(line, "\nFloor:", floor)
    print("Basement first entered at position", basement)
