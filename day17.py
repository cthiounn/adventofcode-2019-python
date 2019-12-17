with open("data/other_input/day17-input.file") as f:
    numbers = [line.strip() for line in f]

def part1(st):
    l = list(map(int, st.split(",")))
    d2= dict()
    for i in range(len(l)):
        d2[i] = l[i]
    i = 0
    rb = 0
    tile_to_explore = dict()
    known_tile=dict()
    x = 0
    y = 0
    d=d2.copy()
    outputQueue=[]
    inputQueue=[]
    globalStop=False
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
                d[p1] = inputQueue.pop()
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
            
        except IndexError:
            break
            

        if response==35  :
            known_tile[(x,y)]=response
            x+=1
        elif response ==46:
            known_tile[(x,y)]=response
            x+=1
        elif response ==10:
            x=0
            y+=1

    dscaffold=[p for p in known_tile if known_tile[p]==35]
    dnew=dict()
    sumintersect=0
    for p in dscaffold:
        x,y=p
        if (x+1,y) in dscaffold and (x-1,y) in dscaffold and (x,y+1) in dscaffold and (x,y-1) in dscaffold: 
            sumintersect+=x*y
            dnew[(x,y)]="O"
        else:
            dnew[(x,y)]="#"
    print(sumintersect) 
    #printmap(dnew)

    #part2 
    d=d2.copy()
    d[0]=2

def ra(a, d):
    return 0 if a not in d else d[a]

TEST='''\
#######...#####
#.....#...#...#
#.....#...#...#
......#...#...#
......#...###.#
......#.....#.#
^########...#.#
......#.#...#.#
......#########
........#...#..
....#########..
....#...#......
....#...#......
....#...#......
....#####......
'''

def test():
    tot=0
    for y, row in enumerate(TEST.splitlines()):
        for x, s in enumerate(row):
            if s=="O":
                print(x,y)
                tot+=x*y
    print(tot)

def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    # print(xmin, ymin, xmax, ymax)
    for i in range(xmin - 1, xmax + 2):
        sprint = ""
        for j in range(ymin - 1, ymax + 2):
            sprint += d2[(i, j)] if (i, j) in d2 else "."
        print(sprint.replace("1", "O").replace("0", ".").replace("2","X").replace("3","-"))


part1(numbers[0])
#test()