import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

wires =  {}
for line in lines:
    line = line.strip("\n")

    # NEED TO LEARN REGEX!
    line = line.split(" -> ")
#    print(line)
    
    if "AND" in line[0]:
        instruction = "AND"
        line = [line[0].split(" AND "),line[1]]
    if "OR" in line[0]:
        instruction = "OR"
        line = [line[0].split(" OR "),line[1]]
    if "LSHIFT" in line[0]:
        instruction = "LSHIFT"
        line = [line[0].split(" LSHIFT "),line[1]]
    if "RSHIFT" in line[0]:
        instruction = "RSHIFT"
        line = [line[0].split(" RSHIFT "),line[1]]
    if "NOT" in line[0]:
        instruction = "NOT"
        line = [line[0].split("NOT "),line[1]]
    print(line) 

    if type(line[0]) != list:
        if line[0].isdigit():
            wires[line[1]] = int(line[0])
        elif line[0] in wires.keys():
            wires[line[1]] = wires[line[0]]
        else: 
            continue
    else:
        if line[0][0] not in wires.keys() or line[0][1] not in wires.keys():
           line[0][0] = None
           line[0][1] = None
        else:
            match instruction:
                case "AND":
                    wires[line[1]] = wires[line[0][0]] & wires[line[0][1]]
                case "OR":
                    wires[line[1]] = wires[line[0][0]] | wires[line[0][1]]
                case "LSHIFT":
                    wires[line[1]] = wires[line[0][0]] << int(line[0][1])
                case "RSHIFT":
                    wires[line[1]] = wires[line[0][0]] >> int(line[0][1])
                case "NOT":
                    wires[line[1]] = wires[line[0][1]] ^ 0xFFFF # bitwise operators in python use signed integers; this puzzle uses 16 bit values per the instructions so 0xFFFF is needed https://stackoverflow.com/questions/31151107/how-do-i-do-a-bitwise-not-operation-in-python
                case _:
                    print("Unexpected operation")
                    sys.exit(1)

print(wires)
print("Part1 NOT COMPLETE")
print("Part2 NOT COMPLETE")
