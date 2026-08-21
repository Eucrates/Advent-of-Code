# adventofcode.com 2018 day 15
# Vibe coded with ChatGPT

import sys
from collections import deque

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def fresh_game():
    grid = []
    units = []

    for i, line in enumerate(lines):
        row = []

        for j, r in enumerate(line.strip("\n")):
            row.append(r)

            if r == "G":
                units.append(["G", (i, j), 200])

            elif r == "E":
                units.append(["E", (i, j), 200])

        grid.append(row)

    return grid, units


def print_grid(g):

    for row in g:
        print(''.join(row))

def get_adjacent(coord):
    # assumes walls around game field; no need to check for edge values
    adjacent = []

    up =    (coord[0]-1, coord[1])
    left =  (coord[0], coord[1]-1)
    right = (coord[0], coord[1]+1)
    down =  (coord[0]+1, coord[1])

    adjacent.append(up)
    adjacent.append(left)
    adjacent.append(right)
    adjacent.append(down)

    return adjacent

def attack(ts,AT):

    victim = min(ts, key=lambda x: (x[2], x[1]))

    victim[2] -= AT

    return ts
    
def update_grid(g,ts):

    for t in ts:
        if t[2] <= 0:
            r,c = t[1]
            g[r][c] = '.'
    return g

def bfs(u,g):
    start = u[1]
    queue = deque([start])
    dist = {start: 0}

    directions = [
            (-1,0),
            (0,-1),
            (0,1),
            (1,0)
            ]

    while queue:
        r,c = queue.popleft()

        for dr,dc in directions:
            nxt = (r+dr, c+dc)

            if nxt in dist:
                continue

            nr,nc = nxt
            
            if g[nr][nc] != '.':
                continue


            dist[nxt] = dist[(r,c)] + 1 
            queue.append(nxt)

    return dist


def move_unit(u,us,g):
    
    targets = set()

    enemies = [e for e in us if e[0] != u[0] and e[2] > 0]

    for enemy in enemies:
        for square in get_adjacent(enemy[1]):
            r,c = square
            if g[r][c] == '.':
                targets.add(square)
    
    if not targets: 
        return None

    dist_from_start = bfs(u,g)

    reachable = [ t for t in targets if t in dist_from_start ]

    if not reachable:
        return None

    target = min(reachable, key=lambda x: (dist_from_start[x], x))
    
    dist_from_target = bfs(["", target, 0],g)

    candidates = []

    target_distance = dist_from_start[target]

    for step in get_adjacent(u[1]):
        r,c = step

        if g[r][c] != '.':
            continue
        if step not in dist_from_target:
            continue
        if dist_from_target[step] == target_distance - 1:
            candidates.append(step)

    if not candidates:
        return None


    return min(candidates)

def play_game(grid,units,e_AT,g_AT):
    rounds = 0
    while True:
        #print_grid(grid)

        battle_end = False
        units = sorted(units, key=lambda unit: unit[1])
        # select unit
        for i,unit in enumerate(units):

            if unit[2] <= 0:
                continue
            # calculate targets
            adjacent = get_adjacent(unit[1])
            enemies = [e for e in units if e[0] != unit[0] and e[2] > 0]         
            if not enemies:
                battle_end = True
                break
            targets = [t for t in units if t[0] != unit[0] and t[2] > 0 and t[1] in adjacent]

            if len(targets) > 0:
                #print(targets)
                AT = g_AT if unit[0] == 'G' else e_AT
                targets = attack(targets, AT)
                if any(t[2] <= 0 for t in targets):
                    grid = update_grid(grid, targets)
            else:
                # move
                move = move_unit(unit,units,grid)
                old_pos = unit[1]

                if move is not None:
                    grid[old_pos[0]][old_pos[1]] = '.'
                    unit[1] = move
                    units[i] = unit
                    grid[move[0]][move[1]] = unit[0]

                    # calculate targets
                    adjacent = get_adjacent(unit[1])
                    targets = [t for t in units if t[0] != unit[0] and t[2] > 0 and t[1] in adjacent]
                    if len(targets) > 0:
                        AT = g_AT if unit[0] == 'G' else e_AT
                        targets = attack(targets, AT)
                        if any(t[2] <= 0 for t in targets):
                            grid = update_grid(grid, targets)


                
                #battle_end = True
                #break
        # remove dead units
        units = [u for u in units if u[2] > 0]

        if battle_end:
            break
    
        rounds += 1
    
    return rounds,sum(u[2] for u in units),units    

HP = 200
elf_AT = 3
goblin_AT = 3

grid, units = fresh_game()
#print_grid(grid)
rounds,remaining_HP,units = play_game(grid,units,elf_AT,goblin_AT)
print(f"Part 1: {rounds * remaining_HP}")


min_AT = 4
best_attack = None
best_rounds = None
best_hp = None

grid,units = fresh_game()
elf_count = sum(1 for u in units if u[0] == 'E')

while True:

    grid,units = fresh_game()
    
    rounds, remaining_HP,units = play_game(grid, units, elf_AT,goblin_AT)

    if sum(1 for u in units if u[0] == 'E') == elf_count:
        
       # print(
       #     "SUCCESS:",
       #     "AT =", elf_AT,
       #     "rounds =", rounds,
       #     "hp =", remaining_HP,
       #     "score =", rounds * remaining_HP
       #     )
       # input()
        #best_attack = elf_AT
        best_rounds = rounds
        best_hp = remaining_HP
        #max_AT = elf_AT - 1
        break
    elf_AT += 1
    #print(min_AT,max_AT)
print(f"Part 2: {best_rounds *  best_hp}")

