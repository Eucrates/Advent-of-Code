import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]
file2 = "tickertape.txt"

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

with open (file2) as f:
    tickerItems = f.readlines()[:-1]

for i, tItem in enumerate(tickerItems):
    tickerItems[i] = tItem.split(": ")
    tickerItems[i][1] = tickerItems[i][1].strip("\n")

sueItems = []
for line in lines:
    line = line.strip("\n")
    line = line.split(",")
    sue = line[0].split(" ")[1][:-1]
    for i in range(len(line)):
        if i == 0:
            line[0] = line[0].split(": ")
            line[0] = [line[0][1],line[0][2]]
        else:
            line[i] = line[i].replace(" ","").split(":")
    sueItems.append([sue,line])


def part1(): 
    for sItem in sueItems:
        match = 0
        for tItem in tickerItems:
            if tItem[0] == sItem[1][0][0] and tItem[1] == sItem[1][0][1]:
                match += 1
            if tItem[0] == sItem[1][1][0] and tItem[1] == sItem[1][1][1]:
                match += 1
            if tItem[0] == sItem[1][2][0] and tItem[1] == sItem[1][2][1]:
                match += 1
        if match == 3:
            return(sItem[0])

def part2(): 
    for sItem in sueItems:
        match = 0
        for tItem in tickerItems:
            if tItem[0] == "trees" or tItem == "trees":
                if tItem[0] == sItem[1][0][0] and tItem[1] < sItem[1][0][1]:
                    match += 1
                if tItem[0] == sItem[1][1][0] and tItem[1] < sItem[1][1][1]:
                    match += 1
                if tItem[0] == sItem[1][2][0] and tItem[1] < sItem[1][2][1]:
                    match += 1
            if tItem[0] == "pomeranians" or tItem[0] == "goldfish":
                if tItem[0] == sItem[1][0][0] and tItem[1] > sItem[1][0][1]:
                    match += 1
                if tItem[0] == sItem[1][1][0] and tItem[1] > sItem[1][1][1]:
                    match += 1
                if tItem[0] == sItem[1][2][0] and tItem[1] > sItem[1][2][1]:
                    match += 1
            else:
                if tItem[0] == sItem[1][0][0] and tItem[1] == sItem[1][0][1]:
                    match += 1
                if tItem[0] == sItem[1][1][0] and tItem[1] == sItem[1][1][1]:
                    match += 1
                if tItem[0] == sItem[1][2][0] and tItem[1] == sItem[1][2][1]:
                    match += 1
        if match == 3:
            return(sItem[0])
print("Part1:",part1())
print("Part2:",part2())


