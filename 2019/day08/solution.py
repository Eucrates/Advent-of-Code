import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

for line in lines:
    line = line.strip("\n")

#print(len(line)//6//25) #100

# 150 pixels on each of 6 lines on each layer
width = 25
height = 6


#width = 2
#height = 2

num_layers = len(line)//height//width


def get_grid(stream):
    i = 0
    image = []
    while i < len(line):
        layer = []
        for _ in range(height):
            layer.append(stream[i:i+width])
            i += width
        image.append(layer)
    return image

image = get_grid(line)



min_zeros = sys.maxsize
for layer in image:
    zeros = 0
    ones = 0
    twos = 0
    for l in layer:
        zeros += l.count("0")
        ones += l.count("1")
        twos += l.count("2")
        #print(l)

    if zeros < min_zeros:
        min_zeros = zeros
        part1 = ones * twos
    #print()
print(f"Part 1: {part1}")

layer_stream = []
for h in range(height):
    line = []
    for w in range(width):
        pixels = ""
        for l in range(num_layers):
            pixel = image[l][h][w]
            if pixel != "2":
                pixels += pixel
                break
        line.append(pixels)
    layer_stream.append(line)


print("Part 2:")
for line in layer_stream:
    for pixel in line:
        if pixel == "1":
            print("X",end="")
        else:
            print(" ",end="")
    print()
