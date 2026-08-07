# Advent of code 2018 day 7
# I relied heavily on various code from
# https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/


import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

queue = {}
rev_queue = {}
alphabet = set()
steps = []

for line in lines:
    first = line[5]
    second = line[36]
    steps.append((first,second))

    alphabet.add(first)
    alphabet.add(second)

    if first not in queue.keys():
        queue[first] = [second]
    else:
        queue[first].append(second)
        queue[first].sort()

    if second not in rev_queue.keys():
        rev_queue[second] = [first]
    else:
        rev_queue[second].append(first)
        rev_queue[second].sort()


for a in alphabet:
    if a not in queue.keys():
        queue[a] = []
    
open_steps = sorted(set(queue) - set(rev_queue),reverse=True)
part1 = ''

while open_steps:
    next_step = open_steps.pop()
    part1 += next_step
    for dependant in queue[next_step]:
        if all(depend in part1 for depend in rev_queue[dependant]) and dependant not in open_steps:
            open_steps.append(dependant)
    open_steps.sort(reverse=True)

print(f"Part 1: {part1}")


helpers = 5
time_per_step = 60
workers = [{'time':0, 'step':None} for _ in range(helpers)]
seconds = 0

lines = steps
while alphabet or any(worker['time'] > 0 for worker in workers):
    steps = [s for s in alphabet if all (b!=s for (_,b) in lines)]

    for i in range(helpers):
        workers[i]['time'] = max(workers[i]['time'] - 1, 0)
        if workers[i]['time'] == 0:
            if workers[i]['step'] is not None:
                lines = [(a, b) for (a, b) in lines if a != workers[i]['step']]
            if steps:
                step = steps.pop()[0]
                workers[i]['time'] = time_per_step + ord(step) - ord('A')
                workers[i]['step'] = step
                alphabet.remove(step)
    seconds += 1

print(f"Part 2: {seconds}")
