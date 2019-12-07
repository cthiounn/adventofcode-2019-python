import itertools
from collections import deque
import unittest


with open('data/my_input/day7-input.file') as f:
    numbers = [ line.strip() for line in f]

def intCode(l,inp,begin):
    i=begin 
    stop= False if begin!=-1 else True
    while not stop : 
        r2=l[i+1] if i+1 <len(l) else 0
        r3=l[i+2] if i+2 <len(l) else 0
        r4=l[i+3] if i+3 <len(l) else 0
        c=l[i]%10
        p1=r2 if (l[i]%1000 >= 100 or c==3 or c==9) else l[r2]
        p2=r3 if (l[i]%10000 >= 1000) else 0 if (c==3 or c==4 or c==9) else l[r3]
        if (c==1):
            l[r4]=p1+p2
            i+=4
        elif (c==2):
            l[r4]=p1*p2
            i+=4
        elif (c==3):
            l[r2]=inp.popleft()
            i+=2
        elif (c==4):
            return (p1,i+2)
        elif (c==5):
            if(p1!=0):
                i=p2
            else:
                i+=3
        elif (c==6):
            if(p1==0):
                i=p2
            else:
                i+=3
        elif (c==7):
            l[r4]= 1 if p1<p2  else 0
            i+=4
        elif (c==8):
            l[r4]= 1 if p1==p2  else 0
            i+=4
        elif (l[i]==99):
            stop= True
            i=-1
        else:
            print("???")
    return ( False,i)

def part1(st,phases,partTwo):
    l=list(map(int,st.split(",")))
    max=0
    for p in itertools.permutations(phases):    
        l1=l.copy()
        l2=l.copy()
        l3=l.copy()
        l4=l.copy()
        l5=l.copy()
        i1=0
        i2=0
        i3=0
        i4=0
        i5=0
        q1=deque([int(p[0]),0])
        q2=deque([int(p[1])])
        q3=deque([int(p[2])])
        q4=deque([int(p[3])])
        q5=deque([int(p[4])])
        i=0
        while q1 or q2 or q3 or q4 or q5 :
            try :
                o1,i1 = intCode(l1,q1,i1)
                if o1:
                    q2.append(o1)
                if i1==-1:
                    break
                o2,i2 =intCode(l2,q2,i2)
                if o2:
                    q3.append(o2)
                if i2==-1:
                    break
                o3,i3 =intCode(l3,q3,i3)
                if o3:
                    q4.append(o3)
                if i3==-1:
                    break
                o4,i4 =intCode(l4,q4,i4)
                if o4:
                    q5.append(o4)
                if i4==-1:
                    break
                o5,i5 =intCode(l5,q5,i5) 
                if i5==-1:
                    break
                if o5 and partTwo:
                    q1.append(o5)
                max= o5 if o5 > max else max 
            except IndexError:
                break 
    return max



assert(part1("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0","01234",False)==43210)
assert(part1("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0","01234",False)==54321)
assert(part1("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0","01234",False)==65210)
assert(part1("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5","56789",True)==139629729)
assert(part1("3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10","56789",True)==18216) 
print(part1(numbers[0],"01234",False))
print(part1(numbers[0],"56789",True))