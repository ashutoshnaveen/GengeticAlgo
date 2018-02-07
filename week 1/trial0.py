import random
import math
def createrandom(x1,x2):
    return int(round((x1+((x2-x1)*random.random()))))
def compute(x1,x2):
    x1=(90/((2**8)-1))*int(x1,2)
    x2=(90/((2**8)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
def binary_encode(x1):
    return bin(x1)[2:].zfill(8)
def sp_crossover(x1,x2):
    for i in range(random.randrange(0,16),16):
        x1[i],x2[i]=x2[i],x1[i]
# declarations / assignments of variables for reproduction #0
a=[]
b=[]
c=[]
expc=[]
cprob=[]
ccounter=0
rand=[]
sumc=0
randl=[]
mating_pool=[]
for i in range(8):
    a.append(binary_encode(createrandom(0,255)))
    b.append(binary_encode(createrandom(0,255)))
    c.append(compute(a[i],b[i]))
    sumc+=c[i]
for i in range(8):
    c[i]=c[i]/sumc
    ccounter+=c[i]
    expc.append(8*c[i])
    cprob.append(ccounter)
    rand.append(random.random())
for i in range(len(rand)):
    for j in range(len(cprob)-1,-1,-1):
        if rand[i]>cprob[j]:
            randl.append(j+1)
            break
        elif rand[i]<cprob[0]:
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
    for j in range(16):
        if random.random()<=0.2:
            if mating_pool[i][j]=='0':
                mating_pool[i][j]='1'
            else:
                mating_pool[i][j]='0'
    mating_pool[i]=''.join(mating_pool[i])

for i in range(10000):
    # extracting values from modified mating pool #1
    a=[mating_pool[i][:8] for i in range(8)]
    b=[mating_pool[i][8:] for i in range(8)]


    # again reproduction #1
    c=[]
    expc=[]
    cprob=[]
    ccounter=0
    rand=[]
    sumc=0
    randl=[]
    mating_pool=[]
    for i in range(8):
        c.append(compute(a[i],b[i]))
        sumc+=c[i]
    for i in range(8):
        c[i]=c[i]/sumc
        ccounter+=c[i]
        expc.append(8*c[i])
        cprob.append(ccounter)
        rand.append(random.random())
    for i in range(len(rand)):
        for j in range(len(cprob)-1,-1,-1):
            if rand[i]>cprob[j]:
                randl.append(j+1)
                break
            elif rand[i]<cprob[0]:
                randl.append(0)
                break
    if randl.count(any(randl))>=6:
        break
    # filling the mating pool #2
    for i in range(8):
        mating_pool.append(list(a[randl[i]]+b[randl[i]]))
    



    # mating pool is generated; so now crossover and mutation is to be applied

    for i in range(8):
        sp_crossover(mating_pool[random.randrange(0,8)],mating_pool[random.randrange(0,8)])

    # mutation of mating pool #2
    for i in range(8):
        for j in range(16):
            if random.random()<=0.2:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else:
                    mating_pool[i][j]='0'
        mating_pool[i]=''.join(mating_pool[i])



#after so much effort lets think it will work
# extracting values from modified mating pool #1
a=[mating_pool[i][:8] for i in range(8)]
b=[mating_pool[i][8:] for i in range(8)]


# again reproduction #1
c=[]
expc=[]
cprob=[]
ccounter=0
rand=[]
sumc=0
randl=[]
mating_pool=[]
for i in range(8):
    c.append(compute(a[i],b[i]))
    sumc+=c[i]
for i in range(8):
    c[i]=c[i]/sumc
    ccounter+=c[i]
    expc.append(8*c[i])
    cprob.append(ccounter)
    rand.append(random.random())
for i in range(len(rand)):
    for j in range(len(cprob)-1,-1,-1):
        if rand[i]>cprob[j]:
            randl.append(j+1)
            break
        elif rand[i]<cprob[0]:
            randl.append(0)
            break
print a
print b
print randl
