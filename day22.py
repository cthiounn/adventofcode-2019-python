import sys
import string
from collections import deque
import re
import math

with open("data/other_input/day22-input.file") as f:
    numbers = [line.strip() for line in f]



def part1(st,lastcard,parttwo,loop):
    cards=[i for  i in range(0,lastcard)]
    j=0
    while j<loop:
        j+=1    
        for s in st:
            stack=re.findall("new stack",s)
            increment=re.findall("increment",s)
            cut=re.findall("cut",s)
            num=re.findall("-?\d+",s)
            #print(stack,cut,increment,num)

            if len(stack)!=0:
                # print("reversing",s)
                cards.reverse()
            elif len(cut)!=0:
                index=int(num[0])
                # print("cut",index,cards)
                cards=cards[index:]+cards[:index]
                # print("cut",cards)
            elif(len(increment)!=0):
                ncards=cards.copy()
                k=0
                j=0
                while j<len(cards):
                    ncards[k]=cards[j]
                    k+=int(num[0])
                    k=k%len(cards)
                    j+=1
                cards=ncards.copy()

    if not parttwo:
        for i,v in enumerate(cards):
            if v==2019:
                print(i)
    else:
        print(cards[2020])


#part1(numbers,10007,False,1)
part1(numbers,10007,True,1)


def part2(st,pos,c,n):
    st.reverse()
    # x0=x0=j=2020
    # x1->ax0+b
    # x2->ax1+b= a^2 x0 + ab+b
    # x3->ax2+b= a^2 x1 + ab+b = a^3 x0 + a^2b+ab+b = a^3 x0 +b(sum a^i in range(3))
    # x^n => a^n x0 +b   * (1 - a^n+1) / (1-a)
 

    a=1
    b=0
    for s in st:
            stack=re.findall("new stack",s)
            increment=re.findall("increment",s)
            cut=re.findall("cut",s)
            num=re.findall("-?\d+",s)

            if len(stack)!=0:
                b+=1
                a*=-1
                b*=-1
            elif len(cut)!=0:
                index=int(num[0])
                b+=index
            elif(len(increment)!=0):
                inc=int(num[0])
                a*=pow(inc, c-2, c)
                b*=pow(inc, c-2, c)
    a%=c
    b%=c

    an=pow(a,n,c)
    first=an*pos
    first%=c
    second=b *(an-1)*pow(a-1,c-2,c)
    second%=c
    result=first + second
    result%=c
    print(result)
    


part2(numbers,2020,119315717514047,101741582076661)