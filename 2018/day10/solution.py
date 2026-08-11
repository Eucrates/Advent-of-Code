
# adventofcode.com 2018 Day 10
# based on u/IGChris's solution
# https://www.reddit.com/r/adventofcode/comments/a4skra/2018_day_10_solutions

import sys
from operator import sub

filename = sys.argv[1]

with open(filename) as f:
    inputs = []
    for line in f:
        line = line.strip("\n")
        posx = int(line.split("position=<")[1].strip().split(', ')[0])
        posy = int(line.split("position=<")[1].strip().split(', ')[1].split(">")[0])
        velx = int(line.split("velocity=<")[1].strip().split(', ')[0])
        vely = int(line.split("velocity=<")[1].strip().split(', ')[1].split(">")[0])
        inputs.append((posx, posy, velx, vely))
        
for i in range(15000):  #large number of iterations
    
    # calculate next position of all points
    points = []
    for p in inputs:
        points.append((p[0] + i * p[2], p[1] + i * p[3]))
    
    # find size of background
    min_coords = []
    max_coords = []
    for coord in zip(*points):
        min_coords.append(min(coord))
        max_coords.append(max(coord))
    min_pos = tuple(min_coords)
    max_pos = tuple(max_coords)

    size = (max_pos[0] - min_pos[0] + 1, max_pos[1] - min_pos[1] + 1)
    if size[1] <= 10: # guess at pixel height
        print("Part 1:")
        local_points = [tuple(map(sub, point, min_pos)) for point in points]
        
        # create empty grid
        grid = []
        for y in range(size[1]):
            row = []
            for x in range(size[0]):
                row.append('.')
            grid.append(row)

        # update points
        for p in local_points:
            grid[p[1]][p[0]] = '#'

        # print grid
        for row in grid:
            print(''.join(row))

        print(f"Part 2: {i}")
