import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")
    # do something
    l = [int(x) for x in  line.split(" ")]

def split_node(meta):
    num_children = meta[0]
    num_meta_entries = meta[1]
    meta = meta[2:]
    tot = 0
    values = []

    for _ in range(num_children):
        subtot, value, meta  = split_node(meta)
        tot += subtot
        values.append(value)

    tot += sum(meta[:num_meta_entries])
 
    if num_children == 0:
        return tot, sum(meta[:num_meta_entries]), meta[num_meta_entries:]
    else:
        return  tot, sum(values[n - 1] for n in meta[:num_meta_entries] if n > 0 and n <= len(values)), meta[num_meta_entries:]

part1, part2, _ = split_node(l)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

