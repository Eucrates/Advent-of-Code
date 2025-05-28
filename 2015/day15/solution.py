import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

ingredients = []
for line in lines:
    line = line.strip("\n")
    # do something
    # print(line)
    line = line.replace(",","")
    line = line.split(" ")
    if "-" in line[2]:
        capacity = -int(line[2][1:])
    else:
        capacity = int(line[2])
    if "-" in line[4]:
        durability = -int(line[4][1:])
    else:
        durability = int(line[4])
    if "-" in line[6]:
        flavor = -int(line[6][1:])
    else:
        flavor = int(line[6])
    if "-" in line[8]:
        texture = -int(line[8][1:])
    else:
        texture = int(line[8])
    if "-" in line[10]:
        calories = -int(line[10][1:])
    else:
        calories = int(line[10])

    ingredients.append([capacity, durability, flavor, texture, calories])

def part1():
    maxScore = 0
    for i in range(101):
        if i == 100:
            capacity   = ingredients[0][0] * i
            durability = ingredients[0][1] * i
            flavor     = ingredients[0][2] * i
            texture    = ingredients[0][3] * i

            if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                score = 0
            else:
                score = capacity * durability * flavor * texture
            if score > maxScore:
                maxScore = score
        else:
            for j in range(101):
                if i + j == 100:
                    capacity   = ingredients[0][0] * i + ingredients[1][0] * j
                    durability = ingredients[0][1] * i + ingredients[1][1] * j
                    flavor     = ingredients[0][2] * i + ingredients[1][2] * j
                    texture    = ingredients[0][3] * i + ingredients[1][3] * j

                    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                        score = 0
                    else:
                        score = capacity * durability * flavor * texture
                    if score > maxScore:
                        maxScore = score
                else:
                    for k in range(101):
                        if i + j + k == 100:
                                capacity   = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k
                                durability = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k
                                flavor     = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k
                                texture    = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k
                                if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                                    score = 0
                                else:
                                    score= capacity * durability * flavor * texture
                                if score > maxScore:
                                    maxScore = score
                        else:
                            for l in range(101):
                                if i + j + k + l ==100:
                                    capacity   = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l
                                    durability = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l
                                    flavor     = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l
                                    texture    = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l
                                    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                                        score = 0
                                    else:
                                        score = capacity * durability * flavor * texture
                                    if score > maxScore:
                                        maxScore = score

    print("Part1:",maxScore)


def part2():
    maxScore = 0
    for i in range(101):
        if i == 100:
            capacity   = ingredients[0][0] * i
            durability = ingredients[0][1] * i
            flavor     = ingredients[0][2] * i
            texture    = ingredients[0][3] * i
            calories = ingredients[0][4] * i
            if calories == 500:
                if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                    score = 0
                else:
                    score = capacity * durability * flavor * texture
                if score > maxScore:
                    maxScore = score
        else:
            for j in range(101):
                if i + j == 100:
                    capacity   = ingredients[0][0] * i + ingredients[1][0] * j
                    durability = ingredients[0][1] * i + ingredients[1][1] * j
                    flavor     = ingredients[0][2] * i + ingredients[1][2] * j
                    texture    = ingredients[0][3] * i + ingredients[1][3] * j
                    calories   = ingredients[0][4] * i + ingredients[1][4] * j
                    if calories == 500:
                        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                            score = 0
                        else:
                            score = capacity * durability * flavor * texture
                        if score > maxScore:
                            maxScore = score
                else:
                    for k in range(101):
                        if i + j + k == 100:
                                capacity   = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k
                                durability = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k
                                flavor     = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k
                                texture    = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k
                                calories   = ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k
                                if calories == 500:
                                    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                                        score = 0
                                    else:
                                        score= capacity * durability * flavor * texture
                                    if score > maxScore:
                                        maxScore = score
                        else:
                            for l in range(101):
                                if i + j + k + l ==100:
                                    capacity   = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l
                                    durability = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l
                                    flavor     = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l
                                    texture    = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l
                                    calories   = ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l
                                    if calories == 500:
                                        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                                            score = 0
                                        else:
                                            score = capacity * durability * flavor * texture
                                        if score > maxScore:
                                            maxScore = score

    print("Part2:",maxScore)

part1()
part2()
