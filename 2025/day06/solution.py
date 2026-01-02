import sys
import math
import numpy as np

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

grid = []
linear_grid = []
for line in lines:
    line = line.strip("\n")
    line = [x for x in list(line)]           # list of all characters in line
    line.insert(0,' ')                       # add space to begining of line for consisitency
    grid.append(line)                        # make a grid of lines
    for n in line: linear_grid.append(n)     # make a linear representation of all characters in input
    
if len(grid[0]) != len(grid[-1]):            # sample input does not have trailing spaces after operators
    print("Correcting length of operator line")
    for _ in range(len(grid[0])-len(grid[-1])):
        grid[-1].append(' ')
        linear_grid.append(' ')

assert [len(grid[i]) == len(grid[i+1]) for i in range(len(grid[:-1]))]   # ensure all lines are of the same length

operators = []                       # get list of operators and their indices
op_indices = []                      # length of numbers in columns varies in input, but not in sample 
for i, op in enumerate(grid[-1]):
    if op != ' ':
        operators.append(op)
        op_indices.append(i)
op_indices.append(len(grid[-1])+1)

lengths = []                         # calculate length of column for each column in input
for i in range(1,len(op_indices)):
    lengths.append(op_indices[i] - op_indices[i-1])


i = 0
horiz_nums = []
while i < len(linear_grid):
    nums = []
    for length in lengths:                     # use column length to determine size of number
        chunk = linear_grid[i:i+length]            
        nums.append(chunk)
        i += length
    assert(len(nums) == len(operators) == len(lengths)) # ensure each line has the same amount of numbers
                                                        # as there are operators and lengths
    horiz_nums.append(nums)             

part1 = 0
for l in range(len(lengths)):                           # could also use operators list or a line in the grid      
    next_form = []                                      # transpose horizontal list into vertical
    for j in range(len(grid[:-1])):                     # skip operator line
        next_form.append(int(''.join(horiz_nums[j][l]).strip()))
        if len(next_form) == len(grid[:-1]):            # if we have all the numbers in a column
            if operators[l] == '*':                     # caluclate
                part1 += math.prod(next_form)
            else:
                part1 += sum(next_form)

print(f"Part 1: {part1}")

vert_nums = []                                          # transform intermediate form into numbers by column
for i,l in enumerate(lengths):                          # i is the index of the nums/operators/lengths;  
    nums = []                                           #     see previous assertion
    for j in range(l):                                  # for each column in a number of length l
        num = ''
        for k in range(len(grid)):                      # repeat for each line in the grid
            num += horiz_nums[k][i][j]
        nums.append(num)
    vert_nums.append(nums)

part2 = 0
for i,form in enumerate(vert_nums):
    assert [len(nums) == len(grid) for nums in form[1:]]    # ensure each list of numbers is as long as the length of the grid
    if operators[i] == '+':                                 # calculate
        ints = [int(''.join(num[:-1]).strip()) for num in form[1:]]
        part2 += sum(ints) 
    else:
        ints = [int(''.join(num[:-1]).strip()) for num in form[1:]]
        part2 += math.prod(ints)

print(f"Part 2: {part2}")
