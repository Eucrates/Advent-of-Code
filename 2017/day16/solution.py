import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename> <iterations> <sequence>")
    sys.exit(1)

file = sys.argv[1]
iterations = int(sys.argv[2])
origSequence = [s for s in sys.argv[3]]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def dance(sequence,instructions):

    for instruction in instructions:
        move = instruction[0]
        match move:
            case "s":
                moves = int(instruction[1:])
                subsequence = sequence[-moves:]
                sequence = sequence[:-moves]
                for i in range(moves):
                    sequence.insert(i,subsequence[i])
            case "x":
                positions = [int(i) for i in instruction[1:].split("/")]
                temp = sequence[positions[0]]
                sequence[positions[0]] = sequence[positions[1]]
                sequence[positions[1]] = temp
            case "p":
                programs = [c for c in instruction[1:].split("/")]
                positions = [sequence.index(programs[0]),sequence.index(programs[1])]
                temp = sequence[positions[0]]
                sequence[positions[0]] = sequence[positions[1]]
                sequence[positions[1]] = temp


    return sequence

for line in lines:
    line = line.strip("\n")
    instructions = line.split(",")

sequence = dance(origSequence,instructions)
print(f"Part 1: {"".join(sequence)}")
    
sequences = [''.join(sequence)]
for i in range(iterations):
    sequence = dance(sequence,instructions)
    if ''.join(sequence) in sequences:
        break
    sequences.append(''.join(sequence))
    
print(f"Part 2: {"".join(sequences[iterations % len(sequences)-1])}")
