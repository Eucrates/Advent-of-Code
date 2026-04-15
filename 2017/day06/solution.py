import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip('\n')
    # do something
    banks = [int(b) for b in line.split()]

#part 1
combos = [[b for b in banks]]
index = banks.index(max(banks))
maxblock = banks[index]
banks[index] = 0

while True:
    while maxblock > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        maxblock -= 1
    if banks in combos:
        break
    else:
        combos.append([b for b in banks])
    index = banks.index(max(banks))
    maxblock = banks[index]
    banks[index] = 0
    banks = [b for b in banks]

print(f"Part 1: {len(combos)}")

#part2 same as part 1; just starting the final bank configuration from part 1
combos = []
while True:
    while maxblock > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        maxblock -= 1
    if banks in combos:
        break
    else:
        combos.append([b for b in banks])
    index = banks.index(max(banks))
    maxblock = banks[index]
    banks[index] = 0
    banks = [b for b in banks]

print(f"Part 2: {len(combos)}")
