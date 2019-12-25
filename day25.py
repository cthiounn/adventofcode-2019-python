from collections import deque

with open("data/other_input/day25-input.file") as f:
    numbers = [line.strip() for line in f]


def part1(st, ccstart):
    l = list(map(int, st.split(",")))
    d2 = dict()
    for i in range(len(l)):
        d2[i] = l[i]

    d = d2.copy()
    outputQueue = []
    inputQueue = []
    globalStop = False

    command = (
        ccstart.replace("E", "east\n")
        .replace("N", "north\n")
        .replace("S", "south\n")
        .replace("W", "west\n")
        .replace("T", "take")
        .replace("D", "drop")
    )
    inputQueue = deque([ord(c) for c in command])
    i = 0
    rb = 0
    outps = ""
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
                    towrite = inputQueue.popleft()
                    d[p1] = towrite
                else:
                    stop = True
                    globalStop = True
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

    # print(outputQueue)
    print("".join(map(chr, outputQueue)))


def ra(a, d):
    return 0 if a not in d else d[a]


command1 = ""  # E
command1 += "E"  # N,S,(W)
# command1 += "S"
# command1 += "T escape pod\n"
command1 += "N"  # N,(S),E
command1 += "N"  # ENN:spool of cat6
command1 += "T spool of cat6\n"
command1 += "S"
command1 += "E"  # N,(W)
command1 += "T mug\n"  # ENE:mug
command1 += "N"  # N,E,(S)
command1 += "N"
# command1 += "take infinite loop\n"
command1 += "W"  # N,S,(E)
command1 += "T asterisk\n"
# command1 += "north\n"
# command1 += "take molten lava\n"
command1 += "S"
command1 += "T monolith\n"
command1 += "NEESE"
command1 += "T sand\n"
command1 += "SW"
command1 += "T prime number\n"
command1 += "ENE"
# command1 += "take giant electromagnet\n"
# command1 += "N"
# command1 += "T photons\n"
# command1 += "drop monolith\n"
command1 += "S"
command1 += "T tambourine\n"
command1 += "W"
command1 += "T festive hat\n"
command1 += "N"
#  command1 += "D sand\n"
command1 += "D mug\n"
command1 += "D spool of cat6\n"
# command1 += "D tambourine\n"
command1 += "D festive hat\n"

command1 += "D monolith\n"
command1 += "W"

part1(numbers[0], command1)

