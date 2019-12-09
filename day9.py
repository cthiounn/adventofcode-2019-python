import itertools
from collections import Counter
import unittest


with open('data/other_input/day9-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st,input):
    l=list(map(int,st.split(",")))
    d=dict()
    for i in range(len(l)):
        d[i]=l[i]
    i=0
    rb=0
    stop= False
    while not stop : 
        r2=ra(i+1,d)
        r3=ra(i+2,d)
        r4=ra(i+3,d)
        c=d[i]%10
        pp1=d[i]%1000//100
        pp2=d[i]%10000//1000
        pp3=d[i]//10000
        # 0 relative, 1 direct, 2 rel+rb
        if pp1==1:
            p1=r2
        elif  pp1==2:
            p1=ra(r2+rb,d)
        else:
            p1=ra(r2,d) 

        if pp2==1:
            p2=r3
        elif pp2==2 :
            p2=ra(r3+rb,d)
        else:
            p2=ra(r3,d) 

        if pp3==1:
            p3=r4
        elif pp3==2 :
            p3=r4+rb
        else:
            p3=r4

        # print(i,"##",d[i],"--",str(r2)+";"+str(p1),str(r3)+";"+str(p2),str(r4)+";")
        if (c==1):
            # print("-------","add")
            d[p3]=p1+p2
            # print("-------","add",d[p3],"in",p3)
            i+=4
        elif (c==2):
            # print("-------","mult")
            d[p3]=p1*p2
            
            # print("-------","mult",d[p3],"in",p3)
            i+=4
        elif (c==3):
            # print("-------","write inp")
            d[p3]=input
            # print("-------","write inp",d[p1],"in",p1)
            i+=2
        elif (c==4):
            # print("-------","write out")
            input=p1
            # print("-------","write out",input)
            i+=2
        elif (c==5):
            if(p1!=0):
                # print("-------","jump-diff0-true")
                i=p2
                # print("-------","jump-diff0-true","jump to",p2)
            else:
                # print("-------","jump-diff0-false")
                i+=3
        elif (c==6):
            if(p1==0):
                # print("-------","jump-eq0-true")
                i=p2
                # print("-------","jump-diff0-true","jump to",p2)
            else:
                # print("-------","jump-eq0-false")
                i+=3
        elif (c==7):
            # print("-------","less than")
            d[p3]= 1 if p1<p2  else 0
            # print("-------","less than",d[p3],"in",p3)
            i+=4
        elif (c==8):
            # print("-------","equals")
            d[p3]= 1 if p1==p2  else 0
            
            # print("-------","equals",d[p3],"in",p3)
            i+=4
        elif (d[i]==99):
            stop= True
        elif (c==9):
            # print("-------","offset","old",rb)
            rb+=p1
            # print("-------","offset","new",rb)
            i+=2
        else:
            print("???")
    print(input)

  
def ra(a,d): 
    return 0 if a not in d else d[a]


part1(numbers[0],1)
part1(numbers[0],2)