import sys
import math
import numpy as np

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

mathgrid1 = []
mathgrid2 = []
max_digits = 0
for line in lines:
    line = line.strip("\n")
    mathgrid2.append([x for x in list(line)])
    #print(len([x for x in list(line)]))
    #line = [x for x in line.split(" ") if x != ""]
    mathgrid1.append(line)

numlength_list = []
for i,n in enumerate(line):
    if n == '+' or n == '*':
        numlength_list.append(i)

dist = []
for i in range(1,len(numlength_list)):
    d = numlength_list[i]-numlength_list[i-1]
    dist.append(d)

j = 0
for i in range(len(dist)):
    assert len(mathgrid2[0][j:j+dist[i]]) == len(mathgrid2[0][j:j+dist[i]]) == len(mathgrid2[0][j:j+dist[i]]) == len(mathgrid2[0][j:j+dist[i]]) == len(mathgrid2[0][j:j+dist[i]]) 
    j += dist[i]


part1 = 0
operands = [x for x in mathgrid1[-1]]
for i in range(len(mathgrid1[0])):
    for grid in mathgrid1[:-1]:
#        operands.append(int(grid[i]))
        
    if mathgrid1[-1][i] == "*":
        part1 += math.prod(operands)
    else:
        part1 += sum(operands)

print(f"Part 1: {part1}")

#print(max_digits)

for h in range(len(dist)):
    nums = [''] * dist[h]
    vert_nums = []
    
    for i in range(len(mathgrid2[0])):
        num = ''
        for j, row in enumerate(mathgrid2[:-1]):
        #print(j,i,mathgrid2[j][i],row)
            num += mathgrid2[j][i]
        vert_nums.append(num)
 #   print(mathgrid2[h])
            #nums[i] += mathgrid2[h][j]
operands = [x for x in mathgrid2[-1] if x != ' ']


nums = []
numbers = []
for i in range(len(vert_nums)):
    num += vert_nums[i]
    if vert_nums[i].strip() != '':
        nums.append(vert_nums[i])
        if i%len(vert_nums)%len(mathgrid2)==len(mathgrid2[:-1]):
            line = [int(x.strip()) for x in nums]
            line.append(operands[len(numbers)])
            numbers.append(line)
            nums =  []

part2 = 0
for numlist in numbers:
    print(numlist)

    if numlist[:-1] == '+':
        part2 += sum(numlist[:-1])
    else:
        part2 += math.prod(numlist[:-1])

print(len(mathgrid2))
print(f"Part 2: {part2}")
