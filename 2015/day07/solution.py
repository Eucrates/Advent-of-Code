import sys
import copy

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

# if the requisite signals are resolved, the output will be calculated
# and the function signal changed to ->
def calculate(wire):
    instruction = wire[1]
    if type(wire[0]) == list:

        if type(wire[0][1]) == int and instruction == "NOT":         # https://stackoverflow.com/questions/31151107/how-do-i-do-a-bitwise-not-operation-in-python
            wire[0] = wire[0][1] ^ 0xFFFF                            # bitwise operators in python use signed integers; to get the right value we need to XOR with
            wire[1] = "->"                                           # a bit mask; the puzzle uses 16 bit values per the instructions so value is XOR'd with 0xFFFF
        elif type(wire[0][0]) == int and type(wire[0][1]) == int:
            match instruction:
                case "AND":
                    wire[0] = wire[0][0] & wire[0][1]
                case "OR":
                    wire[0] = wire[0][0] | wire[0][1]
                case "LSHIFT":
                    wire[0] = wire[0][0] << wire[0][1]
                case "RSHIFT":
                    wire[0]= wire[0][0] >> wire[0][1]
                case _:
                    print("Unexpected operation in calculate:", wire[1])
                    value = wire[0]
            wire[1] = "->"
    return wire

# called recursively whenever a value is resolved
# when a wire is fully resolved, -> is changed to
# -- as sentry
def update(wires, key, value):
    
    # if wire has a place holder, get the value from that place holder
    if type(wires[key][0]) == str:
        wires[key][0] = wires[wires[key][0]][0]

    for k in wires.keys():
        if type(wires[key][0]) == int and wires[key][1] == "->":
            wires[key][1] = "--"

        if type(wires[k][0]) == list:
            if wires[k][0][0] == key:
                wires[k][0][0] = value
            if wires[k][0][1] == key:
                wires[k][0][1] = value
            if type(wires[k][0][0]) == int and type(wires[k][0][1]) == int:
                wires[k] = calculate(wires[k])
            if type(wires[k][0]) == list and type(wires[k][0][1]) == int and wires[k][1] == "NOT":
                wires[k] = calculate(wires[k])
        if wires[k][1] == "->":
            if type(wires[k][0]) == int:
                wires = update(wires, k, wires[k][0])
    return wires

# setup for recursive call; iterates through dictionary, updates the 
# dictionary using the current key:value pairs 
def connect(wires):
    for key in wires.keys():
        if wires[key][1] == "->":
            wires = update(wires,key,wires[key][0])
    return wires


# parse into oritinal dictionary
def getDict(lines):
    d =  {}
    for line in lines:
        line = line.strip("\n")

        line = line.split(" -> ")
        instruction = None    
        if "AND" in line[0]:
            instruction = "AND"
            line = [line[0].split(" AND "),line[1]]
        elif "OR" in line[0]:
            instruction = "OR"
            line = [line[0].split(" OR "),line[1]]
        elif "LSHIFT" in line[0]:
            instruction = "LSHIFT"
            line = [line[0].split(" LSHIFT "),line[1]]
        elif "RSHIFT" in line[0]:
            instruction = "RSHIFT"
            line = [line[0].split(" RSHIFT "),line[1]]
        elif "NOT" in line[0]:
            instruction = "NOT"
            line = [line[0].split("NOT "),line[1]]
        else:
            instruction = "->"
            line = [line[0],line[1]]
    
        if type(line[0]) == list:
            if line[0][0].isdigit():
                line[0][0] = int(line[0][0])
            if line[0][1].isdigit():
                line[0][1] = int(line[0][1])
        elif type(line[0]) == str:
            if line[0].isdigit():
                line[0] = int(line[0])
        else:
            print("Unexpected type in main:",type(line[1]))

        d[line[1]] = [line[0],instruction] 

    return d

original_wires = getDict(lines)

part1_wires = copy.deepcopy(original_wires)  # without deep copy, mutable object inside the dictionary (lists) still point to the same memory locations after the dicitionary is changed
part2_wires = copy.deepcopy(original_wires)  # https://docs.python.org/3/library/copy.html

part1_wires = connect(part1_wires)
print("Part1: a =", part1_wires["a"][0])

# reconfigure wires
part2_wires["b"][0] = part1_wires["a"][0]
part2_wires = connect(part2_wires)
print("Part2: a =", part2_wires["a"][0])
