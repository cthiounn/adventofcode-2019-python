from collections import Counter

with open('data/my_input/day4-input.file',"r") as f:
    min,max = f.readline().split("-")

def part1and2(min,max): 
    print(min,max)
    count1= [x for x in range(int(min),int(max)) if ''.join(sorted(str(x)))==str(x) and any(d>=2  for d in Counter(str(x)).values())]
    print(len(count1))
    count2= [x for x in range(int(min),int(max)) if ''.join(sorted(str(x)))==str(x) and any(d==2  for d in Counter(str(x)).values())]
    print(len(count2))

part1and2(min,max)