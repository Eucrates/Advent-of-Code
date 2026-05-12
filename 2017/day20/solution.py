import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


particles = {}
for i,line in enumerate(lines):
    line = line.strip("\n")
    p,v,a = line.split(", ")
    p = [int(x) for x in p.strip("p=<").strip(">").strip().split(",")]
    v = [int(x) for x in v.strip("v=<").strip(">").strip().split(",")]
    a = [int(x) for x in a.strip("a=<").strip(">").strip().split(",")]
    
    particles[i] = [p,v,a,[abs(p[0]) + abs(p[1]) + abs(p[2])],0]

particles2 = {}
for key in particles.keys():
    particles2[key] = particles[key]

# applies position transformation and gets an average distance from 0
# for each particle after each move
def tic(particle):
    
    p0,v0,a,m0,_= particle
    p1 = [p for p in p0]
    v1 = [v for v in v0]

    v1[0] += a[0]
    v1[1] += a[1]
    v1[2] += a[2]
    p1[0] += v1[0]
    p1[1] += v1[1]
    p1[2] += v1[2]

    m0.append(abs(p1[0]) + abs(p1[1]) + abs(p1[2])) 
    av = sum(m0) / len(m0)
    return p1,v1,a,m0,av

# runs 1000 tics and averages the distance of each particle from 0
# probably a more efficient / definitive way to determine when
# particles have reached their average distance
for i in range(1000):        
    for key in  particles.keys():
        particles[key] = tic(particles[key])

smallest = ["x",max([x[4] for x in particles.values()])]

for i in range(len(particles.keys())):
    if particles[i][4] < smallest[1]:
        smallest = [i,particles[i][4]]

print(f"Part 1: {smallest[0]}")


# removes all instances of particles occupying the same coordinates
def smash(p):
    for i in range(len(p.keys())):
        if p.get(i):
            smasher = p[i][0]
            for j in range(i+1,len(p.keys())-1):
                if p.get(j):
                    if smasher == p[j][0]:
                        p.pop(i,None)
                        p.pop(j,None)
    return p

# same note as above; probably a better way to determine when 
# all particles have smashed, but it worked
for h in range(1000):
    for i in range(len(particles2.keys())):

        if particles2.get(i):
            particles2[i] = tic(particles2[i])
    particles2 = smash(particles2)


print(f"Part 2: {len(particles2.keys())}")



