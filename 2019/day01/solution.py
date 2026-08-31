# Advent of code 2019 day 1
import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

tot = 0
fuelfueltot = 0
for line in lines:
    line = line.strip("\n")
    mass = int(line)
    fuelfuel = mass
    fuel = mass // 3 - 2
    tot += fuel
    fuelfuel = fuel
    while fuel >= 0:
        fuel = (fuel // 3 - 2)
        if fuel < 0: break
        fuelfuel += fuel
          
    fuelfueltot += fuelfuel

print(f"Part 1: {tot}")
print(f"Part 2: {fuelfueltot}")
    
