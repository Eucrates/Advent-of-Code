import sys
import hashlib

puzzle_input = "ugkcyxxp"

code1 = ""
code2 = ['-','-','-','-','-','-','-','-']

i = 0
# presuming it takes longer to fill out code2 than code 1
# and that code 1 will then be longer than 8 characters
while '-' in code2:
    h = hashlib.md5((puzzle_input+str(i)).encode('utf-8')).hexdigest()
    if h.startswith("00000"):
        code1 += h[5]
        # make sure h[5] is a vaild digit and only take the first result for each position
        if h[5].isdigit() and int(h[5]) < 8 and code2[int(h[5])] == "-": 
            code2[int(h[5])] = h[6]
    i += 1

print(f"Part 1: {code1[:8]}")
print(f"Part 2: {''.join(code2)}")
