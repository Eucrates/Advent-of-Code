import sys
import re

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def checkABBA(s):
    
    for i in range(len(s)-3):
        if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
            return True
    return False

def checkABA(hypernet,outer):

    def checkBAB(seg, BAB):
        #print(BAB, end = " ")
        if BAB in seg:
            return True
        return False
    
    for s in outer:
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] == s[i+2]:
         #       print(s[i:i+3], end=" ")
                for seg in hypernet:
                    if checkBAB(seg,s[i+1]+s[i]+s[i+1]):
         #               print
                        return True

    #print
    return False

tls = 0
ssl = 0
for line in lines:
    line = line.strip("\n")
    # extract string within brackets:
    # https://www.geeksforgeeks.org/python/python-extract-substrings-between-brackets/
    hypernet = re.findall(r"\[(.*?)\]",line)
    # https://stackoverflow.com/questions/17284947/regex-to-get-all-text-outside-of-brackets
    # solution by Andrew Clark
    outer = re.findall(r'([^[\]]+)(?:$|\[)', line)
    # print('\n',line, outer, hypernet)
    TLS = True
    for seg in hypernet:
        if checkABBA(seg):
            TLS = False
            break
    if TLS == False:
        continue
    for seg in outer:
        if checkABBA(seg):
            tls += 1
            break
    
for line in lines:

    hypernet = re.findall(r"\[(.*?)\]",line)
    outer = re.findall(r'([^[\]]+)(?:$|\[)', line)

    if checkABA(hypernet,outer):
        ssl += 1
        continue

print(f"Part 1: {tls}")
print(f"Part 2: {ssl}")


