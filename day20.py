import sys
import string
from collections import deque
import json

with open("data/other_input/day20-input.file") as f:
    numbers = [line for line in f]

LRUD = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def part1(st, parttwo):
    d = dict()
    portals=dict()
    xstart,ystart,xfinish,yfinish=0,0,0,0
    for j in range(len(st)):
        line = st[j]
        for i in range(len(line)):
            d[(i, j)] = line[i]
            if line[i] in string.ascii_uppercase:
                nameportal=""
                if j+1 < len(st) and st[j+1][i] in string.ascii_uppercase:
                    nameportal=line[i]+st[j+1][i]
                    if j+2 < len(st) and st[j+2][i]==".":
                        portals[(i,j+1)]=nameportal
                    else:
                        portals[(i,j)]=nameportal
                elif i+1 <len(line)  and st[j][i+1] in string.ascii_uppercase:
                    nameportal=line[i:i+2]

                    if i+2 <len(line)  and st[j][i+2]==".":
                        portals[(i+1,j)]=nameportal
                    else:
                        portals[(i,j)]=nameportal


    #get starting point and finish point
    pstart=[p for p in portals if portals[p]=="AA"]
    pfinish=[p for p in portals if portals[p]=="ZZ"]
    for lrud in LRUD:
        x1,y1=pstart[0]
        x2,y2=pfinish[0]
        dx, dy = lrud
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        if (nx1,ny1) in d and d[(nx1,ny1)]==".":
            xstart=nx1
            ystart=ny1
        if (nx2,ny2) in d and d[(nx2,ny2)]==".":
            xfinish=nx2
            yfinish=ny2

    tiletoexplore = deque([])
    tiletoexplore.append((xstart, ystart, 0))
    positions = set()
    while len(tiletoexplore) != 0:
        tile = tiletoexplore.popleft()
        print(tile)
        for lrud in LRUD:
            xt, yt, step = tile
            step += 1
            dx, dy = lrud
            nx, ny = xt + dx, yt + dy

            if (nx,ny)==(xfinish,yfinish):
                print(step)
                return(step)
            if (not (
                (nx,ny) in d
                and (d[(nx,ny)]=="." or (nx,ny) in portals)
                )
            ):
                continue
            elif ((nx,ny) in d
                and d[(nx,ny)]=="."
            ):
                
                if (nx, ny) not in positions:
                    # print("crawl inner",nx,ny)
                    positions.add((nx, ny))
                    tiletoexplore.append((nx, ny, step))
            elif ((nx,ny) in d
                and (nx,ny) in portals
            ):
                nx2,ny2,step2= teleport(nx,ny,step,portals)

                if (nx2, ny2) not in positions:
                    print(nx,ny,"teleport",nx2,ny2)
                    positions.add((nx2, ny2))
                    tiletoexplore.append((nx2, ny2, step2))
    print(xfinish,yfinish)
    return 0


def teleport(x,y,step,dportal):
    if (x,y) not in dportal:
        return (x,y,step+1)
    value=dportal[(x,y)]
    portals=[p for p in dportal if dportal[p]==value]
    
    print(value,portals)
    if len(portals)<2:
        return (x,y,step+1)
    for po in portals:
        if po!=(x,y):
            return (*po,step-1)
    return  (x,y,step+1)


    


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


def part2(st, parttwo):
    d = dict()
    portals=dict()
    xstart,ystart,xfinish,yfinish=0,0,0,0
    outerportal=[]
    for j in range(len(st)):
        line = st[j]
        for i in range(len(line)):
            d[(i, j)] = line[i]
            if line[i] in string.ascii_uppercase:
                nameportal=""
                if j+1 < len(st) and st[j+1][i] in string.ascii_uppercase:
                    nameportal=line[i]+st[j+1][i]
                    if j+2 < len(st) and st[j+2][i]==".":
                        portals[(i,j+1)]=nameportal

                        if j==0 or j+2==len(st):
                            outerportal.append((i,j+1))

                    else:
                        portals[(i,j)]=nameportal

                        if j==0 or j+2==len(st):
                            outerportal.append((i,j))
                    
                    
                elif i+1 <len(line)  and st[j][i+1] in string.ascii_uppercase:
                    nameportal=line[i:i+2]

                    if i+2 <len(line)  and st[j][i+2]==".":
                        portals[(i+1,j)]=nameportal
                        
                        if i==0 or i+2==len(line):
                            outerportal.append((i+1,j))
                    else:
                        portals[(i,j)]=nameportal

                        if i==0 or i+2==len(line):
                            outerportal.append((i,j))

    #get starting point and finish point
    pstart=[p for p in portals if portals[p]=="AA"]
    pfinish=[p for p in portals if portals[p]=="ZZ"]
    for lrud in LRUD:
        x1,y1=pstart[0]
        x2,y2=pfinish[0]
        dx, dy = lrud
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        if (nx1,ny1) in d and d[(nx1,ny1)]==".":
            xstart=nx1
            ystart=ny1
        if (nx2,ny2) in d and d[(nx2,ny2)]==".":
            xfinish=nx2
            yfinish=ny2

    startinglevel=0
    tiletoexplore = deque([])
    tiletoexplore.append((xstart, ystart, startinglevel, 0))
    positions = set()
    while len(tiletoexplore) != 0:
        tile = tiletoexplore.popleft()
        print(tile)
        for lrud in LRUD:
            xt, yt,level, step = tile
            step += 1
            dx, dy = lrud
            nx, ny = xt + dx, yt + dy

            if (nx,ny)==(xfinish,yfinish) and level==0:
                print(step)
                return(step)
            if (not (
                (nx,ny) in d
                and (d[(nx,ny)]=="." or (nx,ny) in portals)
                )
            ):
                continue
            elif ((nx,ny) in d
                and d[(nx,ny)]=="."
            ):
                
                if (nx, ny,level) not in positions:
                    # print("crawl inner",nx,ny)
                    positions.add((nx, ny, level))
                    tiletoexplore.append((nx, ny, level, step))
            elif ((nx,ny) in d
                and (nx,ny) in portals
            ):
                nx2,ny2,step2= teleport(nx,ny,step,portals)


                if (nx2, ny2,level) not in positions:
                    print(nx,ny,"teleport",nx2,ny2)
                    if (nx,ny) in outerportal:
                        level+=1
                    else:
                        level+=-1
                    positions.add((nx2, ny2,level))
                    tiletoexplore.append((nx2, ny2,level, step2))
    print(xfinish,yfinish)
    return 0

#part1(numbers, False)
part2(numbers, False)

