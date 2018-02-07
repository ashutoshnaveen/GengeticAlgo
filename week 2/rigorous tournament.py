'''tournament selection'''
brute_force_fitness=[]
brute_force_sol1=[]
brute_force_sol2=[]
max_average_fitness=[]
max_average_sol1=[]
max_average_sol2=[]
rig_fitness=[]
rig_sol1=[]
rig_sol2=[]
'''for o in range(10):'''
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
    if a[a1]!=a[b1]:
        if cmp(compute(a[a1][:8],a[a1][8:]),compute(a[b1][:8],a[b1][8:]))==1:
            mating_pool.append(a.pop(a1))
        else:
            mating_pool.append(a.pop(b1))
    if len(mating_pool)==8:
        break


#crossover and mutation
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


# rigorous selection
mating_pool1=copy(mating_pool)                #augmened mating_pool
for i in range(8):
    mating_pool1.insert(i+1,mating_pool[i])
a=mating_pool1
mating_pool1=[]
number=0
counter=0
c1_max=0
m1_max=0
n1_max=0
number_max=0
rigcounter0='0'
rigcounter1='0'
for i in range(5):
    while len(a)>8:
        l=len(a)
        a1=random.randrange(0,l)
        b1=random.randrange(0,l)
        if len(a)<8:
            break
        elif a[a1]!=a[b1]:
            if cmp(compute(a[a1][:8],a[a1][8:]),compute(a[b1][:8],a[b1][8:]))==1:
                mating_pool1.append(a.pop(a1))
            else:
                mating_pool1.append(a.pop(b1))
        

    # mating pool is generated; so now crossover and mutation is to be applied #0
    cross_counter=0
    for i in range(8):
        
        mating_pool1[i]=list(mating_pool1[i])
    while 1:
        A1=random.randrange(0,8)
        B1=random.randrange(0,8)
        if cross_counter<8:
            if A1!=B1:
                sp_crossover(mating_pool1[A1],mating_pool1[B1])
                cross_counter+=1
        else:
            break
    # mutation of mating pool #0
    for i in range(8):
        for j in range(16):
            if random.random()<=0.05:
                if mating_pool1[i][j]=='0':
                    mating_pool1[i][j]='1'
                else:
                    mating_pool1[i][j]='0'
        mating_pool1[i]=''.join(mating_pool1[i])
    for i in range(8):
        if compute(mating_pool1[i][:8],mating_pool1[i][8:])>compute(rigcounter0,rigcounter1):
            rigcounter0,rigcounter1=mating_pool1[i][:8],mating_pool1[i][8:]

    #checking quality of mating_pool
    c=0
    c1=0
    for i in range(0,16,2):
        c+=(compute(b[i][:8],b[i][8:]))
    for i in range(8):
        c1+=compute(mating_pool1[i][:8],mating_pool1[i][8:])


    ''' final check '''
    m=[]
    n=[]
    m1=0
    n1=0
    for i in mating_pool1:
        m.append(i[:8])
        n.append(i[8:])
    for i in range(8):
        m1+=(int(m[i],2)/255.0)*(90/8.0)
        n1+=(int(n[i],2)/255.0)*(90/8.0)
    number+=1
    if c1>c1_max:
        c1_max=c1
        m1_max=m1
        n1_max=n1
        number_max=number
        best_mating_pool=[]
        best_mating_pool.append(m)
        best_mating_pool.append(n)
    print '.' ,
brute_force_fitness.append(c1_max/8.0)
brute_force_sol1.append(m1_max)
brute_force_sol2.append(n1_max)
#print number_max
#print best_mating_pool

print "\n average of maximum case "
#taking the max case of average case
m_max='0'
n_max='0'
    
for i in range(8):
    if compute(best_mating_pool[0][i],best_mating_pool[1][i])>compute(m_max,n_max):
        m_max,n_max=best_mating_pool[0][i],best_mating_pool[1][i]

print "max average:"
max_average_fitness.append(compute(m_max,n_max))
max_average_sol1.append(int(m_max,2)*(90/255.0))
max_average_sol2.append(int(n_max,2)*(90/255.0))


print 'rigorous analysis:'
rig_fitness.append(compute(rigcounter0,rigcounter1))
rig_sol1.append(int(rigcounter0,2)*(90/255.0),)
rig_sol2.append(int(rigcounter1,2)*(90/255.0))
