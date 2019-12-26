import sys
import string
from collections import Counter
import re
import math

with open("data/other_input/day24-input.file") as f:
    numbers = [line.strip() for line in f]


def part1(st):
    seen = set()
    stop = False
    newgrid = st.copy()
    while not stop:
        newgrid2 = newgrid.copy()
        newgrid = []
        for j in range(len(newgrid2)):
            line = newgrid2[j]
            newline = ""
            for i in range(len(line)):
                chartoappend = "."
                c = countbugneigh(newgrid2, i, j)
                if newgrid2[j][i] == "#" and c == 1:
                    chartoappend = "#"
                elif newgrid2[j][i] == "." and (c == 1 or c == 2):
                    chartoappend = "#"
                newline += chartoappend
            newgrid.append(newline)
        if repr(newgrid) in seen:
            stop = True
            print(calculate(newgrid))
            break
        else:
            seen.add(repr(newgrid))


LRUD = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def countbugneigh(st, i, j):
    sum = 0
    for l in LRUD:
        x = l[0] + i
        y = l[1] + j
        if 0 <= x and x < len(st[0]) and 0 <= y and y < len(st) and st[y][x] == "#":
            sum += 1
    return sum


def calculate(n):
    sum = 0
    for j in range(len(n)):
        for i in range(len(n[j])):
            if n[j][i] == "#":
                sum += pow(2, i + j * len(n[j]))
    return sum


def part2(st, time):
    levels = dict()
    st[2] = st[2][:2] + "?" + st[2][3:]
    w, n, e, s = countBorderBug(st)
    ww, nn, ee, ss = countSpecialBug(st)
    levels[0] = (st, w, n, e, s, ww, nn, ee, ss)
    levels[-1] = (createNewLevel(), 0, 0, 0, 0, 0, 0, 0, 0)
    levels[1] = (createNewLevel(), 0, 0, 0, 0, 0, 0, 0, 0)
    minutes = 0
    while minutes < time:
        minutes += 1
        levels = move(levels)
    vals = [v for v in levels.values()]
    print(sum(map(numbug, vals)))


def countBorderBug(st):
    s = numbug(st[-1])
    w = numbug([s[0] for s in st])
    e = numbug([s[-1] for s in st])
    n = numbug(st[0])
    return (w, n, e, s)


def countSpecialBug(st):
    return (
        1 if st[2][1] == "#" else 0,
        1 if st[1][2] == "#" else 0,
        1 if st[2][3] == "#" else 0,
        1 if st[3][2] == "#" else 0,
    )


def move(l):
    newlevels = dict()
    for i in l:
        # create level maxbottom and maxtop
        if (i + 1) not in l:
            bottom = (createNewLevel(), 0, 0, 0, 0, 0, 0, 0, 0)
            newlevels[i + 1] = bottom
        else:
            bottom = l[i + 1]
        if (i - 1) not in l:
            top = (createNewLevel(), 0, 0, 0, 0, 0, 0, 0, 0)
            newlevels[i - 1] = top
        else:
            top = l[i - 1]
        level = imove(l[i], top, bottom)

        newlevels[i] = level
    return newlevels


def imove(middle, top, bottom):
    mid = middle[0]
    _, _, _, _, _, ww, nn, ee, ss = top
    _, w, n, e, s, _, _, _, _ = bottom
    newgrid = []
    for j in range(len(mid)):
        newline = ""
        for i in range(len(mid[j])):
            chartoappend = "."
            c = countadvancedbugneigh(mid, i, j, w, n, e, s, ww, nn, ee, ss)
            if mid[j][i] == "#" and c == 1:
                chartoappend = "#"
            elif mid[j][i] == "." and (c == 1 or c == 2):
                chartoappend = "#"
            elif mid[j][i] == "?":
                chartoappend = "?"
            newline += chartoappend
        newgrid.append(newline)
    w1, n1, e1, s1 = countBorderBug(newgrid)
    ww1, nn1, ee1, ss1 = countSpecialBug(newgrid)
    return (newgrid, w1, n1, e1, s1, ww1, nn1, ee1, ss1)


def countadvancedbugneigh(st, i, j, w, n, e, s, ww, nn, ee, ss):
    sum = 0
    for l in LRUD:
        x = l[0] + i
        y = l[1] + j
        if 0 <= x and x < len(st[0]) and 0 <= y and y < len(st) and st[y][x] == "#":
            sum += 1
    # top and bottom border, add top nn or bottom nn
    if j == 0:
        sum += nn
    elif j == 4:
        sum += ss

    if i == 0:
        sum += ww
    elif i == 4:
        sum += ee

    if i == 1 and j == 2:  # W
        sum += w
    elif i == 2 and j == 1:  # N
        sum += n
    elif i == 3 and j == 2:  # E
        sum += e
    elif i == 2 and j == 3:  # S
        sum += s

    return sum


def createNewLevel():
    p = ["....." for _ in range(5)]
    p[2] = p[2][:2] + "?" + p[2][3:]
    return p


def numbug(s):
    return Counter(repr(s))["#"]


part1(numbers)
part2(numbers, 200)
