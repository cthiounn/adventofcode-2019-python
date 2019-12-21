import string
from collections import deque
with open("data/other_input/day21-input.file") as f:
    numbers = [line.strip() for line in f]



def part1(st,ccstart,cc):
    l = list(map(int, st.split(",")))
    d2 = dict()
    for i in range(len(l)):
        d2[i] = l[i]

    d = d2.copy() 
    outputQueue = []
    inputQueue = []
    globalStop = False

    

    # command += "NOT A T\n"
    # command += "AND T J\n"
    # command += "NOT B T\n"
    # command += "AND T J\n"
    # command += "NOT C T\n"
    # command += "AND T J\n"
    # command += "OR T J\n"
    
    # command += "NOT C T\n"
    # command += "OR T J\n"

    # command += "NOT A T\n"
    # command += "AND T J\n"
    # command += "NOT B T\n"
    # command += "AND T J\n"
    # command += "NOT C T\n"
    # command += "AND T J\n"
    # command += "NOT D T\n"
    # command += "AND T J\n"
    command =ccstart
    command += cc+"\n"
    inputQueue = deque([ord(c) for c in command])
    i = 0
    rb = 0
    step = 0
    outps=""
    while not globalStop:
        stop = False
        while not stop:
            r2 = ra(i + 1, d)
            r3 = ra(i + 2, d)
            r4 = ra(i + 3, d)
            c = d[i] % 10
            pp1 = d[i] % 1000 // 100
            pp2 = d[i] % 10000 // 1000
            pp3 = d[i] // 10000
            # 0 relative, 1 direct, 2 rel+rb
            if pp1 == 1:
                p1 = r2
            elif pp1 == 2:
                p1 = ra(r2 + rb, d)
            else:
                p1 = ra(r2, d)

            if pp2 == 1:
                p2 = r3
            elif pp2 == 2:
                p2 = ra(r3 + rb, d)
            else:
                p2 = ra(r3, d)

            if pp3 == 1:
                p3 = r4
            elif pp3 == 2:
                p3 = r4 + rb
            else:
                p3 = r4

            if c == 1:
                d[p3] = p1 + p2
                i += 4
            elif c == 2:
                d[p3] = p1 * p2
                i += 4
            elif c == 3:
                p1 = r2 + rb if pp1 == 2 else r2
                towrite = inputQueue.popleft()
                d[p1] = towrite
                i += 2
            elif c == 4:
                outputQueue.append(p1)
                i += 2
            elif c == 5:
                if p1 != 0:
                    i = p2
                else:
                    i += 3
            elif c == 6:
                if p1 == 0:
                    i = p2
                else:
                    i += 3
            elif c == 7:
                d[p3] = 1 if p1 < p2 else 0
                i += 4
            elif c == 8:
                d[p3] = 1 if p1 == p2 else 0
                i += 4
            elif d[i] == 99:
                stop = True
                globalStop = True
            elif c == 9:
                rb += p1
                i += 2
            else:
                print("???")
        if globalStop:
            break
    
    for o in outputQueue:
        if o == 35:
            outps+='#'
        elif o == 46:
            outps+='.'
        elif o==10:
            outps+='\n'
        elif o==64:
            outps+='@'
        else:
            print(o)
    print(outps)

def ra(a, d):
    return 0 if a not in d else d[a]  

command1 =""
command1 += "NOT A J\n"
command1 += "NOT B T\n"
command1 += "OR T J\n"
command1 += "NOT C T\n"
command1 += "OR T J\n"
command1 += "AND D J\n"

command2 =""
command2 += "NOT A J\n"
command2 += "NOT B T\n"
command2 += "OR T J\n"
command2 += "NOT C T\n"
command2 += "OR T J\n"
command2 += "AND D J\n"
command2 += "NOT E T\n"
command2 += "NOT T T\n"
command2 += "OR H T\n"
command2 += "AND T J\n"

part1(numbers[0],command1,"WALK")
part1(numbers[0],command2,"RUN")