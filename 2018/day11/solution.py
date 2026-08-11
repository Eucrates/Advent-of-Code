import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <input>")
    sys.exit(1)

serial = int(sys.argv[1])

def calc_power(x,y):
    power = 0
    rackID = x + 10
    power = rackID * y
    power += serial
    power *= rackID
    power = (power // 100) % 10
    power -= 5
    return power


def calculate_ps(x, y):
    return (
        calc_power(x + 1, y + 1)
        + partial_sums[x, y - 1]
        + partial_sums[x - 1, y]
        - partial_sums[x - 1, y - 1]
    )


grid = [[0] * 301 for _ in range(301)]
partial_sums = [[0] * 301 for _ in range(301)]

for y in range(1,301):
    for x in range(1,301):
        grid[y][x] = calc_power(x,y)
        partial_sums[y][x] = grid[y][x] + partial_sums[y-1][x] + partial_sums[y][x-1] - partial_sums[y-1][x-1]
        
# max_value, None
part1 = (-sys.maxsize - 1,None)
part2 = (-sys.maxsize - 1,None,None)

for size in range(1,301):
    for y in range(size, 300):
        for x in range(size, 300):
            total_power = partial_sums[y][x] - partial_sums[y-size][x] - partial_sums[y][x-size] + partial_sums[y-size][x-size]
            top_left_x = x - size + 1
            top_left_y = y - size + 1
        
            if size == 3 and total_power > part1[0]:
                part1 = (total_power, (top_left_x, top_left_y))

            if total_power > part2[0]:
                part2 = (total_power, (top_left_x, top_left_y), size)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
