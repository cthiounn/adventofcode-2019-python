with open('data/my_input/day3-input.file',"r") as f:
    numbers = [ line.strip() for line in f]

dx=dict(zip('LRUD',[-1,1,0,0]))
dy=dict(zip('LRUD',[0,0,1,-1]))
dict=[{},{}]

def part1and2(num):
    i=0
    for num in numbers:
        x=0
        y=0
        globalstep=0
        for move in num.split(','):
            direction=move[0]
            assert direction in 'LRUD'
            step=int(move[1:])
            for _ in range(step):
                globalstep+=1
                x+=dx[direction]
                y+=dy[direction]
                if (x,y) not in dict[i]:
                    dict[i][(x,y)]=globalstep
        i+=1
    common=dict[0].keys() & dict[1].keys()
    minByDistIntersect=min(abs(x)+abs(y) for (x,y) in common)
    minByStepIntersect=min(dict[0][point]+dict[1][point] for point in common)
    print(minByDistIntersect)
    print(minByStepIntersect)


part1and2(numbers)