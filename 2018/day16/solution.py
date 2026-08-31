import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

i = 0
tests = []
operations = []
while i < len(lines):
    line = lines[i].strip('\n')
    if line.startswith("Before:"):
        before = [int(x) for x in line.split("Before: ")[1].strip('[').strip(']').split(', ')]
        line = lines[i+1].strip('\n')
        operation = [int(x) for x in line.split(' ')]
        line = lines[i+2].strip('\n') 
        after = [int(x) for x in line.split("After:  ")[1].strip('[').strip(']').split(', ')]
        
        test = [before, operation, after,0,[]]
        tests.append(test)
        i += 4
        continue

    while lines[i] == (''):
          i += 1
   
    operation = [int(x) for x in line.split(' ') if x != '']
    operations.append(operation)
    i += 1
operations = operations[2:]

registers = {}

for i in range(4):
    registers[i] = 0

def addr(A,B,C):
    registers[C] = registers[A] + registers[B]

def addi(A,B,C):
    registers[C] = registers[A] + B

def mulr(A,B,C):
    registers[C] = registers[A] * registers[B]

def muli(A,B,C):
    registers[C] = registers[A] * B

def banr(A,B,C):
    registers[C] = registers[A] & registers[B]

def bani(A,B,C):
    registers[C] = registers[A] & B

def borr(A,B,C):
    registers[C] = registers[A] | registers[B]

def bori(A,B,C):
    registers[C] = registers[A] | B

def setr(A,B,C):
    registers[C] = registers[A]

def seti(A,B,C):
    registers[C] = A

def gtir(A,B,C):
    registers[C] = 1 if A > registers[B] else 0

def gtri(A,B,C):
    registers[C] = 1 if registers[A] > B else 0

def gtrr(A,B,C):
    registers[C] = 1 if registers[A] > registers[B] else 0

def eqir(A,B,C):
    registers[C] = 1 if A == registers[B] else 0

def eqri(A,B,C):
    registers[C] = 1 if registers[A] == B else 0

def eqrr(A,B,C):
    registers[C] = 1 if registers[A] == registers[B] else 0


opcodes = {
        "addr": [addr, 0,None],
        "addi": [addi, 0,None],
        "mulr": [mulr, 0,None],
        "muli": [muli, 0,None],
        "banr": [banr, 0,None],
        "bani": [bani, 0,None],
        "borr": [borr, 0,None],
        "bori": [bori, 0,None],
        "setr": [setr, 0,None],
        "seti": [seti, 0,None],
        "gtir": [gtir, 0,None],
        "gtri": [gtri, 0,None],
        "gtrr": [gtrr, 0,None],
        "eqir": [eqir, 0,None],
        "eqri": [eqri, 0,None],
        "eqrr": [eqrr, 0,None]
        }

for i,test in enumerate(tests):
    for opcode in opcodes.keys():
        execution = opcodes[opcode][0]

        registers[0] = test[0][0]
        registers[1] = test[0][1]
        registers[2] = test[0][2]
        registers[3] = test[0][3]

        A,B,C = test[1][1],test[1][2],test[1][3]

        execution(A,B,C) 
        
        if [registers[0],registers[1],registers[2],registers[3]] == test[2]:
           
            tests[i][3] += 1
            tests[i][4].append(opcode)

threeormore = 0
for i,test in enumerate(tests):
    if test[3] >= 3:
        threeormore += 1

print(f"Part 1: {threeormore}")

t = []
for i in range(16):
    for test in tests:
        if test[1][0] == i:
            if sorted(test[4]) not in t:
                t.append(sorted(test[4]))

while any (opcodes[opcode][2] is None for opcode in opcodes.keys()):
    i = 0
    while i < len(tests):
        test = tests[i]
        if len(test[4]) == 1:
            opcodes[test[4][0]][2] = test[1][0]
            for j,t in enumerate(tests):
                if test[4][0] in t[4]:
                    tests[j][4].remove(test[4][0])
                    i = -1 
                    break
        i += 1

opcodemap = {}
for opcode in opcodes.keys():
    opcodemap[opcodes[opcode][2]] = opcode
        

for i in range(4):
    registers[i] = 0

for operation in operations:
    opcode = opcodemap[operation[0]]
    execution = opcodes[opcode][0]
    A,B,C = operation[1],operation[2],operation[3]
    execution(A,B,C)


print(f"Part 2: {registers[0]}")
