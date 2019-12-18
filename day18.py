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

part1(numbers)
