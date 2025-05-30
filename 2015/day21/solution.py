import sys
import itertools

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

weapons = []
armors = []
rings = []

# sample.txt is the list of shop items, named so to adhere to .gitignore policies
with open ("sample.txt") as f:
    f.readline()
    for i in range(5):
        weapons.append(f.readline().split()[1:])
    f.readline()
    f.readline()
    armors.append(["0","0","0"])  # allows for 0 armor
    for i in range(5):
        armors.append(f.readline().split()[1:])
    f.readline()
    f.readline()
    rings.append(["0","0","0"])  # allows for 0 rings*
    for i in range(6):
        rings.append(f.readline().split()[2:])

ringpairs = list(itertools.combinations(rings,2))

ringpairs.append((['0', '0', '0'], ['0', '0', '0']))  # *itertools.combinations doesn't allow duplicates and a player can have 0-2 rings

with open (file) as f:
    boss_hitpoints = int(f.readline().split()[2])
    boss_damage = int(f.readline().split()[1])
    boss_armor = int(f.readline().split()[1])

bossStats = [boss_hitpoints, boss_damage, boss_armor]

player_hitpoints = 100
player_damage = 0
player_armor = 0

def buyEquipment():
    statistics = []
    for weapon in weapons:
        cost = int(weapon[0])
        damage = int(weapon[1])
        for armor in armors:
            cost += int(armor[0])
            defense = int(armor[2])
            for ringpair in ringpairs:
                cost += int(ringpair[0][0]) + int(ringpair[1][0])
                damage += int(ringpair[0][1]) + int(ringpair[1][1])
                defense += int(ringpair[0][2]) + int(ringpair[1][2])
                statistics.append([cost,damage,defense])
                defense -= (int(ringpair[0][2]) + int(ringpair[1][2]))
                cost -= (int(ringpair[0][0]) + int(ringpair[1][0]))
                damage -= (int(ringpair[0][1]) + int(ringpair[1][1]))
            cost -= int(armor[0])
        
    return statistics

def playGame(stat):
    playerStats = [player_hitpoints, stat[1],stat[2]]
    bossStats = [boss_hitpoints, boss_damage, boss_armor]

    while True:
        playerAttack = playerStats[1] - bossStats[2]
        if playerAttack <= 0: playerAttack = 1
        bossStats[0] = bossStats[0] - playerAttack
        if bossStats[0] <= 0: return True

        bossAttack = bossStats[1] - playerStats[2]
        if bossAttack <= 0: bossAttack = 1
        playerStats[0] = playerStats[0] - bossAttack
        if playerStats[0] <= 0: return False

    return False

stats = buyEquipment()
winCost = []
loseCost = []
for stat in stats:
    win = playGame(stat)
    if win:
        winCost.append(stat[0])
    else:
        loseCost.append(stat[0])
print(f"Part1: {min(winCost)}")
print(f"Part2: {max(loseCost)}")



