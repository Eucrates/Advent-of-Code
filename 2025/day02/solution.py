import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")


def p1(first, last):
    s = 0
    for i in range(int(first),int(last)+1):
        if len(str(i)) / 2 > len(str(i)) // 2:    # skip when i is odd; 
            continue                              # cannot have two equal sequences
        if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:    # if first half equals second half
            s += i
    return s

def p2(first,last):
    repeats = set()    # repeats must be a set, otherwise the same number could be counted more than once
    for i in range(int(first),int(last)+1):
        maxstring = len(str(i))//2        # largest the substring could be is half the string
        for window in range(1,maxstring + 1):    # look for repeated patterns of any possible length
            if str(i)[:window]*(len(str(i))//window) == str(i):    # substring of window length * how many times the substring could be repeated   
                repeats.add(i)
    return sum(repeats)    


ranges = line.split(",")
part1 = 0
part2 = 0
for r in ranges:
    first,last = r.split("-")
    part1 += p1(first,last)
    part2 += p2(first,last)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
