import string
from collections import deque
import json

with open("data/other_input/day18-input.file") as f:
    numbers = [line.strip() for line in f]

LRUD = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def part1(st):
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
    tiletoexplore = deque([])
    tiletoexplore.append((x, y, "", 0))
    find = False
    kset = "".join(sorted(set(keys.values())))
    positions = set()
    while len(tiletoexplore) != 0 and not find:
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
                    print(step)
                    find = True
                    break
                if (nx, ny, ks) not in positions:
                    positions.add((nx, ny, ks))
                    tiletoexplore.append((nx, ny, k, step))


# heavily inspired from u/jonathan_paulson
def part2(st, to_init):
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
                if not to_init:
                    robotos.append((x, y))
            elif line[i] in string.ascii_lowercase:
                keys[(i, j)] = line[i]
            elif line[i] in string.ascii_uppercase:
                doors[(i, j)] = line[i]

    if to_init:
        d[(x, y)] = "#"
        d[(x + 1, y)] = "#"
        d[(x - 1, y)] = "#"
        d[(x, y + 1)] = "#"
        d[(x, y - 1)] = "#"
        d[(x + 1, y + 1)] = "@"
        d[(x - 1, y - 1)] = "@"
        d[(x - 1, y + 1)] = "@"
        d[(x + 1, y - 1)] = "@"
        robotos.append((x - 1, y - 1))
        robotos.append((x + 1, y - 1))
        robotos.append((x - 1, y + 1))
        robotos.append((x + 1, y + 1))

    tiletoexplore = deque([])

    posRobots = ";".join(map(repr, robotos))
    tiletoexplore.append((posRobots, "", 0))
    find = False
    kset = "".join(sorted(set(keys.values())))
    # positions = dict()
    mindist = 9999999999999
    while len(tiletoexplore) != 0 and not find:
        tile = tiletoexplore.popleft()
        posRobots, k, step = tile

        robots = [eval(e) for e in posRobots.split(";")]
        # posRobots = "".join(map(repr, robots))
        # if (posRobots, k) in positions and step >= positions[(posRobots, k)]:
        #     continue
        # positions[(posRobots, k)] = step

        # test invalidPosition
        invalidPosition = False
        for nrob in range(len(robotos)):
            xr, yr = robots[nrob]
            if (
                d[(xr, yr)] == "#"
                or (xr, yr) not in d
                or (
                    d[(xr, yr)] in string.ascii_uppercase
                    and d[(xr, yr)].lower() not in k
                )
            ):
                invalidPosition = True
                break
        if invalidPosition:
            continue

        # from a position, define what can any robot reach
        # output a dictionnary of position: step, numofroboto
        dpos = dict()
        robotsmoves = deque([])
        for numro in range(len(robotos)):
            robotsmoves.append((robots[numro], numro, 0))
        while len(robotsmoves) != 0:
            pos, num, step = robotsmoves.popleft()
            rx, ry = pos
            if (
                d[(rx, ry)] == "#"
                or (rx, ry) not in d
                or (
                    d[(rx, ry)] in string.ascii_uppercase
                    and d[(rx, ry)].lower() not in k
                )
                or pos in dpos
            ):
                continue
            dpos[pos] = (step, num)
            for lrud in LRUD:
                dx, dy = lrud
                nx, ny = rx + dx, ry + dy
                if (nx, ny) not in d or d[(nx, ny)] == "#":
                    continue
                robotsmoves.append(((nx, ny), num, step + 1))

        # from the uncatched-keys, evaluate from the dictionnary if a roboto can reach
        # apply and submit new position
        for key in keys:
            if keys[key] not in k and key in dpos:
                # inputs
                dist, nro = dpos[key]
                posRobots, k, step = tile

                # calculate
                dist += step
                k += keys[key]

                robots = [eval(e) for e in posRobots.split(";")]
                robots[nro] = key
                posRobots = ";".join(map(repr, robots))
                # test if all keys are catched then output min
                ks = "".join(sorted(k))
                if ks == kset:
                    if dist < mindist:
                        mindist = dist

                # submit next position
                tiletoexplore.append((posRobots, k, dist))
    print(mindist)


# part1(numbers)
part2(numbers, True)

