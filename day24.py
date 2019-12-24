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


def part2(st):
    levels = dict()
    minutes = 0
    while minutes < 200:
        minutes += 1
        newgrid = []
        for j in range(len(st)):
            line = st[j]
            newline = ""
            for i in range(len(line)):
                chartoappend = "."
                c = countbugneigh(st, i, j)
                if st[j][i] == "#" and c == 1:
                    chartoappend = "#"
                elif st[j][i] == "." and (c == 1 or c == 2):
                    chartoappend = "#"
                newline += chartoappend
            newgrid.append(newline)
        st = newgrid.copy()
    vals = [v for v in levels.values()]
    print(sum(map(numbug, vals)))


def numbug(s):
    return Counter(repr(s))["#"]


part1(numbers)
part2(numbers)
