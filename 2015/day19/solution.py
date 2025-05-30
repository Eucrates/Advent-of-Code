# used hints from https://www.reddit.com/r/adventofcode/comments/num2k6/2015_day_19_part_2_i_dont_want_specifics_but_can/ to arrive at reversing the problem for part2
import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.read().split("\n")[:-1]
    for i,line in enumerate(lines):
        lines[i] = line.replace("=","-")

transitions = []
for i,line in enumerate(lines):
    if "->" in line:
        line = line.split(" -> ")
        transitions.append((line[0], line[1]))
    elif line != "":
        molecule = line


molecules = set()

for transition in transitions:
    for i in range(len(molecule)):            # for each character in molecule
        for j in range(len(transition[0])):   # for each chatacter in transition key
            # if molecule character doesn't match transition key or we reach the end of the molecule break
            if (molecule[i + j] != transition[0][j]) or (i+j == len(molecule)):
                break
        # if we do not break, add the molecule to the set
        else:
            molecules.add(molecule[:i] + transition[1] + molecule[i + len(transition[0]):])

print(f"Part 1: {len(molecules)}")

                                     # working backwards form the final molecule
steps = 0                            # replace each occurance of the final transition with starting transition
while molecule != 'e':               # repeat the process until arriving at e
    for start, fin in transitions:   # for each transition in the list, replace the final transition with
        if fin in molecule:          # the starting value
            steps += 1
            molecule = molecule.replace(fin, start, 1)  # update the molecule
print (f"Part 2: {steps}")



