# https://pastebin.com/JJffnFrW for nudges using lists for column/row above below left and right

with open ("input.txt") as f:
    lines = f.readlines();

def getabove(forest,r,c):
    
    col =  []
    for i in range(0,r):
        col.append(forest[i][c])
    return col[::-1]

def getbelow(forest,r,c):

    col = []
    for i in range(r+1,len(forest)):
        col.append(forest[i][c])
    return col

def getright(forest,r,c):
    
    row = []
    for i in range(c+ 1,len(forest[0])):
        row.append(forest[r][i])
    return row

def getleft(forest,r,c):
    
    row = []
    for i in range (0,c):
        row.append(forest[r][i])
    return row[::-1]

def part1(forest):

    forest_length = len(forest)
    forest_width = len(forest[0])


    perimiter = len(forest[0]) *2 + len(forest) * 2 - 4
    visible = []
    for r in range (1,forest_length - 1):
        for c in range (1,forest_width - 1):
            tree_height = forest[r][c]
            tree_num = r * forest_length + c

            # tree visible from above
            up = getabove(forest,r,c)
            if tree_height > max(up):
                visible.append(tree_num)

            # tree visible from below
            down = getbelow(forest,r,c)
            if tree_height > max(down) and tree_num not in visible:
                visible.append(tree_num)
        
            # tree visible from right
            right = getright(forest,r,c)
            if tree_height > max(right) and tree_num not in visible:
                visible.append(tree_num)

            # tree visible from left
            left = getleft(forest,r,c)
            if tree_height > max(left) and tree_num not in visible:
                visible.append(tree_num)
    
    print(perimiter + len(visible))

def getview(l,tree_height):
    view = 0
    for tree in l:
        if tree >= tree_height:
            view +=1
            break
        else:
            view +=1


    #print ("list = ",l,"height = ",tree_height,"view = ",view)
    return view

def part2(forest):
    
    forest_length = len(forest)
    forest_width = len(forest[0])

    sightline = 0
    for r in range (forest_length):
        for c in range (forest_width):
            tree_height = forest[r][c]
            tree_num = r * forest_length + c
            up = getabove(forest,r,c)
            down = getbelow(forest,r,c)
            right = getright(forest,r,c)
            left = getleft(forest,r,c)
            up = getview(up,tree_height)
            down = getview(down,tree_height)
            right = getview(right,tree_height)
            left = getview(left,tree_height)
    #        print (r,c,tree_num,sightline)
    #        for row in forest:
    #            print (row)
    #        print("r, c, tree_num, sightline, up, down, left, right")
    #        print(r,c,tree_num, up*down*left*right, up, down, left, right)
            if up*down*left*right > sightline:
                sightline = up*down*left*right
    #        print (r,c,tree_num,sightline)            
 
        #print (r,c,tree_num,up*down*left*right)
    print(sightline)

forest = []
row = []

for line in lines:
    line = line.strip("\n")
    for tree in line:
        row.append(int(tree))
    forest.append(row)
    row = []

#for row in forest:
#    print(row)


part1(forest)
part2(forest)


