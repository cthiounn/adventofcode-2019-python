import string
from collections import deque
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
    tiletoexplore.append((x,y,'',0))
    find=False
    kset=''.join(sorted(set(keys.values())))
    positions=set()
    while len(tiletoexplore) != 0 and not find:
        tile=tiletoexplore.popleft()
        for lrud in LRUD:
            xt,yt,k,step = tile
            step+=1
            dx, dy = lrud
            nx, ny = xt + dx, yt + dy 
            ks=''.join(sorted(k))
            if (nx,ny) not in d or d[(nx,ny)]=="#" or (d[(nx,ny)].lower() not in k and d[(nx,ny)] in string.ascii_uppercase):
                continue
            elif (nx,ny) in d and (d[(nx,ny)].lower() in k or d[(nx,ny)]=="." or d[(nx,ny)]=="@"):
                if (nx,ny,ks) not in positions:
                    positions.add((nx,ny,ks))
                    tiletoexplore.append((nx,ny,k,step))
            elif (nx, ny) in d and d[(nx,ny)] in string.ascii_lowercase and d[(nx,ny)] not in k:
                k+=d[nx,ny]
                ks=''.join(sorted(k))
                
                if ks==kset:
                    print(step)
                    find=True
                    break
                if (nx,ny,ks) not in positions:
                    positions.add((nx,ny,ks))
                    tiletoexplore.append((nx,ny,k,step))

# heavily inspired from u/jonathan_paulson
def part2(st):
    d = dict()
    x, y = 0, 0
    doors = dict()
    keys = dict()
    robotos=[]
    for j in range(len(st)):
        line = st[j]
        for i in range(len(line)):
            d[(i, j)] = line[i]
            if line[i] == "@":
                x, y = i, j
                robotos.append((x,y))
            elif line[i] in string.ascii_lowercase:
                keys[(i, j)] = line[i]
            elif line[i] in string.ascii_uppercase:
                doors[(i, j)] = line[i]
    tiletoexplore = deque([])
    tiletoexplore.append((robotos,'',0))
    find=False
    kset=''.join(sorted(set(keys.values())))
    positions=dict()
    mindist=9999999999999
    while len(tiletoexplore) != 0 and not find:
        tile=tiletoexplore.popleft()
        
        robots,k,step = tile
        posRobots="".join(map(repr,robots))
        if  (posRobots,k) in positions and step>=positions[(posRobots,k)]:
            continue
        positions[(posRobots,k)]=step

        invalidPosition=False
        for nrob in range(len(robotos)):
            xr,yr=robots[nrob]
            if d[(xr,yr)]=='#' or (xr,yr) not in d or (d[(xr,yr)] in string.ascii_uppercase and d[(xr,yr)].lower() not in k):
                invalidPosition=True
                break
        if invalidPosition:
            continue
        
        dpos=dict()
        robotsmoves=deque([])
        for numro in range(len(robotos)):
            robotsmoves.append((robots[numro],numro,0))
        while len(robotsmoves)!=0:
            pos,num,step=robotsmoves.popleft()
            rx,ry=pos
            if d[(rx,ry)]=='#' or (rx,ry) not in d or (d[(rx,ry)] in string.ascii_uppercase and d[(rx,ry)].lower() not in k) and pos not in dpos:
                continue
            dpos[pos]=(step,num)
            for lrud in LRUD:
                dx, dy = lrud
                nx, ny = rx + dx, ry + dy
                robotsmoves.append(((nx,ny),num,step+1))
        for key in keys:
            if keys[key] not in key in dpos:
                dist,nro=dpos[key]
                robots,k,step = tile
                dist+=step
                k+=keys[key]
                robots[nro]=key
                posRobots="".join(map(repr,robots))

                ks=''.join(sorted(k))
                
                if ks==kset:
                    if dist<mindist:
                        mindist=dist
                tiletoexplore.append(posRobots,k,dist)
    print(mindist)

part1(numbers)
part2(numbers)