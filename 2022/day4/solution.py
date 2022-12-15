with open("input.txt","r") as f:
    lines = f.readlines()

alloverlap = 0
anyoverlap = 0
for line in lines:
    s1 = int(line.strip().split(",")[0].split("-")[0])
    e1 = int(line.strip().split(",")[0].split("-")[1])
    s2 = int(line.strip().split(",")[1].split("-")[0])
    e2 = int(line.strip().split(",")[1].split("-")[1])
    l1 = []
    l2 = []
    for i in range (s1,e1+1):
        l1.append(i)
    for i in range (s2,e2+1):
        l2.append(i)
    if (set(l1) <= set (l2)) or (set(l2) <= set(l1)):
        alloverlap +=1
    if any(x in l1 for x in l2):
        anyoverlap += 1

print("all: ", alloverlap)
print("any: ", anyoverlap)
