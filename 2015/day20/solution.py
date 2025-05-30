import sys
from sympy import divisors

# get and validate input
if len(sys.argv) != 2:
    print("Usage: solution.py <input>")

try:
    totalPresents = int(sys.argv[1])
except Exception as e:
    print(e)
    exit(1)

# house 1 gets 1 * 10 presents
# house 2 gets 1 * 10 + 2 * 10 presents
# house 3 gets 1 * 10 + 3 * 10 presents
# house 4 gets 1 * 10 + 2 * 10 + 4 * 10 presents
# it's the sum of the divisors * 10
house = 1
while True:
    pres = sum(divisors(house)) * 10
    if pres >= totalPresents:
        break
    house += 1

print(f"Part1: {house}")

house = 1
while True:
    pres = 0
    # each elf visits a max of 50 houses
    for visit in range(1,51):
        if house % visit == 0:               # if the visit number is a mod of the house number
            pres += (house // visit) * 11    # presents are the divisor of that visit * 11
    if pres >= totalPresents:
        break
    house += 1

print(f"Part2: {house}")
