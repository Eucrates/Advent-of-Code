import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def Part1():

    coord = [1,1]
    code = ''
    for line in lines:
        line = line.strip("\n")
        for c in line:
            match c:
                case "U":
                    if coord[0] > 0:
                        coord[0] -= 1
                case "D":
                    if coord[0] < 2:
                        coord[0] += 1
                case "L":
                    if coord[1] > 0:
                        coord[1] -= 1
                case "R":
                    if coord[1] < 2:
                        coord[1] += 1
        match coord:
            case [0,0]:
                num = '1'
            case [0,1]:
                num = '2'
            case [0,2]:
                num = '3'
            case [1,0]:
                num = '4'
            case [1,1]:
                num = '5'
            case [1,2]:
                num = '6'
            case [2,0]:
                num = '7'
            case [2,1]:
                num = '8'
            case [2,2]:
                num = '9'
        code += num
    return code


def Part2():

    coord = [2,0]
    code = ''

    for line in lines:
        line = line.strip("\n")

        for c in line:
            match coord:
                case [2,0]:         #5
                    if c == "R":
                        coord[1] += 1
                case [1,1]:         #2
                    if c == "R":
                        coord[1] += 1
                    if c == "D":
                        coord[0] += 1
                case [2,1]:         #6
                    if c == "U":
                        coord[0] -= 1
                    if c == "D":
                        coord[0] += 1
                    if c == "L":
                        coord[1] -= 1
                    if c == "R":
                        coord[1] += 1
                case [3,1]:         #A
                    if c == "U":
                        coord[0] -= 1
                    if c == "R":
                        coord[1] += 1
                case [0,2]:         #1
                    if c == "D":
                        coord[0] += 1
                case [1,2]:         #3
                    if c == "D":
                        coord[0] += 1
                    if c == "U":
                        coord[0] -= 1
                    if c == "L":
                        coord[1] -= 1
                    if c == "R":
                        coord[1] += 1
                case [2,2]:         #7
                    if c == "U":
                        coord[0] -= 1
                    if c == "D":
                        coord[0] += 1
                    if c == "L":
                        coord[1] -= 1
                    if c == "R":
                        coord[1] += 1
                case [3,2]:         #B
                    if c == "U":
                        coord[0] -= 1
                    if c == "D":
                        coord[0] += 1
                    if c == "L":
                        coord[1] -= 1
                    if c == "R":
                        coord[1] += 1
                case [4,2]:         #D
                    if c == "U":
                        coord[0] -= 1
                case [1,3]:         #4
                    if c == "L":
                        coord[1] -= 1
                    if c == "D":
                        coord[0] += 1
                case [2,3]:         #8
                    if c == "U":
                        coord[0] -= 1
                    if c == "D":
                        coord[0] += 1
                    if c == "L":
                        coord[1] -= 1
                    if c == "R":
                        coord[1] += 1
                case [3,3]:         #C  
                    if c == "U":
                        coord[0] -= 1
                    if c == "L":
                        coord[1] -= 1
                case [2,4]:         #9
                    if c == "L":
                        coord[1] -= 1
        match coord:
            case [0,2]:
                num = '1'
            case [1,1]:
                num = '2'
            case [1,2]:
                num = '3'
            case [1,3]:
                num = '4'
            case [2,0]:
                num = '5'
            case [2,1]:
                num = '6'
            case [2,2]:
                num = '7'
            case [2,3]:
                num = '8'
            case [2,4]:
                num = '9'
            case [3,1]:
                num = 'A'
            case [3,2]:
                num = 'B'
            case [3,3]:
                num = 'C'
            case [4,2]:
                num = 'D'
        code += num
    return code

print(f"Part 1: {Part1()}")
print(f"Part 1: {Part2()}")
