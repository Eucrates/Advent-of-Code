def gval(l):
 
    if l.islower():
        return ord(l)-96
    else:
        return ord(l)-38

with open ("input.txt","r") as f:
    
    lines = f.readlines()

tot = 0
for line in lines:
    
    l1,l2 = line[:len(line)//2],line[len(line)//2:len(line)-1]
    for l in l1:
        if l in l2:
            tot += gval(l)
            break
   
print (tot)
tot2 = 0
for i in range(0,len(lines),3):
    for l in lines[i].strip():
        if l in lines[i+1].strip() and l in lines[i+2].strip():
            tot2 += gval(l)
            break
print (tot2)
