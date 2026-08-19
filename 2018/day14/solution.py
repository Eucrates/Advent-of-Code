import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <input>")
    sys.exit(1)

inp = sys.argv[1]
inpt = int(inp)

recipes = [3,7]

elf1 = 0
elf2 = 1

while len(recipes) < (inpt + 10):
    sum1 = recipes[elf1] + recipes[elf2]
    if sum1 >= 10:
        recipes.append(1)
    recipes.append(sum1 % 10)
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

num = ''.join(str(x) for x in recipes[inpt:inpt+10])
print(f"Part 1: {num}")

# carry on where we left off
end_string = ''.join(str(x) for x in recipes[-len(inp):])
while inp != end_string:
    sum1 = recipes[elf1] + recipes[elf2]
    if sum1 >= 10:
        recipes.append(1)
        end_string += '1'
        end_string = end_string[-len(inp):]
        if inp == end_string:
            part2 = end_string.find(inp) + len(recipes) - len(inp)
            break
    recipes.append(sum1 % 10)
    end_string = end_string + str(sum1 %10)
    end_string = end_string[-len(inp):]
    
    if inp == end_string:
        part2 = end_string.find(inp) + len(recipes) - len(inp)
        break
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(f"Part 2: {part2}")






