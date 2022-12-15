from collections import defaultdict

with open ("input.txt") as f:
    lines = f.readlines()


path = []
system = defaultdict(int)
tot = 0
for line in lines:

    # if it's a command
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "..":
            path.pop()
        else:
            if d == "/":
                path.append("root")
            else:
                path.append(d)
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        continue
    elif line.split()[0].isdigit():
        size = int(line.split()[0])
        # add the file size to each folder in the path
        for i in range (len(path)):
            system["/".join(path[:i+1])] += size
    else:
        print("Something's wrong with line[0]")
        exit(1)


tot = 0
for key in system.keys():
    if system[key] < 100000:
        tot+=system[key]
    print (key,system[key])
print (tot)


unused = 70000000 - system['root']
needed = 30000000 - unused

print ("Unused space =", unused)
print ("Needed space =", needed)

current = system['root'] 
for key in system.keys():
    if system[key] >= needed and system[key] < current:
        current = system[key]

print ("Smallest folder to delete and free up needed space is", current)

