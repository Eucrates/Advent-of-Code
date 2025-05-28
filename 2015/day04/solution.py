import sys
import hashlib

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")
    # do something
    # print(line)

    i = 1
    h = hashlib.md5((line+str(i)).encode('utf-8')).hexdigest()
    while h[:5] != "00000":
        i += 1
        h = hashlib.md5((line+str(i)).encode('utf-8')).hexdigest()
    
        if i % 10000000 == 0:
            print(i, "numbers tried")
    print("Part 1 five leading 0s:", i, h)
    
    i = 1
    h = hashlib.md5((line+str(i)).encode('utf-8')).hexdigest()
    while h[:6] != "000000":
        i += 1
        h = hashlib.md5((line+str(i)).encode('utf-8')).hexdigest()
    
        if i % 10000000 == 0:
            print(i, "numbers tried")
    print("Part 2 six leading 0s:", i, h)
