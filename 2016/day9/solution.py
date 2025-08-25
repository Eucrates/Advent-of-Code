import sys
import re

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

part1 = 0
for line in lines:
    line = line.strip("\n")
    i = 0
    decomp = ""
    while i < len(line):
        if line[i] == "(":
            j = i + 1
            while line[j] != ")":
                j += 1
            chars,times = line[i+1:j].split("x")
            chars = int(chars)
            times = int(times)
            rep = line[j+1:j+1+chars]
            decomp += rep * times
            i = j + chars

        else:
#            print(line[i],end="")
            decomp += line[i]
        i += 1

    part1 += len(decomp)

print(f"Part 1: {part1}")

# could not the recursion correct on part 2
# this is from blockingthesky's solution https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/
def decompress(s):
    # if the string does not have a  marker, return the length of the string
    if '(' not in s:
        return len(s)

    ret = 0

    # recursively decompress as long as there is a marker in ther string
    while '(' in s:
        ret += s.find('(')  # add length of string to the first open parentheses
        s = s[s.find('('):]  # string now equals up to the first open parentheses
        marker = s[1:s.find(')')].split('x')  # split the marker into string length and number of times repeated
        s = s[s.find(')') + 1:]  # string now equals the remaining string after the closed parentheses
        ret += decompress(s[:int(marker[0])]) * int(marker[1])  # return the length of the string after decompressing
                                                                # the subsequent string and add it to current return value
        s = s[int(marker[0]):] # string now equals the string after the length of the repeated sequence
    ret += len(s) # add the length of the string to the return value
    return ret

for line in lines:
    line = line.strip()
    part2 = decompress(line)
    print(f"Part 2: {part2}")

