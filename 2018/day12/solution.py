import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

    initial_state = lines[0].split(" ")[2].strip("\n")

rules = {}
for line in lines[2:]:
    line = line.strip("\n")
    rule, n = line.split(" => ")
    rules[rule] = n

def next_gen(state,idx):
    next_gen = ''
    idx -= 2
    # account for edge cases (infiinite pots with no plants on either side)
    pad_state = '....' + state + '....'
    initial_series = state[:5]
    for i in range(2,len(pad_state)-2):    
        series = pad_state[i-2:i+3]
        pot = rules.get(series,'.')
        next_gen += pot
    
    # Trim prepended empty pots
    while next_gen[0] != '#':
        next_gen = next_gen[1:]
        idx += 1
    #Trim trailing empty pots
    while next_gen[-1] != '#':
        next_gen = next_gen[:-1]
    tot = 0
    for i,x in enumerate(next_gen):
        if x == '#':
            tot += (i + idx)

        
    return next_gen, tot, idx
   

state = initial_state
total_sum = initial_state.count('#')
idx = 0
iterations = 20
for i in range(1,iterations + 1):
    state,tot,idx  = next_gen(state,idx)

print(f"Part 1: {tot}")

state = initial_state
idx = 0
pots = 0
iterations = 50000000000
for i in range(1,iterations + 1):
    prev_state = state
    state,tot,idx  = next_gen(state,idx)
    
    # population stablizes after so many iterations
    if prev_state == state:
        part2 = tot + (iterations-i)*state.count("#")
        break

print(f"Part 2: {part2}")
