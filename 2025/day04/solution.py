import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

grid = ['.' * (len(lines[0].strip("\n"))+2)]        # place . around all four sides of grid to account for edge cases
for line in lines:
    line = line.strip("\n")
    grid.append("." + line + '.')
grid.append('.' * (len(lines[0].strip("\n"))+2))


def countRolls(grid):
    access = 0
    removal_queue = set()
    for r in range(1,len(grid) - 1):
        for c in range(1,len(grid[r]) - 1):
            count = 0
            if grid[r][c] != '@':        # check each surrounding square
                continue
            if grid[r-1][c-1] == '@':
                count += 1
            if grid[r-1][c] == '@':
                count += 1
            if grid[r-1][c+1] == '@':
                count += 1
            if grid[r][c-1] == '@':
                count += 1
            if grid[r][c+1] == '@':
                count += 1
            if grid[r+1][c-1] == '@':
                count += 1
            if grid[r+1][c] == '@':
                count += 1
            if grid[r+1][c+1] == '@':
                count += 1
            if count < 4:
                access += 1
                removal_queue.add((r,c))
    return access,removal_queue


part1,_ = countRolls(grid)
print(f"Part 1: {part1}")

part2 = 0

if part1 == 0: removable = False
else: removable = True

while removable:
    _,removal_queue = countRolls(grid)    
    if len(removal_queue) == 0:        # no more removable rolls
        removable = False
    else:
        for roll in removal_queue:     
            r,c = roll[0],roll[1]
            grid[r] = grid[r][:c] + '.' + grid[r][c+1:]  # grid[r][c] = @; replace it with .
        part2 += len(removal_queue)                      

print(f"Part 2: {part2}")
