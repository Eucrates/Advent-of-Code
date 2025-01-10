import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1]


for line in lines:
    line = line.strip("\n")
    
    house = [0,0]
    santaHouse = [0,0]
    roboHouse = [0,0]
    year1 = set()
    year1.add((house[0],house[1]))

    santaVisit = set() 
    roboVisit = set()
    santaVisit.add((house[0],house[1]))
    roboVisit.add((house[0],house[1]))
    # Part 1
    for i,c in enumerate(line):
        match c:
            case "^":
                house[0] += 1
                year1.add((house[0],house[1]))
            case ">":
                house[1] += 1
                year1.add((house[0],house[1]))
            case "v":
                house[0] -= 1
                year1.add((house[0],house[1]))
            case "<":
                house[1] -=1
                year1.add((house[0],house[1]))
            case _:
                print("unexpected token:", c)
                sys.exit(1)

# Part2
    i = 0
    while i < len(line)-1:
        match line[i]:
            case "^":
                santaHouse[0] += 1
                santaVisit.add((santaHouse[0],santaHouse[1]))
            case ">":
                santaHouse[1] += 1
                santaVisit.add((santaHouse[0],santaHouse[1]))
            case "v":
                santaHouse[0] -= 1
                santaVisit.add((santaHouse[0],santaHouse[1]))
            case "<":
                santaHouse[1] -=1
                santaVisit.add((santaHouse[0],santaHouse[1]))
            case _:
                print("unexpected token:", c)
                sys.exit(1)

        match line[i+1]:
            case "^":
                roboHouse[0] += 1
                roboVisit.add((roboHouse[0],roboHouse[1]))
            case ">":
                roboHouse[1] += 1
                roboVisit.add((roboHouse[0],roboHouse[1]))
            case "v":
                roboHouse[0] -= 1
                roboVisit.add((roboHouse[0],roboHouse[1]))
            case "<":
                roboHouse[1] -=1
                roboVisit.add((roboHouse[0],roboHouse[1]))
            case _:
                print("unexpected token:", c)
                sys.exit(1)
        i += 2
        

    print("Houses with at least 1 present year 1:", len(year1))
    santaVisit.update(roboVisit)
    print("Houses with at least 1 present year 2:", len(santaVisit))
 
    


