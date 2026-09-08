import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

rng = sys.argv[1]

low,high = [int(x) for x in rng.split("-")]

def check_pass(i):

    str_pass = str(i)
    
    double = False
    j = 0

    while j < len(str_pass) -1:
        if int(str_pass[j]) > int(str_pass[j+1]):
            return False
        if str_pass[j] == str_pass[j+1]:
            double = True
        j += 1

    if double:
        return True
    return False

def rev_pass(i):

    str_pass = str(i)

    j = 0
    double = False
    while j < len(str_pass) - 1:
        if int(str_pass[j]) > int(str_pass[j+1]):
            return False
        j += 1 

    pos1 = str_pass.count(str_pass[0])
    pos2 = str_pass.count(str_pass[1])
    pos3 = str_pass.count(str_pass[2])
    pos4 = str_pass.count(str_pass[3])
    pos5 = str_pass.count(str_pass[4])

    if pos1 == 2 or pos2 == 2 or pos3 == 2 or pos4 == 2 or pos5 == 2:
        return True

    return False

tot_passwords = 0
rev_passwords = 0
for i in range(low, high+1):
    if check_pass(i):
        tot_passwords += 1
    if rev_pass(i):
        rev_passwords += 1

print(f"Part 1: {tot_passwords}")
print(f"Part 2: {rev_passwords}")
  
