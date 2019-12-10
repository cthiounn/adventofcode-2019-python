import math
import sys


with open('data/other_input/day10-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st): 
    d=dict()
    i=0
    for l in st:
        for j in range(len(l)):
            if l[j]=="#":
                d[(j,i)]=str(j)+"!"+str(i)
        i+=1
        
    j=[(l,ra(l,d)) for l in d.keys()]
    maxStation=max(j,key=lambda a:a[1])
    print(maxStation[1])
    print(maxStation)
    maxStationCoord=maxStation[0]

    topRightCoordinate=(len(st[0]),0)
    bottomRightCoordinate=(len(st[0]),len(st))
    topLeftCoordinate=(0,0)
    bottomLeftCoordinate=(0,len(st))
    countAstDestroyed=0
    while countAstDestroyed!=200:
        dAst=dict()
        for l in d:
            if between(l,maxStationCoord,topRightCoordinate) and l!=maxStationCoord and l[1]!=maxStationCoord[1]:
                dAst[l]=abs((l[0]-maxStationCoord[0])/(l[1]-maxStationCoord[1]))
        p=sorted(list(set(dAst.values())))
        for i in p:
            print(i)
            kdest= min([k for k,v in dAst.items() if v==i],key=lambda a : md(a,maxStationCoord))
            del d[kdest]
            countAstDestroyed+=1
            print(countAstDestroyed,kdest)
            if countAstDestroyed==200:
                print("winner",kdest)
                break
        if len(dAst.keys())==0:
            break 
        print("------ first quadrant ",countAstDestroyed)
        # rotate
        dAst=dict()
        for l in d:
            if between(l,maxStationCoord,bottomRightCoordinate) and l!=maxStationCoord and l[0]!=maxStationCoord[0]:
                dAst[l]=abs((l[1]-maxStationCoord[1])/(l[0]-maxStationCoord[0]))
        p=sorted(list(set(dAst.values())))
        for i in p:
            kdest= min([k for k,v in dAst.items() if v==i],key=lambda a : md(a,maxStationCoord))
            del d[kdest]
            countAstDestroyed+=1
            print(countAstDestroyed,kdest)
            if countAstDestroyed==200:
                print("winner",kdest)
                break
        if len(dAst.keys())==0:
            break 
        # rotate
        dAst=dict()
        for l in d:
            if between(l,maxStationCoord,bottomLeftCoordinate) and l!=maxStationCoord and l[1]!=maxStationCoord[1]:
                dAst[l]=abs((l[0]-maxStationCoord[0])/(l[1]-maxStationCoord[1]))
        p=sorted(list(set(dAst.values())))
        for i in p:
            kdest= min([k for k,v in dAst.items() if v==i],key=lambda a : md(a,maxStationCoord))
            del d[kdest]
            countAstDestroyed+=1
            print(countAstDestroyed,kdest)
            if countAstDestroyed==200:
                print("winner",kdest)
                break
        if len(dAst.keys())==0:
            break 
                # rotate
        dAst=dict()
        for l in d:
            if between(l,maxStationCoord,topLeftCoordinate) and l!=maxStationCoord and l[0]!=maxStationCoord[0]:
                dAst[l]=abs((l[1]-maxStationCoord[1])/(l[0]-maxStationCoord[0]))
        p=sorted(list(set(dAst.values())))
        for i in p:
            kdest= min([k for k,v in dAst.items() if v==i],key=lambda a : md(a,maxStationCoord))
            del d[kdest]
            countAstDestroyed+=1
            print(countAstDestroyed,kdest)
            if countAstDestroyed==200:
                print("winner",kdest)
                break
        if len(dAst.keys())==0:
            break 

    

def can_see(a,b,d):
    x,y =a
    x1,y1=b
    ratio=(x1-x)/(y1-y) if y1-y!=0 else math.inf
    for l in d.keys():
        if l!=a and l!=b  and between(l,a,b) :
            x2,y2=l
            ratio2=(x2-x)/(y2-y) if y2-y!=0 else math.inf
            if ratio2==ratio and md(a,b) >md(a,l): 
                return False
    return True
  
def ra(a,d): 
    count=0
    for ast in d.keys():
        if ast!=a and can_see(a,ast,d):
            count+=1
    return count

def md(a,b):
    x,y=a
    x1,y1=b
    return abs(x-x1)+abs(y-y1)

def between(l,a,b):
    x,y=a
    s,t=b
    xmin=min(x,s)
    xmax=max(x,s)
    ymin=min(y,t)
    ymax=max(y,t)
    r,w=l
    return xmin<=r and r<=xmax and ymin<=w and w<=ymax

part1(numbers)