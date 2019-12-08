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
    min=100
    minProduct=0
    for l in layers:
        if Counter(l)["0"] < min:
            min = Counter(l)["0"]
            minProduct=Counter(l)["2"]*Counter(l)["1"]
    
    print(minProduct)

    lp=layers[::-1] 
    first=lp.pop()

    while (lp):
        first=addLayer(first,lp.pop()) 

    n = wide
    formatted = [first[i:i+n] for i in range(0, len(first), n)]
    for fo in formatted:
        print(fo) 


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