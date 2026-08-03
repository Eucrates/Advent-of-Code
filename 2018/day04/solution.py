import sys
from datetime import datetime
import bisect 

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

date_format = "%Y-%m-%d %H:%M"
records = []
for line in lines:
    line = line.strip("\n")
    #print(line)
    date_string = line.split("[")[1].split("]")[0]
    date_object = datetime.strptime(date_string, date_format)
    record = [int(date_object.timestamp()), date_object, date_string, line.split("] ")[1]]
    bisect.insort(records, record)
    # do something

asleep = {}
i = 0
while i < len(records):
    if records[i][3].startswith("Guard"):
        guard = int(records[i][3].split(" ")[1][1:])
        if guard not in asleep.keys():
            asleep[guard] = [0] * 61
        #print(guard)
        i += 1
        while i < len(records) and not records[i][3].startswith("Guard"):
            #print(records[i+1][1], records[i][1])
            minutes_asleep = (records[i+1][0] - records[i][0]) // 60
            asleep[guard][0] += minutes_asleep
            for m in range(records[i][1].minute, records[i+1][1].minute):
                asleep[guard][m+1] += 1
            i += 2

most_asleep = 0
for guard in asleep.keys():
    if asleep[guard][0] > most_asleep:
        strat1_guard = guard
        most_asleep = asleep[guard][0]

#print(sleepiest_guard, asleep[sleepiest_guard])
strat1_minute = asleep[strat1_guard][1:].index(max(asleep[strat1_guard][1:]))
#print(sleepiest_minute)
part1 = strat1_guard * strat1_minute

print(f"Part 1: {part1}")

strat2_minute = 0
for guard in asleep.keys():
    sleepiest_minute = asleep[guard][1:][asleep[guard][1:].index(max(asleep[guard][1:]))]
    if sleepiest_minute > strat2_minute:
        strat2_minute = sleepiest_minute
        strat2_sleepiest_minute = asleep[guard][1:].index(max(asleep[guard][1:]))
        strat2_guard = guard

part2 = strat2_guard * strat2_sleepiest_minute

print(f"Part 2: {part2}")
                                                    
