import sys

if len(sys.argv) < 3:
    print("Usage: solution.py <filename> <totalTime>")
    sys.exit(1)

file = sys.argv[1]
totalTime = int(sys.argv[2])
with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


winner = 0
leaderboard = {}
for line in lines:
    line = line.strip("\n")
    line = line.split(" ")
    name = line[0]
    speed = int(line[3])
    time = int(line[6])
    rest = int(line[13])
    tot = totalTime
    distance = 0
                      # [speed, time, total distance, poins, flying]
    leaderboard[name] = [speed,time,rest,0,0,True]
    flying = True

    # check that there is enough time left for complete flight
    # or rest; break if not
    # if reindeer is flying, compute distance, subtract time 
    # flying from total time. When flying time is up, flying 
    # = False
    # check that there is a full rest break left, else break
    # subract rest time from total time,
    # flying = True
    
    while True:
        if flying == True:
            if tot - time >= 0:
                distance += speed*time
                flying = False
                tot -= time
            else:
                break
        else:
            if tot - rest >= 0:
                tot -= rest
                flying = True
            else:
                break
    
    # if the reindeer is flying at the end, compute the 
    # distance by km/second left
    if flying == True:
        distance += tot * speed
    if distance > winner:
        winner = distance
print("Part1:",winner)

leaderDist = 0                      # distance of current leader
for second in range(1,totalTime+1):
    for reindeer in leaderboard.keys():
        speed = leaderboard[reindeer][0]
        time = leaderboard[reindeer][1]
        rest = leaderboard[reindeer][2]
        if leaderboard[reindeer][5] == True:   # if the reindeer is flying,       
            leaderboard[reindeer][3] += speed  # add the km/s to the total distance
        
        # reindeer stops flying when second % total rest and flight time is between flight time and        # rest time
        if second % (time + rest) <= (rest + time) and second % (rest + time) >= time:
            leaderboard[reindeer][5] = False           
        # reindeer starts flying if second % total time is less than flight time
        if second % (time + rest) < time:
            leaderboard[reindeer][5] = True

    # get the current leader distance
    for reindeer in leaderboard.keys():
        if leaderboard[reindeer][3] > leaderDist:
            leaderDist = leaderboard[reindeer][3]

    # any reindeer who is at the leader distance gets a point
    for reindeer in leaderboard.keys():
        if leaderboard[reindeer][3] == leaderDist:
            leaderboard[reindeer][4] += 1

# find the higest point value
winner = 0
for reindeer in leaderboard.keys():
    if leaderboard[reindeer][4] > winner:
        winner = leaderboard[reindeer][4]

print("Part2:", winner)


