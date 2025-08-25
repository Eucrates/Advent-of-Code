import sys
from statistics import mode

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

'''
messages = []
for line in lines:
    line = line.strip("\n")
    # do something
    messages.append(line)
'''

# https://www.geeksforgeeks.org/python/python-find-most-frequent-element-in-a-list/
def most_common(charList):
    return mode(charList)

def least_common(charList):
    d = {}
    for c in charList:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    
    min_val = len(charList)
    for key in d.keys():
        if d[key] < min_val:
            min_val = d[key]
            letter = key

    return letter

message1 = ""
message2 = ""

for i in range(len(lines[0])-1): # repeat for all characters except newline
    charList = []
    for line in lines:
        charList.append(line[i])
    message1 += most_common(charList)
    message2 += least_common(charList)

print(f"Part 1: {message1}")
print(f"Part 2: {message2}")
