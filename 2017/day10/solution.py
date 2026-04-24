import sys

if len(sys.argv) < 3:
    print("Usage: solution.py <filename> <length>")
    exit(1)

file = sys.argv[1]
size = int(sys.argv[2])

def twister(string,sequence,pos,skip):

    for length in sequence:
        indices = [index % len(string) for index in range(pos,pos+length)]
        segment = [string[j] for j in indices]
        segment = segment[::-1]
        for j, val in enumerate(segment):
            string[(j+pos)%len(string)] = val 
        pos += length + skip
        pos = pos % len(string)
        skip += 1
    return string,pos,skip

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    pos = 0
    skip = 0
    string = [i for i in range(size)]
    
    if sys.argv[1] == "sample3.txt":
        pass
    else:
        sequence = [int(i) for i in line.strip("\n").split(",")]
        string,pos,skip = twister(string,sequence,pos,skip)
        print(f"Part 1: {string[0] * string[1]}")

    pos = 0
    skip = 0
    string = [i for i in range(size)]
    if line == "\n":
        sequence = []
    else:
        sequence = [ord(c) for c in line.strip("\n")]
    for i in [17,31,73,47,23]:
        sequence.append(i)
    for _ in range(64):
        string,pos,skip = twister(string,sequence,pos,skip)

    denseHash = []
    for i in range(0,len(string),16):
        d = string[i:i+16]
        dense = d[0]
        for j in d[1:]:
            dense ^= j
        
        denseHash.append(dense)
    knotHash = "".join(f"{d:02x}" for d in denseHash)
    print(f"Part 2: {knotHash}")

