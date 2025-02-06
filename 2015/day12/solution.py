import sys
import json

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    data = json.load(f)

tot =  0
totNoRed = 0

def iterJson(data):
    global tot
    for key,value in data.items():
        if type(value) == dict:
            iterJson(value)
        elif type(value) == list:
            for val in value:
                if type(val) == str:
                    if val.isdigit():
                        tot += int(val)
                elif type(val) == list:
                    for v in val:
                        iterList(v)
                elif type(val) == dict:
                    iterJson(val)
                elif type(val) == int:
                    tot += val
                else:
                    print("Unknown type inner iterJson:", type(val))
        elif type(value) == str:
            pass
        elif type(value) == int:
            tot += value
        else:
            print("Unknown type outer iterJson:", type(value),value)

def iterList(l):
    global tot
    global totNoRed
    if type(l) == dict:
        iterJson(l)
    elif type(l) == list:
        for item in l:
            iterList(item)
    elif type(l) == str:
        if l.isdigit():
            tot += int(l)
    elif type(l) == int:
        tot += l
    elif type(l) == str:
        pass
    else:
        print("unknown type, outer iterlist:", type(l),l)


def iterJsonNoRed(data):
    global totNoRed
    for key,value in data.items():
        if type(value) == dict:
            if "red" in value.values():
                continue
            iterJsonNoRed(value)
        elif type(value) == list:
            for val in value:
                if type(val) == str:
                    if val.isdigit():
                        totNoRed += int(val)
                elif type(val) == list:
                    for v in val:
                        iterListNoRed(v)
                elif type(val) == dict:
                    if "red" in val.values():
                        continue
                    iterJsonNoRed(val)
                elif type(val) == int:
                    totNoRed += val
                else:
                    print("Unknown type inner iterJson:", type(val))
        elif type(value) == str:
            pass
        elif type(value) == int:
            totNoRed += value
        else:
            print("Unknown type outer iterJson:", type(value),value)

def iterListNoRed(l):
    global totNoRed
    if type(l) == dict:
        if "red" in l.values():
            return
        iterJsonNoRed(l)
    elif type(l) == list:
        for item in l:
            iterListNoRed(item)
    elif type(l) == str:
        if l.isdigit():
            totNoRed += int(l)
    elif type(l) == int:
        totNoRed += l
    elif type(l) == str:
        pass
    else:
        print("unknown type, outer iterlist:", type(l),l)


iterJson(data)
print("Part1:", tot)
iterJsonNoRed(data)
print("Part2:", totNoRed)
