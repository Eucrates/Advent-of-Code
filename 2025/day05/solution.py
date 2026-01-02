import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

i = 0
IDs = False                # marker for switch from ranges to ids
ids = []
ranges = []
while i < len(lines):
    if IDs:
        ids.append(int(lines[i].strip("\n")))
    elif lines[i] == "\n":
        IDs = True
        i += 1
        continue
    else:
        ranges.append(lines[i].strip("\n").split("-"))
        ranges[i][0] = int(ranges[i][0])
        ranges[i][1] = int(ranges[i][1])
    i += 1

fresh = set()                             # set will contain only unique ids
for i in ids:                             # for each id
    for r in ranges:                      #    for each range
        if i >= r[0] and i <= r[1]:       #        if id in range
            fresh.add(i)                  #           add id to set

part1 = len(fresh)
print(f"Part 1: {part1}")

ranges = sorted(ranges, key=lambda sublist: sublist[0])    # sort ranges by starting value

i = 0
while i < len(ranges)-1:
    a = ranges[i][0]            # current range start
    b = ranges[i][1]            # current range end
    c = ranges[i+1][0]          # next range start
    d = ranges[i+1][1]          # next range end

    if c > b:                   # if next range starts after current range ends, no need to merge
        i += 1 
        continue
    merged_range = ['-','-']    # sets current range list to non digits; if case is missed, error will occur when total is calculated
    if d <= b:                  # if next range ends before or when current range ends,
        merged_range[1] = b     # merged range end = current range end
        if c <= b:              # if next range begins before or when current range ends,
            merged_range[0] = a # merged range start = current range start
        else:                   # else  
            merged_range[0] = c # merged range start = next range start

    else:                       # if next range ends after current range ends
        merged_range[1] = d     # merged range end = next range end
        if c <= b:              # if next range starts before or when current range ends
            merged_range[0] = a # merged range start = current range start
        else:                   # else
            merged_range[0] = c # merged range start = next range start

    ranges[i+1] = merged_range  # set next range to merged range 
    ranges.remove(ranges[i])    # remove current range

# ranges no longer overlap

part2 = sum([r[1]+1 - r[0] for r in ranges])    # sum of differences in ranges
print(f"Part 2: {part2}")



