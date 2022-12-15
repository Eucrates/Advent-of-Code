
rows = []
with open ("input.txt","r") as f:
    for i in range (8):
        rows.append(f.readline().strip("\n"))
    f.readline()
    f.readline()
    lines = f.readlines()

dock = list(zip(rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))

dock = [
['Z','J','N','W','P','S'],
['G','S','T'],
['V','Q','R','L','H'],
['V','S','T','D'],
['Q','Z','T','D','B','M','J'],
['M','W','T','J','D','C','Z','L'],
['L','P','M','W','G','T','J'],
['N','G','M','T','B','F','Q','H'],
['R','D','G','C','P','B','Q','W']
]

for line in lines:
    count, stack1, stack2 = int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5].strip())
    for i in range(count):
        
        crate = dock[stack1-1].pop()
        dock[stack2-1].append(crate)

s = ''
for i in dock:
    s += i.pop()

print (s)

dock = [
['Z','J','N','W','P','S'],
['G','S','T'],
['V','Q','R','L','H'],
['V','S','T','D'],
['Q','Z','T','D','B','M','J'],
['M','W','T','J','D','C','Z','L'],
['L','P','M','W','G','T','J'],
['N','G','M','T','B','F','Q','H'],
['R','D','G','C','P','B','Q','W']
]
for line in lines:
    count, stack1, stack2 = int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5].strip())
    sublist = dock[stack1-1][len(dock[stack1-1])-count:len(dock[stack1-1])]
    for item in sublist:
        dock[stack1-1].pop()
        dock[stack2-1].append(item)


s = ''
for i in dock:
    s += i.pop()

print (s)
