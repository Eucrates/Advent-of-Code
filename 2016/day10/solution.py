import sys
import re

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

instructions = []
slots = {}

# sample
#matchValue1 = "2"
#matchValue2 = "5"

# input
matchValue1 = 17
matchValue2 = 61

startswithBot=0

for line in lines:
    line = line.strip("\n")
    pattern1 = r"bot \d+"
    pattern2 = r"output \d+"
# by inspection, my input has no input instructions
#    pattern3 = r"input \d+"


    # create dictionary with all bot and output recipients
    matches = re.findall(pattern1, line)
    for match in matches:
        if match not in slots.keys():
            slots[match] = [None, None]
    matches = re.findall(pattern2, line)
    for match in matches:
        if match not in slots.keys():
            slots[match] = [None, None]

    instructions.append(line)

# initialize values
i = 0
while i < len(instructions):
    if instructions[i].startswith("value"):
        bot = instructions[i].split("to ")[1]
        value = instructions[i].split("value ")[1].split(" goes")[0]
        if slots[bot][0] == None:
            slots[bot][0] = int(value)
        elif slots[bot][1] == None:
            slots[bot][1] = int(value)
        else:
            print(instructions[i])
            print(bot, "full")
            exit(1)
        # remove instruction from list
        instructions.remove(instructions[i])
    else:
        i += 1

# 
i = 0
while i < len(instructions):
    bot = instructions[i].split(" gives")[0]

    # if bot has two chips
    if slots[bot][0] != None and slots[bot][1] != None:
        low_bot = instructions[i].split("to ")[1].split(" and")[0]
        high_bot = instructions[i].split("to ")[2]
        low_value = min(int(slots[bot][0]), int(slots[bot][1]))
        high_value = max(int(slots[bot][0]), int(slots[bot][1]))

        
        if low_value == matchValue1 and high_value == matchValue2:
            part1 = bot
        
        # put values in first available slot (it's sorted when pulled out above)
        if slots[low_bot][0] == None:
            slots[low_bot][0] = low_value
        elif slots[low_bot][1] == None:
            slots[low_bot][1] = low_value
        
        if slots[high_bot][0] == None:
            slots[high_bot][0] = high_value
        elif slots[high_bot][1] == None:
            slots[high_bot][1] = high_value

        # clear bot values    
        slots[bot][0] = None
        slots[bot][1] = None
        
        # Done with this instructino
        instructions.remove(instructions[i])
        
        # cycle back to first instruction to look for full bot
        i = 0
    else:
        i += 1

print(f"Part 1: {part1}")

part2 = slots["output 0"][0] * slots["output 1"][0] * slots["output 2"][0]

print(f"Part 2: {part2}")
