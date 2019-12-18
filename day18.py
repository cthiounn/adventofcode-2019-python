import string
with open("data/other_input/day18-input.file") as f:
    numbers = [line.strip() for line in f]

LRUD={(0,1),(0,-1),(1,0),(-1,0)}
def part1(st):
    d = dict()
    x,y=0,0
    doors = dict()
    keys= dict()
    for j in range(len(st)):
        line=st[j]
        for i in range(len(line)):
            d[(i,j)]=line[i]
            if line[i]=="@":
                x,y=i,j
            elif line[i] in string.ascii_lowercase:
                keys[(i,j)]=line[i]
            elif line[i] in string.ascii_uppercase:
                doors[(i,j)]=line[i]
 
    globalstep=0
    keystocatch=keys.copy()
    print(keystocatch)
    while len(keystocatch)>0:
        r=[(kcatch,stepToKey(x,y,kcatch,d)) for kcatch in keystocatch if stepToKey(x,y,kcatch,d)!=0]
        print("reachables",r)
        minstep=99999999999999
        if len(r)==1:
            chosen=r[0][0]
            stepchosen=r[0][1]
        else:
            chosen=r[0][0]
            stepchosen=0
            for rea,rstep in r:
                nx,ny=rea
                dk=d.copy()
                dk[rea]="."
                dcatch=[d for d in doors if doors[d]==keys[rea].upper()]
                try:
                    dk[dcatch[0]]="."
                except IndexError:
                    break
                rb=sum([stepToKey(nx,ny,kcatch,dk) for kcatch in keystocatch if stepToKey(nx,ny,kcatch,dk)!=0])+rstep
                if (rb<minstep):
                    minstep=rb
                    chosen=rea
                    stepchosen=rstep
        
        globalstep+= stepchosen
        del keystocatch[chosen]
        d[chosen]="."
        dcatch=[d for d in doors if doors[d]==keys[chosen].upper()]
        try:
            d[dcatch[0]]="."
        except IndexError:
            break
        d[(x,y)]="."
        x,y=chosen
        d[(x,y)]="@"
        print(chosen,keys[chosen],stepchosen)
        print("remaining",keystocatch)
        printmap(d)
            
            # print([(k,keys[k],reachable_tiles[k]) for k in keys if k in reachable_tiles])
            # print([(k,doors[k],reachable_tiles[k]) for k in doors if k in reachable_tiles])
    print(globalstep)

def stepToKey(x,y,kcatch,d):
    reachable_tiles=dict()
    step=0
    reachable_tiles[(x,y)]=0
    tiletoexplore=dict()
    tiletoexplore[(x,y)]=0
    while len(tiletoexplore)!=0:
        tiletoexplorecopy=tiletoexplore.copy()
        tiletoexplore.clear()
        for tile in tiletoexplorecopy:
            xt,yt=tile
            step=tiletoexplorecopy[tile]+1
            for lrud in LRUD:
                dx,dy=lrud
                nx,ny=xt+dx,yt+dy
                if d[(nx,ny)] ==".":
                    if (nx,ny) not in reachable_tiles:
                        reachable_tiles[(nx,ny)]=step 
                        tiletoexplore[(nx,ny)]=step
                    elif reachable_tiles[(nx,ny)] >step:
                        reachable_tiles[(nx,ny)]=step
                elif  d[(nx,ny)] in string.ascii_letters:
                    reachable_tiles[(nx,ny)]=step
    if kcatch in reachable_tiles:
        return step
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

part1(numbers)


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