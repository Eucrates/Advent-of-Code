import sys
import itertools
import threading
import time
import queue

input_received_evnet = threading.Event()

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


def calculate(thread_id,input_queue,output_queue=None,states=None):

    if output_queue is None:
        output_queue = queue.Queue()
    if states is None:
        states = [x for x in orig_states]
    
    #print(f"Thread {thread_id} started and waiting...")
    #print(f"Thread {thread_id} received: {list(input_queue.queue)}")

    pos = 0
    while pos < len(states):
        inst = str(states[pos]).rjust(5,"0")
        op = int(inst[-2:])
        params = inst[:-2][::-1]
        if op == 99:
            #print(f"Thread {thread_id} finished.")
            #print(list(output_queue.queue))
            if threading.current_thread() is threading.main_thread():
                return output_queue.get()
            return

        if op == 1 or op == 2 or (op > 4 and op <= 8):
            if params[0] == "0":
                operand1 = states[states[pos+1]]
            else:
                operand1 = states[pos+1]
            if params[1] == "0":
                operand2 = states[states[pos+2]]
            else:
                operand2 = states[pos+2]
            location = states[pos+3]
            if op == 1:
                val = operand1+operand2
                pos += 4
                states[location] = val
            elif op == 2:
                val = operand1*operand2
                pos += 4
                states[location] = val
            elif op == 5:
                if operand1 != 0:
                    pos = operand2
                else:
                    pos += 3
            elif op == 6:
                if operand1 == 0:
                    pos = operand2
                else:
                    pos += 3
            elif op == 7:
                if operand1 < operand2:
                    states[location] = 1
                else:
                    states[location] = 0
                pos += 4
            elif op == 8:
                if operand1 == operand2:
                    states[location] = 1
                else:
                    states[location] = 0
                pos += 4
        elif op == 3:
            i = input_queue.get()
            location = states[pos+1]
            states[location] = i
            pos += 2
        elif op == 4:
            if params[0] == "0":
                location = states[pos+1]
                out = states[location]
            else:
                out = states[pos+1]
            output_queue.put(out)
            pos += 2
        else:

            print("Unknown state:",op, params)
            exit(1)
    return states


for line in lines:
    line = line.strip("\n")
    states = line.split(",")

    states = [int(x) for x in states]

orig_states = [x for x in states]

def Part1():
    maxout = -sys.maxsize

    numbers = range(5)
    all_sequences = list(itertools.permutations(numbers))
    for sequence in all_sequences:
        q1 = queue.Queue()
        q2 = queue.Queue()
        q3 = queue.Queue()
        q4 = queue.Queue()
        q5 = queue.Queue()

        q1.put(sequence[0])
        q2.put(sequence[1])
        q3.put(sequence[2])
        q4.put(sequence[3])
        q5.put(sequence[4])
    
        q1.put(0)
        states = [x for x in orig_states]
        out_a = calculate(1,q1)
        q2.put(out_a)
        states = [x for x in orig_states]
        out_b = calculate(2,q2)
        q3.put(out_b)
        states = [x for x in orig_states]
        out_c = calculate(3,q3)
        q4.put(out_c)
        states = [x for x in orig_states]
        out_d = calculate(4,q4)
        q5.put(out_d)
        states = [x for x in orig_states]
        out_e = calculate(5,q5)
        if out_e > maxout:
            maxout = out_e
            seq = sequence
        #print(sequence,":",maxout,out_e)
    return maxout
print(f"Part 1: {Part1()}")

def Part2():
    maxout = -sys.maxsize
    numbers = range(5,10)
    all_sequences = list(itertools.permutations(numbers))
    out_e = 0
    for sequence in all_sequences:
        #print(sequence)
        q1 = queue.Queue()
        q2 = queue.Queue()
        q3 = queue.Queue()
        q4 = queue.Queue()
        q5 = queue.Queue()

        t1 = threading.Thread(target=calculate, args=(1,q1,q2,[x for x in orig_states]))
        t2 = threading.Thread(target=calculate, args=(2,q2,q3,[x for x in orig_states]))
        t3 = threading.Thread(target=calculate, args=(3,q3,q4,[x for x in orig_states]))
        t4 = threading.Thread(target=calculate, args=(4,q4,q5,[x for x in orig_states]))
        t5 = threading.Thread(target=calculate, args=(5,q5,q1,[x for x in orig_states]))

        q1.put(sequence[0])
        q2.put(sequence[1])
        q3.put(sequence[2])
        q4.put(sequence[3])
        q5.put(sequence[4])
        
        q1.put(0)
        #print("Starting first threat....")

        for t in [t1,t2,t3,t4,t5]:
            t.start()
        for t in [t1,t2,t3,t4,t5]:
            t.join()
        
        if not q1.empty():
            maxout = max(maxout,q1.get())
        #print("All threads finished")
    return maxout

print(f"Part 2: {Part2()}")







