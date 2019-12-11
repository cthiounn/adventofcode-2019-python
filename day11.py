import sys
with open('data/other_input/day11-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st):
    l=list(map(int,st.split(",")))
    d=dict()
    d2=dict()

    x,y=(0,0)
    for i in range(len(l)):
        d[i]=l[i]
    i=0
    rb=0
    paint=0
    direction=0
    #0 up 1 right 2 bottom 3 left
    inp=0
    output1=0
    output2=0
    output1done=False
    output2done=False
    step=0
    globalStop=False
    inputQueue=[]
    inputQueue.append(0)
    outputQueue=[]
    while not globalStop:
        #inp=ra((x,y),d2)
        # print("reading input:",inp)
        step+=1
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
            if (c==1):
                d[p3]=p1+p2
                i+=4
            elif (c==2):
                d[p3]=p1*p2
                i+=4
            elif (c==3):
                d[p3]=inputQueue.pop()
                i+=2
            elif (c==4):
                outputQueue.append(p1)
                i+=2
                if (len(outputQueue)==2):
                    break
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
                d[p3]= 1 if p1<p2  else 0
                i+=4
            elif (c==8):
                d[p3]= 1 if p1==p2  else 0
                i+=4
            elif (d[i]==99):
                stop= True
                globalStop=True
            elif (c==9):
                rb+=p1
                i+=2
            else:
                print("???")
        try:
            output2=outputQueue.pop()
            output1=outputQueue.pop()
        except IndexError:
            break
        # print("output :",output1,output2)
        #print
        if (x,y) not in d2 :
            paint+=1
        d2[(x,y)]=output1

        # print("init d",direction)
        # print("init pos",x,y)
        # print("oo",output2)
        #turn and move
        increment=output2 if output2==1 else -1
        direction= (direction+increment)%4
        #0 up 1 right 2 bottom 3 left
        if direction==0:
            y-=1
        elif direction==1:
            x+=1
        elif direction==2:
            y+=1
        elif direction==3:
            x-=1
        # print("final d",direction)
        # print("final pos",x,y)
        inputQueue.append(ra((x,y),d2))
        printmap(d2)
        # print("info next step, pos",x,y,"; reading input",inp, "; direction", direction, ", i pointer=",i)
        # print("paint,step:",paint,step)
        # if(step==10):
        #     sys.exit()
         
    
    print(d2)
    print(paint)
    printmap(d2)

  
def ra(a,d): 
    return 0 if a not in d else d[a]

def printmap(d2):
    xmin=min([x for x,y in d2])
    ymin=min([y for x,y in d2])
    xmax=max([x for x,y in d2])
    ymax=max([y for x,y in d2])

    print(xmin,ymin,xmax,ymax)
    for i in range(xmin-1,xmax+2):
        sprint=""
        for j in range(ymin-1,ymax+2):
            sprint+= str(d2[i,j]) if (i,j) in d2 else "."
        print(sprint.replace("1","O").replace("0"," "))
part1(numbers[0])