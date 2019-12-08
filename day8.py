import itertools
from collections import Counter
import unittest


with open('data/my_input/day8-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st,wide,tall):
    layers=[]
    while (st):
        layers.append(st[0:wide*tall])
        st=st[wide*tall:]
    g=[(Counter(l)["0"], Counter(l)["2"]*Counter(l)["1"]) for  l in layers ]
    print(sorted(g,key=lambda x : int(x[0]))[0][1]) 
    lp=layers[::-1] 
    pattern=lp.pop()

    while (lp):
        pattern=addLayer(pattern,lp.pop()) 

    n = wide
    formatted = [pattern[i:i+n] for i in range(0, len(pattern), n)]
    for fo in formatted:
        print(fo.replace("0",".")) 


def addLayer(p,o):
    a=""
    for i in range(len(p)):
        if p[i]=="0":
            a+="0"
        elif p[i]=="1":
            a+="1"
        else:
            a+=o[i]
    return a

part1(numbers[0],25,6)