import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def checkTriangle(triangle):
#    print(triangle)
    if triangle[0] + triangle[1] <= triangle[2]:
        return False
    if triangle[0] + triangle[2] <= triangle[1]:
        return False
    if triangle[1] + triangle[2] <= triangle[0]:
        return False
    return True

valid = 0
tot = 0
tris = []
for line in lines:
    line = line.strip("\n")
    triangle = line.split()
    triangle[0] = int(triangle[0])
    triangle[1] = int(triangle[1])
    triangle[2] = int(triangle[2])
    if checkTriangle(triangle):
        valid += 1
    tris.append(triangle)
print(f"Part 1: {valid}")

i = 0
valid = 0
while i < len(tris) -2:
    if checkTriangle([tris[i][0], tris[i+1][0], tris[i+2][0]]):
        valid += 1
    if checkTriangle([tris[i][1], tris[i+1][1], tris[i+2][1]]):
        valid += 1
    if checkTriangle([tris[i][2], tris[i+1][2], tris[i+2][2]]):
        valid += 1
    i += 3

print(f"Part 2: {valid}")
