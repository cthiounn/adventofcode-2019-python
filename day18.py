import string
import random

with open("data/other_input/day18-input.file") as f:
    numbers = [line.strip() for line in f]

LRUD = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def part1(st, br):
    d = dict()
    x, y = 0, 0
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
                doors[(i, j)] = line[i]
    # printmap(d)
    if len(keys) == 0:
        return 0
    globalstep = 0
    r = [
        (kcatch, stepToKey(x, y, kcatch, d))
        for kcatch in keys
        if stepToKey(x, y, kcatch, d) != 0
    ]
    inp = []
    for ra in r:
        dk = d.copy()
        chosen = ra[0]
        stepchosen = ra[1]
        dk[chosen] = "@"
        dcatch = [d for d in doors if doors[d] == keys[chosen].upper()]
        if len(dcatch) > 0 and dcatch[0] in dk:
            dk[dcatch[0]] = "."
        dk[(x, y)] = "."
        newinput = stringify(dk)
        inp.append((ra, stepchosen + part1(newinput, False), stepchosen))
    if len(inp) > 0:
        chosen = min(inp, key=lambda s: s[1])
        if br:
            print(chosen[1])
        globalstep = chosen[2]

    return globalstep


def stepToKey(x, y, kcatch, d):
    reachable_tiles = dict()
    step = 0
    reachable_tiles[(x, y)] = 0
    tiletoexplore = dict()
    tiletoexplore[(x, y)] = 0
    while len(tiletoexplore) != 0:
        tiletoexplorecopy = tiletoexplore.copy()
        tiletoexplore.clear()
        for tile in tiletoexplorecopy:
            xt, yt = tile
            step = tiletoexplorecopy[tile] + 1
            for lrud in LRUD:
                dx, dy = lrud
                nx, ny = xt + dx, yt + dy
                if (nx, ny) not in reachable_tiles:
                    reachable_tiles[(nx, ny)] = step
                    if d[(nx, ny)] == ".":
                        tiletoexplore[(nx, ny)] = step
                elif reachable_tiles[(nx, ny)] > step:
                    reachable_tiles[(nx, ny)] = step
    if kcatch in reachable_tiles:
        return reachable_tiles[kcatch]
    else:
        return 0


def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    # print(xmin, ymin, xmax, ymax)
    for j in range(ymin - 1, ymax + 2):
        sprint = ""
        for i in range(xmin - 1, xmax + 2):
            sprint += d2[(i, j)] if (i, j) in d2 else "."
        print(sprint)


def stringify(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    sstring = []
    for j in range(ymin, ymax + 1):
        sprint = ""
        for i in range(xmin, xmax + 1):
            sprint += d2[(i, j)] if (i, j) in d2 else "."
        sstring.append(sprint)
    return sstring


part1(numbers, True)


# def simulate(rea,rstep,d,doors,keys):
#     if len(keys)==0:
#         return 0
#     else:
#         nx,ny=rea
#         dk=d.copy()
#         dk[rea]="."
#         dcatch=[d for d in doors if doors[d]==keys[rea].upper()]
#         try:
#             dk[dcatch[0]]="."
#         except IndexError:
#             break
#         ddoors=doors.copy()
#         dkeys=keys.copy()
#         return rstep + simulate(,,dk,ddoors,dkeys)
