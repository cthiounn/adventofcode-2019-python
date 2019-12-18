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
    knowntiles=dict()
    find=False
    kset=''.join(sorted(set(keys.values())))
    knowntiles[x,y,'']=0
    while len(tiletoexplore) != 0 and not find:
        tile=tiletoexplore.popleft()
        #r=[(kcatch,stepToKey(x,y,kcatch,d)) for kcatch in keystocatch if stepToKey(x,y,kcatch,d)!=0]
 
        for lrud in LRUD:
            xt,yt,k,step = tile
            
            print(step)
            step+=1
            dx, dy = lrud
            nx, ny = xt + dx, yt + dy 
            if (nx,ny) not in d or d[(nx,ny)]=="#" or (d[(nx,ny)].lower() not in k and d[(nx,ny)] in string.ascii_uppercase):
                continue
            elif (nx,ny) in d and (d[(nx,ny)].lower() in k or d[(nx,ny)]=="." or d[(nx,ny)]=="@"):
                if (nx,ny,k) in knowntiles and step < knowntiles[(nx,ny,k)]:
                    tiletoexplore.append((nx,ny,k,step))
                    knowntiles[(nx,ny,k)]=step
                elif (nx,ny,k) not in knowntiles:
                    tiletoexplore.append((nx,ny,k,step))
                    knowntiles[(nx,ny,k)]=step
            elif (nx, ny) in d and d[(nx,ny)] in string.ascii_lowercase and d[(nx,ny)] not in k:
                k+=d[nx,ny]
                ks=''.join(sorted(k))
                
                if ks==kset:
                    print(knowntiles)
                    print(step)
                    find=True
                    break
                if (nx,ny,k) in knowntiles and step < knowntiles[(nx,ny,k)]:
                    tiletoexplore.append((nx,ny,k,step))
                    knowntiles[(nx,ny,k)]=step
                elif (nx,ny,k) not in knowntiles:
                    tiletoexplore.append((nx,ny,k,step))
                    knowntiles[(nx,ny,k)]=step


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

part1(numbers)
