import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def validChrs(password):

    invalid = "iol"

    for c in invalid:
        if c in line:
            return False
    return True

def straight(password):
    ret = False
    for i in range(len(password) - 2):
        if ord(password[i])+1 == ord(password[i+1]) and ord(password[i])+2 == ord(password[i+2]):
            ret = True
            break
    return ret

def doublePair(password):
    pairs = 0
    i = 0
    while i < len(password)-1:

        if line[i] == line[i+1]:
            
            pairs += 1
            i += 2
        else:
            i += 1
    if pairs >= 2:
        return True
    else:
        return False

def increment(password):
    numPass = []
    for i in range(len(password)):
        numPass.append(ord(password[i]))

    numPass = numPass[::-1]
    numPass[0] += 1
    for i in range(len(numPass)-1):
        if numPass[i] > ord("z"):
            numPass[i] = ord("a")
            numPass[i+1] += 1


    numPass = numPass[::-1]
    passwordInc = ""
    for i in range(len(numPass)):
        passwordInc += chr(numPass[i])

    return passwordInc


for line in lines:
    line = line.strip("\n")
    while True:
        line = increment(line)
        if validChrs(line) and doublePair(line) and straight(line):
            break
print("Part1:",line)
while True:
    line = increment(line)
    if validChrs(line) and doublePair(line) and straight(line):
        break
print("Part2:",line)
