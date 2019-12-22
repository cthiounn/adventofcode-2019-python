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


def part2(st):
    st.reverse()
    j=2020
    #101741582076661
    for k in range(10000):
        print(k-1,j)
        for s in st:
                stack=re.findall("new stack",s)
                increment=re.findall("increment",s)
                cut=re.findall("cut",s)
                num=re.findall("-?\d+",s)

                if len(stack)!=0:
                    j=119315717514047-1-j
                elif len(cut)!=0:
                    # print("before",j)
                    index=int(num[0])
                    j=j+index+119315717514047
                    j%=119315717514047
                    # print(j,index)
                elif(len(increment)!=0):
                    inc=int(num[0])
                    mod= j% inc
                    negativemod= mod-inc
                    j=abs(negativemod)*inc + (j+abs(negativemod)) //inc 
    


part2(numbers)