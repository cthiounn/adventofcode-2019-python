with open('data/my_input/day5-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st,input):
    l=list(map(int,st.split(",")))
    i=0 
    stop= False
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
            l[r2]=input
            i+=2
        elif (c==4):
            input=p1
            i+=2
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
        else:
            print("???")
    print(input)
      


part1(numbers[0],1)
part1(numbers[0],5)  