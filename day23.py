from collections import deque

with open("data/other_input/day23-input.file") as f:
    numbers = [line.strip() for line in f]
import asyncio


def ra(a, d):
    return 0 if a not in d else d[a]


def part1(st):
    l = list(map(int, st.split(",")))
    d2 = dict()
    for i in range(len(l)):
        d2[i] = l[i]
    known_tile = dict()
    d = d2.copy()
    outputQueue = []
    inputQueues = [deque([]) for _ in range(256)]
    status = [(0, 0, d.copy()) for _ in range(50)]
    for j in range(len(inputQueues)):
        inputQueues[j].append((j, -1))
    globalStop = False
    total = 0
    x = 0
    y = 0
    dest = 0
    stop = False
    while not stop:
        for i in range(50):
            iinit, rbinit, dinit = status[i]
            oo = []
            if len(inputQueues[i]) > 0:
                oo.append(inputQueues[i].popleft())
            result = computer(oo, iinit, rbinit, dinit)
            x, y, iinit, rbinit, dinit, dest = result
            status[i] = (iinit, rbinit, dinit)
            if dest == 255:
                print(y)
                stop = True
                break
            # elif dest == -1:
            #     inputQueues[i].append((-1, -1))
            else:
                inputQueues[dest].append((x, y))


def computer(inputs, iinit, rbinit, d2):
    x = 0
    y = 0
    dest = 0
    i = iinit
    rb = rbinit
    d = d2.copy()
    outputQueue = []
    inputQueue = deque([])
    if len(inputs) > 0:
        for n in inputs:
            inputQueue.append(n[0])
            inputQueue.append(n[1])
    globalStop = False
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

                if len(inputQueue) > 0:
                    d[p1] = inputQueue.popleft()
                    i += 2
                else:
                    return (-1, -1, i, rb, d.copy(), -1)
                # else:
                # d[p1] =-1
                # await asyncio.sleep(1)
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
            y = outputQueue.pop()
            x = outputQueue.pop()
            dest = outputQueue.pop()
            return (x, y, i, rb, d.copy(), dest)
        except IndexError:
            break


part1(numbers[0])
