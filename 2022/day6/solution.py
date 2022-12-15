with open ("input.txt","r") as f:
    signal = f.readline().strip()

window = 14

def find_message_start(signal):
    tot = 0
    for i in range(window):
        tot = tot + i
    
    for h in range(len(signal)):
        block = signal[h:h+window]
        if len(block) < window:
            return "No message found"
        k = 0
        for i in range (window):
            if k == tot:
                return(h+window)
            for j in range (i+1,window):
                if block[i] == block[j]:
                    break
                k +=1

print(find_message_start(signal))
