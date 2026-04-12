import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

part1 = 0
part2 = 0
for line in lines:
    line = line.strip("\n")
    # do something
    nums = line.split()
    ints = []
    for i, num in enumerate(nums):
        ints.append(int(num))
    part1 += (max(ints) - min(ints))
    result = 0
    for c,i in enumerate(ints):                # cycle through ints
        if result != 0:                        # break and sum conditions
            part2 += result
            result = 0
            break
        n = len(ints)
        for j in range(n-1):                
            k = ints[(j+c+1) % n]              # go through remaining ints circularly
            if max(i,k) % min(i,k) == 0:       # setup result and break conditions
                result += max(i,k) // min(i,k)
                break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
