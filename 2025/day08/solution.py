import sys
import math

import numpy as np
from scipy.spatial.distance import cdist

# https://blender.stackexchange.com/questions/271586/calculate-the-distance-for-every-entry-of-2-lists-with-x-y-z-3d-coordinates-usin

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

boxes = []

for line in lines:
    line = line.strip("\n")
    box = [int(n) for n in line.split(",")]
    boxes.append(box)

num_boxes = len(boxes)
distances = []
for box1 in range(num_boxes):
    for box2 in range(box1+1,num_boxes):
        x = (boxes[box1][0] - boxes[box2][0]) ** 2
        y = (boxes[box1][1] - boxes[box2][1]) ** 2
        z = (boxes[box1][2] - boxes[box2][2]) ** 2
        dist = math.sqrt(x+y+z)                         # because math
        distances.append([[box1,box2],dist])            

distances.sort(key=lambda x: x[1],reverse=True)         # sort on distances  (reversed, because using the pop method later on which takes the last element)

circuits = [{box} for box in range(num_boxes)]          # each box starts in its own circuit        

def getCircuit(box):
    for c, circuit in enumerate(circuits):
        if box in circuit:
            return c



i = 0
while i < 1000:                                         # per the instructions, we're looking at the first 1000 pairs                   
    box1,box2 = distances.pop()[0]                      # get the boxes that are the shortest distance appart
    c1 = getCircuit(box1)                               # find out which circuit the box is in
    c2 = getCircuit(box2)                                  
    if c1 != c2:                                        # if they're not the same circuit, merge circuits and delete the circuit of the second box
        circuits[c1] = circuits[c1] | circuits[c2]
        del circuits[c2]
    i += 1

circuits = sorted(circuits,key=len,reverse=True)        # sort circuits by length

part1 = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
print(f"Part 1: {part1}")

oneCircuit = False                                      # stop merging boxes after one circuit has formed that is the same lenghth as the number of boxes
while len(distances) > 1:
    box1,box2 = distances.pop()[0]                      # continue until all the distance pairs have been used (will break early when full circuit is formed)
    c1 = getCircuit(box1)
    c2 = getCircuit(box2)
    if c1 != c2:
        circuits[c1] = circuits[c1] | circuits[c2]
        del circuits[c2]
    for circuit in circuits:                            # check for a full circuit; break out of while loop if found, current boxes are last two needed for full circuit
        if len(circuit) == num_boxes:
            oneCircuit = True
            break
    if oneCircuit:
        break
    i += 1

part2 = boxes[box1][0] * boxes[box2][0]
print(f"Part 2: {part2}")
