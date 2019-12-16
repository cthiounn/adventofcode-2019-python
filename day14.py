import math

with open("data/my_input/day14-input.file") as f:
    numbers = [line.strip() for line in f]

# code heavily inspired from /u/skater_boy
def part1(lines):
    store=dict()
    reacts=dict()
    for st in lines:
        s1,s2=st.split("=>")
        inps=s1.strip().split(", ")
        out=s2.strip().split(" ")
        outname=out[1]
        outnumber=int(out[0])
        store[outname]=0
        formula=[(outname,outnumber)]
        for ip in inps:
            ipa = ip.strip().split(" ")
            inname=ipa[1]
            innumber=int(ipa[0]) 
            store[inname]=0
            formula.append((inname,innumber))
        reacts[outname]=formula
        
    store1=store.copy()
    totalOre=reduce("FUEL",1,store1,reacts)
    print(totalOre)
    print(int(searchIn(1e12,store,reacts)))


def reduce(e,n,store,reacts):
    if e=="ORE":
        return n
    else:
        tot=0
        numreq=reacts[e][0][1]
        k = math.ceil((n -store[e])/ numreq) 
        store[e] = store[e] -n + k * numreq 
        for i in range(1, len(reacts[e])):
                tot += reduce(reacts[e][i][0], k*reacts[e][i][1],store,reacts)
        return tot


def searchIn(search,store,reacts):
    infsearch=0
    supsearch=search
    while infsearch<supsearch:
        middle=(infsearch+supsearch+1)//2
        storecopy=store.copy()
        if (reduce("FUEL",middle,storecopy,reacts)<=search):
            infsearch=middle
        else :
            supsearch=middle-1
    return infsearch


part1(numbers)