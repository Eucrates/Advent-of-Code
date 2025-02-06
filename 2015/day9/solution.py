import sys
import itertools

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline



locations = []
distances = {}
for line in lines:                                                      # parse lines
    line = line.strip("\n")                                             
    # do something
    # print(line)

    key = line.split(" = ")[0]                                          # get distance from location1 to location2,
    distances[key] = line.split(" = ")[1]                               # add it as a key with the distance as the value
    reverse = key.split(" to ")[1] + " to " + key.split(" to ")[0]      # do the same with location2 to location1   
    distances[reverse] = line.split(" = ")[1]
    location1 = line.split(" to ")[0]
    location2 = line.split(" to ")[1].split(" = ")[0]
    if location1 not in locations:                                      # make a list of all locations
       locations.append(location1)
    if location2 not in locations:
        locations.append(location2)



permutations = list(itertools.permutations(locations))                  # generate a list of all combainations of all locations

routes = {}                                                             # dictionary of routes
for perm in permutations:           
    keys = []
    for i in range(len(perm) - 1):
        keys.append(perm[i] + " to " + perm[i +1])                      # use location1 "to location2" as key
    tot = 0
    route = ""
    for key in keys:
        route += key + " "
        tot += int(distances[key])                                      # add the total distance traveled per route to a list
    routes[route] = tot

dist = []
for key in routes.keys():                                               # make a list of the distances
    dist.append(routes[key])

minDist = min(dist)                                                     # select the minimum distance
maxDist = max(dist)

print("Part1: Minimum distance:", minDist)
print("Part2: Maximum distance:", maxDist)
