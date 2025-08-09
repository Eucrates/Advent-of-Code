import sys
import logging
from random import randint as rand

if len(sys.argv) != 6:
    print("Usage: solution.py <player_HP> <player_mana> <boss_HP> <boss_damage> <DEBUG,INFO>")
    sys.exit(1)

player_HP = int(sys.argv[1])
player_mana = int(sys.argv[2])
boss_HP = int(sys.argv[3])
boss_damage = int(sys.argv[4])
debugLevel = sys.argv[5]


match debugLevel:
    case "DEBUG":
        logging.basicConfig(level=logging.DEBUG, format = '%(message)s')
    case "INFO":
        logging.basicConfig(level=logging.INFO, format = '%(message)s')
    case _:
        print("Debugging level not understood")
        exit(1)

logging.StreamHandler.terminator = ""

spells = [ # Name               cost    damage, healing, armor, mana,  turns
            ["Magic Missile",   53,     4,      0,       0,     0,     0],
            ["Drain",           73,     2,      2,       0,     0,     0],
            ["Shield",          113,    0,      0,       7,     0,     0],
            ["Poison",          173,    3,      0,       0,     0,     0],
            ["Recharge",        229,    0,      0,       0,   101,     0]
          ]

def spell_upkeep():

    global player_mana
    global boss_HP
    global player_armor
    ret = False
    for i in range (2,5):
        if spells[i][6] > 0:
            match spells[i][0]:
                case "Shield":
                    spells[i][6] -= 1
                    logging.debug(f"'s timer is now {spells[i][6]}.\n")
                    if spells[i][6] == 0:
                        logging.debug("Shield wears off, decreasing armor by 7.\n")
                        player_armor = 0
                case "Poison":
                    spells[i][6] -= 1
                    logging.debug(f" deals {spells[i][2]} damage")
                    boss_HP -= 3
                    if boss_HP <= 0:
                        logging.debug(f". This kills the boss and the player wins.\n")
                        ret = True
                    logging.debug(f"; its timer is now {spells[i][6]}.\n")
                    if spells[i][6] == 0:
                        logging.debug(f"{spells[i][0]} wears off.\n")
                case "Recharge":
                    spells[i][6] -= 1
                    logging.debug(f" provides {spells[i][5]} mana; its timer is now {spells[i][6]}.\n")
                    player_mana += 101
                    if spells[i][6] == 0:
                        logging.debug(f"{spells[i][0]} wears off.\n")
    return ret
def print_stats():
    logging.debug(f" - Player has {player_HP} hit points, {player_armor} armor, {player_mana} mana\n")
    logging.debug(f" - Boss has {boss_HP} hit points\n")

def run_sim(sequence,part):
    global boss_HP
    global player_HP
    global player_armor
    global player_mana
    global mana_spent

    mana_spent = 0
    for spell in sequence:
        logging.debug(f"\n-- Player Turn --\n")
        if part == 2:
            player_HP -= 1
            if player_HP <= 0:
                return 0xFFFFFFFF # a large number
        print_stats()
        if spell_upkeep():
            return mana_spent
        # not enough mana, player loses
        if spells[spell][1] > player_mana:    # Not enough mana to cast, return 
            logging.debug(f"Player attempts to cast {spells[spell][0]} for {spells[spell][1]}; not enough mana, player loses\n")
            return 0xFFFFFFFF  
        logging.debug(f"Player casts {spells[spell][0]}")
        mana_spent += spells[spell][1]
        player_mana -= spells[spell][1]
        match spells[spell][0]:
            case "Magic Missile":
                logging.debug(f", dealing {spells[spell][2]} damage.\n")
                boss_HP -= 4
            case "Drain":
                logging.debug(f", dealing {spells[spell][2]} damage, and healing {spells[spell][3]} hit points.\n")
                boss_HP -= 2
                player_HP += 2
            case "Shield":
                logging.debug(f", increasing armor by 7.\n")
                player_armor = 7
                spells[spell][6] = 6
            case "Poison":
                logging.debug(f".\n")
                spells[spell][6] = 6
            case "Recharge":
                spells[spell][6] = 5
                logging.debug(f".\n")
        
        if boss_HP <= 0:
            return mana_spent
        logging.debug(f"\n-- Boss turn --\n")
        print_stats()        
        if spell_upkeep():
            return mana_spent
        boss_attack = boss_damage - player_armor
        if boss_attack <= 0:
            boss_attack = 1
        logging.debug(f"Boss attacks for {boss_attack} damage!\n")
        player_HP -= boss_attack
        if player_HP <= 0:
            return 0xFFFFFFFF
    return 0xFFFFFFFF

my_list = [0, 1, 2, 3, 4]
n = 20

for part in range (1,3):
    min_mana = 0xFFFFFFFF
    for j in range(100000):
        for spell in spells:
            spell[6] = 0
        player_HP = int(sys.argv[1])
        player_armor = 0
        player_mana = int(sys.argv[2])
        boss_HP = int(sys.argv[3])
        boss_damage = int(sys.argv[4])
        mana_spent = 0

        # 20 random spells; could not get itertools to produce a proper list 
        # all_combos = list(itertools.combinations_with_replacement([0, 1, 2, 3, 4], 20 ))
        sequence = [rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4), rand(0,4)]

        total_mana = run_sim(sequence,part) 
        if total_mana < min_mana:
            min_mana = total_mana
    if part == 1:
        print (f"Part 1: {min_mana}")
    else:
        print (f"Part 2: {min_mana}")
    
