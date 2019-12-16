with open("data/other_input/day16-input.file") as f:
    numbers = [line.strip() for line in f]

def part1(st):
    l=[0,1,0,-1]
    d=dict()
    for j in range(len(st)):
        d[j]=grow(l,j+1)
    output=st
    phase=0
    while(phase!=100):
        temp=""
        for i in range(len(output)):
            # print("-----")
            tot=0
            for j in range(len(output)):
                # print(d[i][(j+1)%len(d[i])],int(output[j]),d[i][(j+1)%len(d[i])]*int(output[j]))
                tot+=d[i][(j+1)%len(d[i])]*int(output[j])
            temp+=str(tot)[-1]
        output=temp
        # print(phase)
        phase+=1    
    print(output[:8])

def grow(l,i):
    if i==1:
        return l
    else:
        m=[]
        for ii in l:
            for j in range(i):
                m.append(ii)
        return m

part1(numbers[0])