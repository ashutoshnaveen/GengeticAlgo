from time import sleep
import random
import math
from copy import copy
def createrandom(bit_size):
    return random.randrange(0,2**(bit_size))
def compute(x1,x2):
    x1=(float(90)/((2**bit_size)-1))*int(x1,2)
    x2=(float(90)/((2**bit_size)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
def binary_encode(x1):
    return bin(x1)[2:].zfill(bit_size)

    
def sp_crossover(x1,x2):
    for i in range(random.randrange(0,2*bit_size),2*bit_size):
        x1[i],x2[i]=x2[i],x1[i]

def tp_crossover(x1,x2):
    a=0
    b=0
    while a==b:
        a=random.randrange(0,2*bit_size)
        b=random.randrange(0,2*bit_size)
    for i in (range(min(a,b))+range(max(a,b),2*bit_size)):
        x1[i],x2[i]=x2[i],x1[i]
population_number=input('Population Number::')
global bit_size
bit_size=input('Bit Size::')
iteration=input('Number of generations::')
# Initialization of lists

global a
a=[]
for i in range(population_number):
    r1=binary_encode(createrandom(bit_size))
    r2=binary_encode(createrandom(bit_size))
    a.append(r1+r2)
    a.append(r1+r2)
#population generated
mating_pool=[]
while len(mating_pool)<population_number:
    x1=random.randrange(0,len(a))
    x2=random.randrange(0,len(a))
    if x1!=x2:
        if cmp(compute(a[x1][:bit_size],a[x1][bit_size:]),compute(a[x2][:bit_size],a[x2][bit_size:]))==1:
            mating_pool.append(list(a.pop(x1)))                                 #converting to list in function
        else:
            mating_pool.append(list(a.pop(x2)))
# mating_pool is generated
crossover_count=0
while crossover_count<population_number:
    t1=random.randrange(0,population_number)
    t2=random.randrange(0,population_number)
    if t1!=t2:
        tp_crossover(mating_pool[t1],mating_pool[t2])
        crossover_count+=1


# mating_pool is modified by crossover
# initializing mutation
for i in range(population_number):
    for j in range(2*bit_size):
        if random.random()<.2:
            if mating_pool[i][j]=='0':
                mating_pool[i][j]='1'
            else :
                mating_pool[i][j]='0'
for i in range(population_number):
    mating_pool[i]=''.join(mating_pool[i])
# mutation done
#generating further generations
compute_counter=binary_encode(0)+binary_encode(0)
for i in range(iteration):
    c1=0
    a=[]
    for i in range(population_number):
        for i in range(2):
            a.append(mating_pool[i])
    mating_pool=[]
    while len(mating_pool)<population_number:
        x1=random.randrange(0,len(a))
        x2=random.randrange(0,len(a))
        if x1!=x2:
            if cmp(compute(a[x1][:bit_size],a[x1][bit_size:]),compute(a[x2][:bit_size],a[x2][bit_size:]))==1:
                mating_pool.append(list(a.pop(x1)))                                 #converting to list in function
            else:
                mating_pool.append(list(a.pop(x2)))
    # mating_pool is generated
    crossover_count=0
    while crossover_count<population_number:
        t1=random.randrange(0,population_number)
        t2=random.randrange(0,population_number)
        if t1!=t2:
            tp_crossover(mating_pool[t1],mating_pool[t2])
            crossover_count+=1


    # mating_pool is modified by crossover
    # initializing mutation
    for i in range(population_number):
        for j in range(2*bit_size):
            if random.random()<.2:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else :
                    mating_pool[i][j]='0'
    for i in range(population_number):
        mating_pool[i]=''.join(mating_pool[i])
    # mutation done
    for i in range(population_number):
        if compute(mating_pool[i][:bit_size],mating_pool[i][bit_size:])>compute(compute_counter[:bit_size],compute_counter[bit_size:]):
            compute_counter=mating_pool[i]
print 'Optimization complete'
print ((int(compute_counter[:bit_size],2)/float((2**bit_size)-1))*90)
print ((int(compute_counter[bit_size:],2)/float((2**bit_size)-1))*90)
sleep(5)
