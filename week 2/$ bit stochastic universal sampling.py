import random
import math
text_file = open('output.txt', 'w')
def createrandom():
    return random.randrange(0,16)
def compute(x1,x2):
    x1=(float(90)/((2**4)-1))*int(x1,2)
    x2=(float(90)/((2**4)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
def binary_encode(x1):
    return bin(x1)[2:].zfill(4)
def sp_crossover(x1,x2):
    for i in range(random.randrange(0,8),8):
        x1[i],x2[i]=x2[i],x1[i]

'''roullete sampling #1'''
a=[]
b=[]
c=[]
cp=[]
prob=[]
rand=[]
randl=[]
F=0
cp_counter=0
r=random.random()
mating_pool=[]
for i in range(8):
    a.append(binary_encode(createrandom()))
    b.append(binary_encode(createrandom()))
    c.append(compute(a[i],b[i]))
    F+=c[i]
for i in range(8):
    prob.append(c[i]/F)
    cp_counter+=prob[i]
    cp.append(cp_counter)
    rand.append(random.random())
for i in range(8):
    for j in range(7,-1,-1):
        if rand[i]>cp[j]:
            randl.append(j+1)
            break
        elif rand[i]<cp[0]:
            randl.append(0)
            break


# filling the mating pool #0
for i in range(8):
    mating_pool.append(list(a[randl[i]]+b[randl[i]]))


# mating pool is generated; so now crossover and mutation is to be applied #0

for i in range(8):
    sp_crossover(mating_pool[random.randrange(0,8)],mating_pool[random.randrange(0,8)])

# mutation of mating pool #0
for i in range(8):
    for j in range(8):
        if random.random()<=0.2:
            if mating_pool[i][j]=='0':
                mating_pool[i][j]='1'
            else:
                mating_pool[i][j]='0'
    mating_pool[i]=''.join(mating_pool[i])

print F
'''improvement in quality'''

for i in range(1000000):
    a=[]
    b=[]
    c=[]
    cp=[]
    prob=[]
    rand=[]
    randl=[]
    F=0
    cp_counter=0
    r=random.random()

    for i in range(8):
        a.append(mating_pool[i][0:4])
        b.append(mating_pool[i][4:])
        c.append(compute(a[i],b[i]))
        F+=c[i]

    for i in range(8):
        prob.append(c[i]/F)
        cp_counter+=prob[i]
        cp.append(cp_counter)
        rand.append(random.random())
    for i in range(8):
        for j in range(7,-1,-1):
            if rand[i]>cp[j]:
                randl.append(j+1)
                break
            elif rand[i]<cp[0]:
                randl.append(0)
                break

    # filling the mating pool #0
    mating_pool=[]
    for i in range(8):
        mating_pool.append(list(a[randl[i]]+b[randl[i]]))


    # mating pool is generated; so now crossover and mutation is to be applied #0

    for i in range(8):
        sp_crossover(mating_pool[random.randrange(0,8)],mating_pool[random.randrange(0,8)])

    # mutation of mating pool #0
    for i in range(8):
        for j in range(8):
            if random.random()<=0.2:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else:
                    mating_pool[i][j]='0'
        mating_pool[i]=''.join(mating_pool[i])
    print F
print a
print b
