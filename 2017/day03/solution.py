import sys
from math import ceil,sqrt

if len(sys.argv) < 2:
    print("Usage: solution.py square#")
    sys.exit(1)

num = int(sys.argv[1])

if num == 1:    # edge case; otherwise ring won't be created; also range below can't decrement by 0
    part1 = 0
else:
    sqrrt = 1
    i = 1
    rings = 1
    prevRing = [1]
    while i < num:
        sqr = sqrrt**2
        ringsize = sqr - (sqrrt-2)**2
        ring = [j for j in range(i+1,i+ringsize+1)]
        if num in ring:
            break
        rings += 1
        i += ringsize
        sqrrt += 2

    for j in range(ring[-1],ring[-1]-len(ring),-sqrrt+1):
        side = [k for k in range(j-sqrrt+1,j+1)]  
        
        # lowest side will have previous ring's bottom corner square in it instead of current ring's but this should not matter because we're only looking to see if the number is in the side; distance from number to the center of the side will be the same
        if num in side:
            # distance to center of side + the number of previous rings
            part1 = abs(num - side[ceil(len(side)//2)]) + rings - 1
            break

print(f"Part 1: {part1}")

# Part 2 coordinate generator adapted from ihf's answer here:
# https://math.stackexchange.com/questions/163080/on-a-two-dimensional-grid-is-there-a-formula-i-can-use-to-spiral-coordinates-in
def spiral(n):
        k=int(ceil((sqrt(n)-1)/2))
        t=int(2*k+1)
        m=int(t**2)
        t=int(t-1)
        if n>=m-t: return k-(m-n),-k
        else: m=m-t
        if n>=m-t: return -k,-k+(m-n)
        else: m=m-t
        if n>=m-t: return -k+(m-n),k 
        else: return k,k-(m-n-t)

coordVals = {}
coordVals[(0,0)] = 1

i = 1
for i in range(1,num):
    square = 0
    x,y = spiral(i)
    for i in [-1,0,1]:
        for j in [-1,0,1]:
           square += coordVals.get((x+i, y+j),0) 

    coordVals[(x,y)] = square
    if square > num:
        break

print(f"Part 2: {square}")

