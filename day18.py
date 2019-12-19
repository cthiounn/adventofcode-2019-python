import string
from collections import deque
import json

with open("data/other_input/day18-input.file") as f:
    numbers = [line.strip() for line in f]

LRUD = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def part1(st, parttwo):
    d = dict()
    x, y = 0, 0
    alldoors = dict()
    doors = dict()
    keys = dict()
    for j in range(len(st)):
        line = st[j]
        for i in range(len(line)):
            d[(i, j)] = line[i]
            if line[i] == "@":
                x, y = i, j
            elif line[i] in string.ascii_lowercase:
                keys[(i, j)] = line[i]
            elif line[i] in string.ascii_uppercase:
                alldoors[(i, j)] = line[i]
    for door in alldoors:  # filter for part 2
        if alldoors[door].lower() in keys.values():
            doors[door] = alldoors[door]
        else:
            d[door] = "."
    tiletoexplore = deque([])
    tiletoexplore.append((x, y, "", 0))
    kset = "".join(sorted(set(keys.values())))
    positions = set()
    while len(tiletoexplore) != 0:
        tile = tiletoexplore.popleft()
        for lrud in LRUD:
            xt, yt, k, step = tile
            step += 1
            dx, dy = lrud
            nx, ny = xt + dx, yt + dy
            ks = "".join(sorted(k))
            if (
                (nx, ny) not in d
                or d[(nx, ny)] == "#"
                or (
                    d[(nx, ny)].lower() not in k
                    and d[(nx, ny)] in string.ascii_uppercase
                )
            ):
                continue
            elif (nx, ny) in d and (
                d[(nx, ny)].lower() in k or d[(nx, ny)] == "." or d[(nx, ny)] == "@"
            ):
                if (nx, ny, ks) not in positions:
                    positions.add((nx, ny, ks))
                    tiletoexplore.append((nx, ny, k, step))
            elif (
                (nx, ny) in d
                and d[(nx, ny)] in string.ascii_lowercase
                and d[(nx, ny)] not in k
            ):
                k += d[nx, ny]
                ks = "".join(sorted(k))

                if ks == kset:
                    if not parttwo:
                        print(step)
                    return step
                if (nx, ny, ks) not in positions:
                    positions.add((nx, ny, ks))
                    tiletoexplore.append((nx, ny, k, step))
    return 0


def part2(st):
    d = dict()
    x, y = 0, 0
    doors = dict()
    keys = dict()
    robotos = []
    for j in range(len(st)):
        line = st[j]
        for i in range(len(line)):
            d[(i, j)] = line[i]
            if line[i] == "@":
                x, y = i, j
            elif line[i] in string.ascii_lowercase:
                keys[(i, j)] = line[i]
            elif line[i] in string.ascii_uppercase:
                doors[(i, j)] = line[i]
    d[(x, y)] = "#"
    d[(x + 1, y)] = "#"
    d[(x - 1, y)] = "#"
    d[(x, y + 1)] = "#"
    d[(x, y - 1)] = "#"
    d[(x + 1, y + 1)] = "@"
    d[(x - 1, y - 1)] = "@"
    d[(x - 1, y + 1)] = "@"
    d[(x + 1, y - 1)] = "@"

    st1 = dicttolist(d, 0, x, 0, y)
    st2 = dicttolist(d, x, len(st[0]), 0, y)
    st3 = dicttolist(d, 0, x, y, len(st))
    st4 = dicttolist(d, x, len(st[0]), y, len(st))

    print(part1(st1, True) + part1(st2, True) + part1(st3, True) + part1(st4, True))


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


def dicttolist(d2, xmin, xmax, ymin, ymax):

    li = []
    for j in range(ymin, ymax + 1):
        sprint = ""
        for i in range(xmin, xmax + 1):
            sprint += str(d2[(i, j)]) if (i, j) in d2 else "."
        li.append(sprint)
    return li


part1(numbers, False)
part2(numbers)

