import math

with open('data/my_input/day1-input.file') as f:
    numbers = [ int(line.strip()) for line in f]

def calculateFuel(n):
    return math.floor(n/3)-2

def calculateFuelIterate(n):
    if n<=0:
        return 0
    elif (calculateFuel(n))<=0 :
        return 0
    else :
        return calculateFuel(n)+calculateFuelIterate(calculateFuel(n))

print(sum(map(calculateFuel,numbers)))
print(sum(map(calculateFuelIterate,numbers)))