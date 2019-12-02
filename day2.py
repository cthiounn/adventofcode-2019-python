with open('data/my_input/day2-input.file') as f:
    numbers = [ line.strip() for line in f]

def part1(st,noun,verb,search):
    listOfNumber=list(map(int,st.split(",")))
    i=0
    listOfNumber[1]=noun
    listOfNumber[2]=verb
    stop= False
    while not stop : 
        ref2=listOfNumber[i+1]
        ref3=listOfNumber[i+2]
        ref4=listOfNumber[i+3]
        if (listOfNumber[i]==1):
            listOfNumber[ref4]=listOfNumber[ref2]+listOfNumber[ref3]
        elif (listOfNumber[i]==2):
            listOfNumber[ref4]=listOfNumber[ref2]*listOfNumber[ref3]
        elif (listOfNumber[i]==99):
            stop= True
        i+=4
    
    if search and listOfNumber[0]==19690720:
        print(100*noun+verb)
    elif not search:
        print(listOfNumber[0])
    
def part2(st):
    for noun in range(100):
        for verb in range(100):
            part1(st,noun,verb,True)


part1(numbers[0],12,2,False)
part2(numbers[0])