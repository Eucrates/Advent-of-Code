import sys
import itertools

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


names = set()
d = {}
for line in lines:
    line = line.strip("\n")

    name1 = line.split(" ")[0]
    name2 = line.split(" ")[-1][:-1]
    if " gain " in line:
        points = int(line.split(" gain ")[1].split(" ")[0])
    if " lose " in line:
        points = -int(line.split(" lose ")[1].split(" ")[0])
    d[name1 + " " + name2] = points
    names.add(name1)


perms =  list(itertools.permutations(names))

totals = []
for perm in perms:
    nameList = []
    tot = 0
    for p in perm:
        nameList.append(p)
        #print(p)
    i = 0
    while i < len(nameList):
        if i == len(nameList) - 1:
            key1 = nameList[i] + " " + nameList[0]
            key2 = nameList[0] + " " + nameList[i]
        else:
            key1 = nameList[i] + " " + nameList[i+1]
            key2 = nameList[i+1] + " " + nameList[i]
       # print(i, key1, key2)
        tot += d[key1] + d[key2]
        i += 1
    totals.append(tot)

part1 = max(totals)
print("Part1:", part1)


for name in names:
    d[name + " Me"] = 0
    d["Me " + name] = 0

names.add("Me")
permsMe = list(itertools.permutations(names))
totals = []
for perm in permsMe:
    nameList = []
    tot = 0
    for p in perm:
        nameList.append(p)
    i = 0
    while i < len(nameList):
        if i == len(nameList) - 1:
            key1 = nameList[i] + " " + nameList[0]
            key2 = nameList[0] + " " + nameList[i]
        else:
            key1 = nameList[i] + " " + nameList[i+1]
            key2 = nameList[i+1] + " " + nameList[i]
        tot += d[key1] + d[key2]
        i += 1
    totals.append(tot)

print("Part2:", max(totals))
