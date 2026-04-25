import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

grid = {}
for line in lines:
    line = line.strip("\n")
    line = [int(i) for i in line.split(": ")]
    grid[line[0]] = line[1]

depth = max(grid.keys())

state = {}
for key in grid.keys():
    state[key] = [0,1]      # starts at zero, moving forwared

# advance state 1 pico second
def tic(state):
    for key in state.keys():
        if state[key][0] == 0:     # scanner moves foward from 0
            state[key][1] = 1
        if state[key][0] == grid[key] - 1:    # scanner moves backward from end
            state[key][1] = -1
        state[key][0] = (state[key][0] + state[key][1])

    return state

i = 0    # position in layers
severity = 0
while i <= depth:  # while not at the end of the firewall

    if i in state.keys() and state[i][0] == 0: # if layer scanner is 0 when in that position, add severity
        severity += i * grid[i]
    state = tic(state)
    i += 1

print(f"Part 1: {severity}")

for key in state.keys():    # reset state
    state[key] = [0,1]
       
t = 0    # total number of tics
caught = True
while caught:
    i = 0    # position in layers
    caught = False
    currState = state    # save state to reset if caught
    while i <= depth:
        if i in state.keys() and state[i][0] == 0:
            caught = True
            state = tic(currState)  # return to begining of attept and advance one
            t += 1
            break
        if i == depth and not caught: 
            delay = t - depth   # delay = total tics minus depth of firewall
            break
        state = tic(state)
        t += 1
        i += 1
    state = tic(state)  # caught in the last layer
    t += 1
print(f"Part 2: {delay}")
    
