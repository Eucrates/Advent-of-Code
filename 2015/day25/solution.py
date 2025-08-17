import sys
import re

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")
    # regular expression adapted from google AI Overview
    # searching for "python parse numbers out of sentence")
    row_column = re.findall(r'\d+\d*', line)
row = int(row_column[0])
column = int(row_column[1])

''' for comparison and troubleshooting
starter_codes = [
 [20151125,  18749137,  17289845,  30943339,  10071777,  33511524],
 [31916031,  21629792,  16929656,   7726640,  15514188,   4041754],
 [16080970,   8057251,   1601130,   7981243,  11661866,  16474243],
 [24592653,  32451966,  21345942,   9380097,  10600672,  31527494],
 [   77061,  17552253,  28094349,   6899651,   9250759,  31663883],
 [33071741,   6796745,  25397450,  24659492,   1534922,  27995004]
 ]
'''


# generate a list of codes long enough to get a square grid of max(row,column)

def genCodes(row,column):
    def next_code(code):
        nextcode = code * 252533
        remainder= nextcode % 33554393
        return remainder

    codes = []
    code = 20151125
    codes.append(code)
    for i in range(max(row, column) ** 2 * 2):
        nextcode = next_code(code)
        codes.append(nextcode)
        code = nextcode
    return codes

codes = genCodes(row,column)

# transformation 1: each row has the code in the correct order:
# row one has code 1
# row two has codes 2 and 3
# row three has codes 4, 5 and 6, etc
codeGrid = []
k = 0
for i in range(1,len(codes))
    gridLine = []
    for j in range(i):
        if k < len(codes):
            gridLine.append(codes[k])
            k += 1
    if k == len(codes):
        break
    codeGrid.append(gridLine)


# transformaiton 2: drops each code back to the proper row
# now row one has codes 1, 3 and 6
# row two has codes 2, 5
# row three has 4
newCodeGrid = []
newLine = [codeGrid[0][0]]
i = 1
h = 0
j = 0
while h < row * column:
    while i < len(codeGrid):
        line = codeGrid[i]
        temp = i
        sentinel = len(line) - 1
        while len(line) > sentinel:            
            num = line.pop()
            newLine.append(num)
            j += 1
            i += 1
        i = temp
        i += 1
    if newLine == []:
        break
    newCodeGrid.append(newLine)
    newLine = []
    h += 1
    i = h

print("Part1:,"newCodeGrid[row-1][column-1])
