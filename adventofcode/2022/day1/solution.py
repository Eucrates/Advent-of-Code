#!/usr/bin/python3

def max (l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    l.remove(m)
    return m,l


elfs = []
sum = 0
with open ("input.txt","r") as f:
    for line in f:
        if line == "\n":
            elfs.append(sum)
            sum = 0
        else:
            sum += int(line.strip()) 


maximum,elfs = max(elfs)
print (f"Most calories by one elf = {maximum}")
top3 = maximum
maximum,elfs = max(elfs)
top3 += maximum
maximum,elfs = max(elfs)
top3 += maximum
print (f"Calories by top 3 elves = {top3}")

