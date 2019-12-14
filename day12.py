import re
with open("data/my_input/day12-input.file","r") as f:
    coords=[lines.strip() for lines in f]

def part1(l):
    i=0
    moons=dict()
    velocities=dict()
    for s in l:
        x,y,z=re.findall("-?\d+",s)
        moons[i]=[int(x),int(y),int(z)]
        velocities[i]=[0,0,0]
        i+=1

    stop=False
    step=0
    pos_velx=set()
    pos_vely=set()
    pos_velz=set()
    first_step=dict()
    while(not stop):
        xgalaxy="!".join(map(str,(moons[0][0],velocities[0][0],moons[1][0],velocities[1][0],moons[2][0],velocities[2][0],moons[3][0],velocities[3][0])))
        ygalaxy="!".join(map(str,(moons[0][1],velocities[0][1],moons[1][1],velocities[1][1],moons[2][1],velocities[2][1],moons[3][1],velocities[3][1])))
        zgalaxy="!".join(map(str,(moons[0][2],velocities[0][2],moons[1][2],velocities[1][2],moons[2][2],velocities[2][2],moons[3][2],velocities[3][2])))
        if  xgalaxy not in pos_velx:
            pos_velx.add(xgalaxy)
        else:
            if 0 not in first_step:
                first_step[0]=step
        if  ygalaxy not in pos_vely:
            pos_vely.add(ygalaxy)
        else:
            if 1 not in first_step:
                first_step[1]=step
        if  (zgalaxy) not in pos_velz:
            pos_velz.add(zgalaxy)
        else:
            if 2 not in first_step:
                first_step[2]=step
        
        #calculate new velocities
        for i in range(3):
            for j in range(i+1,4):
                for axis in range(3):
                    if moons[i][axis]>moons[j][axis]:
                        velocities[i][axis]-=1
                        velocities[j][axis]+=1
                    elif moons[i][axis]<moons[j][axis]:
                        velocities[i][axis]+=1
                        velocities[j][axis]-=1
        #move moons
        for i in range(4):
            for axis in range(3):
                moons[i][axis] +=velocities[i][axis]
         
        step+=1     
        if step==1000:
            total_energy=0
            for i in range(4):
                total_energy+=(abs(moons[i][0])+abs(moons[i][1])+abs(moons[i][2])) *  (abs(velocities[i][0])+abs(velocities[i][1])+abs(velocities[i][2]))
            print(total_energy)
        if 1 in first_step and 0 in first_step and 2 in first_step:
            stop=True
    print(int(lcd(lcd(first_step[0],first_step[1]),first_step[2])))

def gcd(a,b):
    if b==0: return a
    else: return gcd(b,a % b)

def lcd(a,b):
    if a==0 or b==0: return 0
    else: return a*b/gcd(a,b)

part1(coords)