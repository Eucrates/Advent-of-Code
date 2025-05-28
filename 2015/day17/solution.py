import sys
from itertools import product

if len(sys.argv) < 3:
    print("Usage: solution.py <input filename> <liters>")
    sys.exit(1)

file = sys.argv[1]

try:
    liters = int(sys.argv[2])
except Exception as e:
    print(e)
    sys.exit()

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

containers = []
for line in lines:
    line = line.strip("\n")
    containers.append(int(line))


containers.sort(reverse=True)

# get a list of all container combinations using binary tuples
combos = [i for i in product(range(2), repeat = len(containers))]

fitLiters = 0
minContainers = len(containers)
for combo in combos:
    tot = 0
    containersUsed = 0
    for i,used in enumerate(combo):
        if used == 1:
            tot += containers[i]
            if tot > liters:
                continue
            containersUsed += 1
    if tot == liters:
        fitLiters += 1
        if containersUsed < minContainers:
            minContainers = containersUsed


            
# redundant loop, but I couldn't figure out how to get the minimum number of containers
# before running the second set of calculations
waysToUseMin = 0

for combo in combos:
    totContainers = 0
    tot = 0
    for i,used in enumerate(combo):
        if used == 1:
            totContainers += 1
            tot += containers[i]
    if (totContainers == minContainers) and (tot == liters):
        waysToUseMin += 1



print(f"Part1 = {fitLiters}")
print(f"Part2 = {waysToUseMin}")





