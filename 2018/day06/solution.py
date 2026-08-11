# adventofcode.com 2018 day 6
# solution derivied with help from https://www.reddit.com/r/adventofcode/comments/a3kr4r/2018_day_6_solutions/

import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

coords = set()
max_r = 0
max_c = 0

for line in lines:
    line = line.strip("\n")
    line = line.split(", ")
    r,c = int(line[0]), int(line[1])
    coords.add((r,c))
    max_r = max(max_r, r)
    max_c = max(max_c, c)

coord_point = {coord: point for coord, point in enumerate(coords, start=1)}
sizes = {}
infinite = set()

for i in range(max_r + 1):
    for j in range(max_c + 1):
        man_dist = sorted([(abs(r-i) + abs(c-j), coord) for coord, (r,c) in coord_point.items()])

        if len(man_dist) == 1 or man_dist[0][0] != man_dist[1][0]:
            coord = man_dist[0][1]
            if coord in sizes.keys():
                sizes[coord] += 1
            else:
                sizes[coord] = 1

            if i ==0 or i==max_r or j == 0 or j == max_c:
                infinite.add(coord)

part1 = max(size for coord, size in sizes.items() if coord not in infinite)
print(f"Part 1: {part1}")

part2 = 0
for i in range(max_r + 1):
    for j in range(max_c + 1):
        part2 += int(sum(abs(r - i) + abs(c - j) for r,c in coords) < 10000)

print(f"Part 2: {part2}")
