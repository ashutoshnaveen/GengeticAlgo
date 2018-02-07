'''tournament selection'''
import random
import math
from copy import copy
def createrandom():
    return random.randrange(0,256)
def compute(x1,x2):
    x1=(float(90)/((2**8)-1))*int(x1,2)
    x2=(float(90)/((2**8)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
def binary_encode(x1):
    return bin(x1)[2:].zfill(8)
def sp_crossover(x1,x2):
    for i in range(random.randrange(0,16),16):
        x1[i],x2[i]=x2[i],x1[i]

''' Selection starts '''

a=[]
mating_pool=[]
for i in range(8):
    r1=binary_encode(createrandom())
    r2=binary_encode(createrandom())
    for i in range(2):
        a.append(r1+r2)
b=copy(a)    
while 1:
    l=len(a)
    a1=random.randrange(0,l)
    b1=random.randrange(0,l)
    print a1,b1
    if a[a1]!=a[b1]:
        if cmp(compute(a[a1][:8],a[a1][8:]),compute(a[b1][:8],a[b1][8:]))==1:
            mating_pool.append(a.pop(a1))
        else:
            mating_pool.append(a.pop(b1))
    if len(mating_pool)==8:
        break

    print mating_pool




# mating pool is generated; so now crossover and mutation is to be applied #0
cross_counter=0
for i in range(8):
    mating_pool[i]=list(mating_pool[i])
while 1:
    A1=random.randrange(0,8)
    B1=random.randrange(0,8)
    if cross_counter<8:
        if A1!=B1:
            sp_crossover(mating_pool[A1],mating_pool[B1])
            cross_counter+=1
    else:
        break
# mutation of mating pool #0
for i in range(8):
    for j in range(16):
        if random.random()<=0.05:
            if mating_pool[i][j]=='0':
                mating_pool[i][j]='1'
            else:
                mating_pool[i][j]='0'
    mating_pool[i]=''.join(mating_pool[i])





for i in range(8):
    mating_pool.insert(i+1,mating_pool[i])
a=mating_pool
mating_pool=[]
number=0
counter=0
c1_max=0
m1_max=0
n1_max=0
number_max=0
for i in range(100000):
    while len(a)>8:
        l=len(a)
        a1=random.randrange(0,l)
        b1=random.randrange(0,l)
        if a[a1]!=a[b1]:
            if cmp(compute(a[a1][:8],a[a1][8:]),compute(a[b1][:8],a[b1][8:]))==1:
                mating_pool.append(a.pop(a1))
            else:
                mating_pool.append(a.pop(b1))
        else:
            pass






    # mating pool is generated; so now crossover and mutation is to be applied #0
    cross_counter=0
    for i in range(8):
        mating_pool[i]=list(mating_pool[i])
    while 1:
        A1=random.randrange(0,8)
        B1=random.randrange(0,8)
        if cross_counter<8:
            if A1!=B1:
                sp_crossover(mating_pool[A1],mating_pool[B1])
                cross_counter+=1
        else:
            break
    # mutation of mating pool #0
    for i in range(8):
        for j in range(16):
            if random.random()<=0.05:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else:
                    mating_pool[i][j]='0'
        mating_pool[i]=''.join(mating_pool[i])

    #checking quality of mating_pool
    c=0
    c1=0
    for i in range(0,16,2):
        c+=(compute(b[i][:8],b[i][8:]))
    for i in range(8):
        c1+=compute(mating_pool[i][:8],mating_pool[i][8:])
    print c1
    ''' final check '''
    m=[]
    n=[]
    m1=0
    n1=0
    for i in mating_pool:
        m.append(i[:8])
        n.append(i[8:])
    for i in range(8):
        m1+=(int(m[i],2)/255.0)*(90/8.0)
        n1+=(int(n[i],2)/255.0)*(90/8.0)
    number+=1
    print m1,n1
    if c1>c1_max:
        c1_max=c1
        m1_max=m1
        n1_max=n1
        number_max=number
print c1_max
print m1_max
print n1_max
print number_max
