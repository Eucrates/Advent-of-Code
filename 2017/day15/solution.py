import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

startingValues = []
for line in lines:
    line = int(line.strip("\n").split("with ")[1])
    startingValues.append(line)

A = startingValues[0]
B = startingValues[1]
part1 = 0
for _ in range(40000000):
    A = (A * 16807) % 2147483647
    B = (B * 48271) % 2147483647
    if f"{A:032b}"[16:] == f"{B:032b}"[16:]:
        part1 += 1
print(f"Part 1: {part1}")

A = startingValues[0]
B = startingValues[1]
part2 = 0
generators = [[],[]]
while len(generators[0]) < 5000000 or len(generators[1]) < 5000000:
    A = (A * 16807) % 2147483647
    B = (B * 48271) % 2147483647
    if A % 4 == 0:
        generators[0].append(A)
    if B % 8 == 0:
        generators[1].append(B)

for i in range(5000000):
    if f"{generators[0][i]:032b}"[16:] == f"{generators[1][i]:032b}"[16:]:
        part2 += 1
print(f"Part 2: {part2}")

