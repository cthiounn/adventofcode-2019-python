import itertools
from collections import Counter
import unittest


with open("data/my_input/day9-input.file") as f:
    numbers = [line.strip() for line in f]


def part1(st, input):
    l = list(map(int, st.split(",")))
    d = dict()
    for i in range(len(l)):
        d[i] = l[i]
    i = 0
    rb = 0
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
            d[p1] = input
            i += 2
        elif c == 4:
            input = p1
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
        elif c == 9:
            rb += p1
            i += 2
        else:
            print("???")
    print(input)


def ra(a, d):
    return 0 if a not in d else d[a]


part1(numbers[0], 1)
part1(numbers[0], 2)

