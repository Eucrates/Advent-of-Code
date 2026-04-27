import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <input>")
    sys.exit(1)

num = int(sys.argv[1])

buff = [0]
index = 0
for i in range(1,2018):
    index = (index + num) % len(buff) + 1
    buff.insert(index,i)
part1 = buff[buff.index(2017)+1]

print(f"Part 1: {part1}")


# inserting is very time consuming; instead keep track of the length of
# the buffer and the next number to be inserted whenever it places a 
# value directly after 0 (index 1) because 0 is always the 0th index of
# the buffer  
index = 0
length = 1
for i in range(50000000):
    index = (index + num) % length + 1
    length += 1
    insertion = i + 1
    if index == 1:
        next_num = insertion

print(f"Part 2: {next_num}")
