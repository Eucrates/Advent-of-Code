import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def p1(line):

    joltage = str(max([int(x) for x in line[:-1]]))    # max value in line before last character
    for marker in range(len(line[:-1])):                    # find first occurance of max value in line
        if line[marker] == joltage:
            break
    joltage += str(max([int(x) for x in line[marker+1:]]))  # max value in line after first digit

    return int(joltage)

def p2(line):

    DIGITS = 12
    joltage = ""
    marker = 0

    while len(joltage) < DIGITS:
        chunk = line[marker:len(line)-(DIGITS-len(joltage))+1]    # only nead to search from current marker to 
        digit = max([int(x) for x in chunk])                      # length of remaining digits in joltage
        joltage += str(digit)
        for i in range(len(chunk)):                               # find first occurance of max digit in chunk
            if int(chunk[i]) == digit:                            
                break
        marker = i + marker + 1                          # marker is current marker plus ith place in chunk + 1
        
    return int(joltage)

part1 = 0
part2 = 0

for line in lines:
    line = line.strip("\n")
    part1 += p1(line)
    part2 += p2(line)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
