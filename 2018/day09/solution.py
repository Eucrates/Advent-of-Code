import sys
from collections import deque

if len(sys.argv) != 1:
    print("Usage: solution.py")
    sys.exit(1)

def game(num_players, last_marble_value):
    circle = deque([0])
    players_scores = {}

    for current in range(1, last_marble_value + 1):
        if current % 23 == 0:
            circle.rotate(7)
            if current % num_players not in players_scores.keys():
                players_scores[current % num_players] = current + circle.pop()
            else:
                players_scores[current % num_players] += current + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(current)

    return max(players_scores.values())

# very slow:
'''
circle = deque([0])
players_scores = {}
current = 0

for i in range(1, last_marble_value + 1):
    player = i % num_players

    if i % 23 == 0:
        #print("mod 23: keep, remove, reset current")
        if player not in players_marbles.keys():
            players_marbles[player] = i
        else:
            players_marbles[player] += i
        removed = circle[(circle.index(current) - 7) % len(circle)]
        #print(removed)
        players_marbles[player] += removed
        idx = circle.index(removed)
        circle.remove(removed)
        current = circle[idx]
        #print(circle[(circle.index(current) - 7) % len(circle)]) 
    else:
        if len(circle) == 1:
            circle.append(i)
        else:
            idx = circle.index(current)
            left = (idx + 1) % len(circle)
            right = (idx + 2) % len(circle)
            circle.insert(left+1,i)
        current = i

    #print(f"[{player}] ({current}), {circle}")
max_key, part1 = max(players_marbles.items(), key=lambda item: item[1])
'''

print(f"Part 1: {game(459, 71320)}")
print(f"Part 2: {game(459, 7132000)}")

