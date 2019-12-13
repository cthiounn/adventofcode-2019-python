import sys

with open("data/other_input/day13-input.file") as f:
    numbers = [line.strip() for line in f]


def part1(st, ii,part2):
    l = list(map(int, st.split(",")))
    d = dict()
    d2 = dict()
 
    for i in range(len(l)):
        d[i] = l[i]
    if part2:
        d[0]=ii
    i = 0
    rb = 0
    paint = 0
    direction = 0
    # 0 up 1 right 2 bottom 3 left
    inp = 0
    x = 0
    y = 0
    tileid=0
    step = 0
    globalStop = False
    inputQueue = []
    inputQueue.append(ii)
    outputQueue = []
    score=[]
    while not globalStop:
        # inp=ra((x,y),d2)
        # print("reading input:",inp)
        step += 1
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
                d[p1] = inputQueue.pop()
                i += 2
            elif c == 4:
                outputQueue.append(p1)
                i += 2
                if len(outputQueue) == 3:
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
            tileid = outputQueue.pop()
            y = outputQueue.pop()
            x = outputQueue.pop()
        except IndexError:
            break
        if x==-1 and y==0:
            score.append(tileid)
        else:
            d2[(x,y)]=tileid

    print(sum([1 for p in d2.values() if p==2]))
    printmap(d2)


def ra(a, d):
    return 0 if a not in d else d[a]


def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    # print(xmin, ymin, xmax, ymax)
    for i in range(xmin - 1, xmax + 2):
        sprint = ""
        for j in range(ymin - 1, ymax + 2):
            sprint += str(d2[i, j]) if (i, j) in d2 else "."
        print(sprint.replace("1", "O").replace("0", ".").replace("2","X").replace("3","-"))


part1(numbers[0], 0,False)
#part1(numbers[0], 2,True)

