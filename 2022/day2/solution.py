strategy = []
with open ("input.txt","r") as f:
    for line in f.readlines():
        line = line.strip()
        strategy.append(line.split(" "))
strategy.remove(strategy[len(strategy)-1])



'''

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
'''
score = 0
for s in strategy:

    O,S = s[0],s[1]
    match O:
        case 'A':
            match S:
                case 'X':
                    score = score + 1 + 3
                case 'Y':
                    score = score + 2 + 6
                case 'Z':
                    score = score + 3 + 0
        case 'B':
            match S:
                case 'X':
                    score = score + 1 + 0 
                case 'Y':
                    score = score + 2 + 3
                case 'Z':
                    score = score + 3 + 6
        case 'C':
            match S:
                case 'X':
                    score = score + 1 + 6
                case 'Y':
                    score = score + 2 + 0
                case 'Z':
                    score = score + 3 + 3

print (score)


score = 0
for s in strategy:

    O,S = s[0],s[1]
    match O:
        case 'A':
            match S:
                case 'X':
                    score = score + 0 + 3
                case 'Y':
                    score = score + 3 + 1
                case 'Z':
                    score = score + 6 + 2
        case 'B':
            match S:
                case 'X':
                    score = score + 0 + 1
                case 'Y':
                    score = score + 3 + 2
                case 'Z':
                    score = score + 6 + 3
        case 'C':
            match S:
                case 'X':
                    score = score + 0 + 2
                case 'Y':
                    score = score + 3 + 3
                case 'Z':
                    score = score + 6 + 1

print (score)
