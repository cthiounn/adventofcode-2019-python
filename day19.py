import string
from collections import deque
with open("data/other_input/day19-input.file") as f:
    numbers = [line.strip() for line in f]



def part1(st,maxx,maxy,minx,miny):
    l = list(map(int, st.split(",")))
    d2 = dict()
    for i in range(len(l)):
        d2[i] = l[i]
    i = 0
    rb = 0
    known_tile = dict()
    d = d2.copy()
    outputQueue = []
    inputQueue = deque([])
    globalStop = False
    total=0
    for x in range(minx,maxx):
        for y in range(miny,maxy):
            i = 0
            rb = 0
            d = d2.copy()
            outputQueue = []
            inputQueue = deque([])
            globalStop = False
            inputQueue.append(x)
            inputQueue.append(y)
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
                        d[p1] = inputQueue.popleft()
                        i += 2
                    elif c == 4:
                        outputQueue.append(p1)
                        i += 2
                        if len(outputQueue) == 1:
                            break
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
                try:
                    response = outputQueue.pop()
                    total+=response
                    known_tile[(x,y)]=response
                except IndexError:
                    break
                
    print(total)
        
def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    # print(xmin, ymin, xmax, ymax)
    for j in range(ymin - 1, ymax + 2):
        sprint = ""
        for i in range(xmin - 1, xmax + 2):
            sprint += str(d2[(i, j)]) if (i, j) in d2 else "."
        print(sprint)

def ra(a, d):
    return 0 if a not in d else d[a]
part1(numbers[0],50,50,0,0)


def part2(st):
    l = list(map(int, st.split(",")))
    d2 = dict()
    for i in range(len(l)):
        d2[i] = l[i]
    i = 0
    rb = 0
    known_tile = dict()
    d = d2.copy()
    outputQueue = []
    inputQueue = deque([])
    globalStop = False
    total=0
    x=0
    y=0
    while (True):
            if computer(x,y,d)==1 :
                if computer(x-99,y+99,d)==1:
                    print((x-99)*10000+(y))
                    break
                else:
                    x+=1
            else:
                y+=1

def computer(x,y,d2):
    if x<0:
        return 0
    if y<0:
        return 0
    i = 0
    rb = 0
    d = d2.copy()
    outputQueue = []
    inputQueue = deque([])
    globalStop = False
    inputQueue.append(x)
    inputQueue.append(y)
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
                d[p1] = inputQueue.popleft()
                i += 2
            elif c == 4:
                outputQueue.append(p1)
                i += 2
                if len(outputQueue) == 1:
                    break
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
        try:
            return outputQueue.pop()
        except IndexError:
            break

    
part2(numbers[0])