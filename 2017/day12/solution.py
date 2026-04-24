import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

piped = {}
for line in lines:
    line = line.strip("\n")
    line = line.split(" <-> ")
    programA = line[0]
    programB = line[1].split(", ")
    piped[programA] = set(programB)
    piped[programA].add(programA)

for _ in range(2):       # run twice to ensure each key has the full set of programs piped to it 
    for key in piped.keys():
        for key2 in piped.keys():
            if key in piped[key2]:
                for program in piped[key2]:
                    piped[key].add(program)


print(f"Part 1: {len(piped["0"])}")

# frozen sets implementation discussed here
# https://stackoverflow.com/questions/73997158/python-how-to-get-the-unique-sets-from-a-group-of-sets
sets = list(piped.values())
print(f"Part 2: {len(set(map(frozenset, sets)))}")
