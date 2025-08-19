import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def top5(freq):
    checkOrder = "abcdefghijklmnopqrstuvwxyz"

    # turn dictionary into list of lists
    fList = []
    for c in checkOrder:
        if c in freq.keys():
            fList.append([c, freq[c]])
    
    # sort by key then value
    sortedList = sorted(fList, key=lambda x: (x[0], x[1]))
    
    # sorts reverse alphabetically
    sortedList = sortedList[::-1]
    # https://www.geeksforgeeks.org/python/python-sort-list-according-second-element-sublist/
    # sorts by frequencey of letter
    n = len(sortedList)
    for i in range(n):
        for j in range(0, n-i-1):
            if sortedList[j][1] > sortedList[j+1][1]:
                sortedList[j], sortedList[j+1] = sortedList[j+1], sortedList[j]

    # reverses list
    sortedList = sortedList[::-1]
    
    # gets top 5 frequency letters
    checksum = sortedList[0][0] + sortedList[1][0] + sortedList[2][0] + sortedList[3][0] + sortedList[4][0]
    return checksum

def decryptName(encryptedName, sectorID):
 
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    decryptedName = ""
    for e in encryptedName:
        if e == "-":
            d = " "
        else:
            # get index of letter to decrypt
            # rotate that by the sectorID
            # mod 26 to get the position in the alphabet of the decrypted letter
            i = alphabet.index(e)
            d = alphabet[(i + sectorID) % 26]
        decryptedName += d

    return decryptedName

idSum = 0
for line in lines:
    line = line.strip("\n")

    checksum = line.split("[")[1].split("]")[0]
    encryptedName = "-".join(line.split("[")[0].split("-")[:-1])
    roomname = "".join(line.split("[")[0].split("-")[:-1])
    sectorID = int(line.split("[")[0].split("-")[-1])
    
    # https://www.geeksforgeeks.org/python/python-frequency-of-each-character-in-string/
    freq = {}
    for c in roomname:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    if top5(freq) == checksum:
        idSum += sectorID

    name = decryptName(encryptedName,sectorID)
    
    # name found by inspection of decrypted names searching for names containing "north"
    if name == "northpole object storage":
        nposid = sectorID

print(f"Part 1: {idSum}")
print(f"Part 2: {nposid}")

