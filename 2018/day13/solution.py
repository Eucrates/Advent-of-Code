import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

def print_grid(grid):
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            coord = next((cart[0] for cart in carts if cart[1] == (r,c)), None)
            if coord:
                print(coord,end='')
            else:
                print(col,end='')
        print()
    print()

def move_carts(carts):
    carts = sorted(carts, key=lambda x: x[1])
    coords = set()
    crashes = []
    i = 0
    while i < len(carts):
        cart = carts[i]
        coord = cart[1]
        match cart[0]:
            case '^':
                new_coord = (coord[0]-1, coord[1])
                next_track = grid[new_coord[0]][new_coord[1]]
                if next_track == '\\':
                    cart[0] = '<'
                elif next_track == '/':
                    cart[0] = '>'
                elif next_track == '+':
                    match cart[2]:
                        case 'left':
                            cart[0] = '<'
                        case 'straight':
                            pass
                        case "right":
                            cart[0] = '>'
                    cart[2] = new_dir[cart[2]]
                pass

            case 'v':
                new_coord = (coord[0]+1, coord[1])
                next_track = grid[new_coord[0]][new_coord[1]]
                if next_track == '\\':
                    cart[0] = '>'
                elif next_track == '/':
                    cart[0] = '<'
                elif next_track == '+':
                    match cart[2]:
                        case 'left':
                            cart[0] = '>'
                        case 'straight':
                            pass
                        case "right":
                            cart[0] = '<'
                    cart[2] = new_dir[cart[2]]
                pass

            case '>':
                new_coord = (coord[0], coord[1]+1)
                next_track = grid[new_coord[0]][new_coord[1]]
                if next_track == '\\':
                    cart[0] = 'v'
                elif next_track == '/':
                    cart[0] = '^'
                elif next_track == '+':
                    match cart[2]:
                        case 'left':
                            cart[0] = '^'
                        case 'straight':
                            pass
                        case "right":
                            cart[0] = 'v'
                    cart[2] = new_dir[cart[2]]
                pass

            case '<':
                new_coord = (coord[0], coord[1]-1)
                next_track = grid[new_coord[0]][new_coord[1]]
                if next_track == '\\':
                    cart[0] = '^'
                elif next_track == '/':
                    cart[0] = 'v'
                elif next_track == '+':
                    match cart[2]:
                        case 'left':
                            cart[0] = 'v'
                        case 'straight':
                            pass
                        case "right":
                            cart[0] = '^'
                    cart[2] = new_dir[cart[2]]
                pass

            case _:
                print(cart[0])
                print("Unknown cart orientation")
         
        cart[1] = new_coord
        
        # check for crashes after each cart moves
        crashed = None
        for j, c in enumerate(carts):
            if j != i and c[1] == new_coord:
                crashed = j
                break

        # remove crasehed carts
        if crashed is not None:
            crashes.append(new_coord)

            for index in sorted([i, crashed], reverse=True):
                carts.pop(index)
            
            # if the crashed cart is before i, reduce i
            if crashed < i:
                i -= 1

            continue

        i += 1 

    return carts,crashes



grid = []
carts = []
new_dir = {'left': 'straight', 'straight': 'right', 'right':'left'}

for r, line in enumerate(lines):
    line = line.strip("\n")
    row = []
    for c, x in enumerate(line):
        curr_coord = (r,c)
        if (x == '>' or x == '<' or x == 'v' or x == '^'):
            carts.append([x, (r,c), "left"])

        row.append(x)
    grid.append(row)

orig_carts = []
for cart in carts:
    orig_carts.append([cart[0],cart[1],cart[2]])

# Correct base grid
for cart in carts:
    r,c = cart[1]
    if (cart[0] == '<') or (cart[0] == '>'):
        grid[r][c] = '-'
    elif (cart[0] == 'v') or (cart[0] == '^'):
        grid[r][c] = '|'



#print_grid(grid)
while True:
    carts,crashes = move_carts(carts)
    if len(crashes) > 0:
        break
#    print_grid(grid)
#    input()


print(f"Part 1: {crashes[0][1]},{crashes[0][0]}")

carts = [cart.copy() for cart in orig_carts]
#print_grid(grid)
while len(carts) > 1:
    carts, crashes = move_carts(carts)
    if len(carts) == 0:
        print("All carts crashed")
        exit()
#    print_grid(grid)
#    input()

#print_grid(grid)
print(f"Part 2: {carts[0][1][1]},{carts[0][1][0]}")
