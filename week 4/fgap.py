from time import sleep
import random
import math
from copy import copy
import time
#import matplotlib.pyplot as plt
'''def plot(a,b):
    plt.plot(a)
    plt.plot(b)
    plt.show()
'''
def createrandom(bit_size):
    return random.randrange(0,2**(bit_size))
def compute(x1,x2,upper_limit):
    global bit_size,rank
    x1=(float(upper_limit)/((2**bit_size)-1))*int(x1,2)
    x2=(float(upper_limit)/((2**bit_size)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    try:
        return s(x1-2+(rank*(upper_limit_i/3)))/(x1-2+(rank*(upper_limit_i/3))) + s(x2-2+(rank*(upper_limit_i/3)))/(x2-2+(rank*(upper_limit_i/3)))+(s(x1-20+(rank*(upper_limit_i/3)))/(x1-20+(rank*(upper_limit_i/3))) + s(x2-20+(rank*(upper_limit_i/3)))/(x2-20+(rank*(upper_limit_i/3))))
    except ZeroDivisionError:
        x1+=0.0000001
        x2+=0.0000001
        return s(x1-2+(rank*(upper_limit_i/3)))/(x1-2+(rank*(upper_limit_i/3))) + s(x2-2+(rank*(upper_limit_i/3)))/(x2-2+(rank*(upper_limit_i/3)))+(s(x1-20+(rank*(upper_limit_i/3)))/(x1-20+(rank*(upper_limit_i/3))) + s(x2-20+(rank*(upper_limit_i/3)))/(x2-20+(rank*(upper_limit_i/3))))
def binary_encode(x1):
    global bit_size
    return bin(x1)[2:].zfill(bit_size)
def sp_crossover(x1,x2):
    for i in range(random.randrange(0,2*bit_size),2*bit_size):
        x1[i],x2[i]=x2[i],x1[i]

#sorting subroutine###########################################################
def build_max_heap(a):
    for i in range((len(a)/2)-1,-1,-1):
        max_heapify(a,i)
    return a
def left(i):
    return (2*i)+1
def right(i):
    return (2*i)+2
def max_heapify(a,i):
    l=left(i)
    r=right(i)
    if l<len(a) and compute(a[l][:bit_size],a[l][bit_size:],upper_limit)>compute(a[i][:bit_size],a[i][bit_size:],upper_limit):
        largest=l
    else:
        largest=i
    if r<len(a) and compute(a[r][:bit_size],a[r][bit_size:],upper_limit)>compute(a[largest][:bit_size],a[largest][bit_size:],upper_limit):
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        max_heapify(a,largest)

def heapsort(a):
    b=[]
    build_max_heap(a)
    for i in range(0,len(a)-1):
        a[0],a[-1]=a[-1],a[0]
        b.append(a.pop(-1))
        max_heapify(a,0)
    b.append(a.pop(-1))
    return b
###############################################################################
from mpi4py import MPI
comm=MPI.COMM_WORLD
global rank
rank=comm.rank
size=comm.size

#population_number=10#input('Population Number::')
bit_size=10#input('Bit Size::')
bit_size=int(round(bit_size-(math.log(3)/math.log(2))))
population_number=bit_size*2
if bit_size<8:
    iteration=1000#input('Number of generations::')
else:
    iteration=10000 
upper_limit=50#input("Upper Limit::")
upper_limit_i=upper_limit
upper_limit=((rank+1)*upper_limit/3)-(rank*(upper_limit/3))
start_time=time.time()
gl_max=[]
if rank ==0:
    #print bit_size,upper_limit
    a=[]
    mating_pool=[]
    for i in range(population_number):
        r1=binary_encode(createrandom(bit_size))
        r2=binary_encode(createrandom(bit_size))
        for i in range(2):
            a.append(r1+r2)
    #population generated
            
    #selection starts
    while len(mating_pool)<population_number:
        r1=random.randrange(0,len(a))
        r2=random.randrange(0,len(a))
        if a[r1]!=a[r2]:
            if compute(a[r1][:bit_size],a[r1][bit_size:],upper_limit)>=compute(a[r2][:bit_size],a[r2][bit_size:],upper_limit):
                mating_pool.append(a.pop(r1))
            else:
                mating_pool.append(a.pop(r2))


    # mating_pool generated
    #sorting_subroutine##################################################################################

    mating_pool=[list(i) for i in heapsort(mating_pool)]


    #####################################################################################################
    mating_pool[population_number/2:]=mating_pool[:population_number/2]
    c_cnt=0
    while c_cnt<population_number/2:
        t1=random.randrange(population_number/2,population_number)
        t2=random.randrange(population_number/2,population_number)
        if t1!=t2:
            sp_crossover(mating_pool[t1],mating_pool[t2])
            c_cnt+=1

    # crossover complete

    #mutation initiation
    # initializing mutation
    for i in range(population_number):
        for j in range(2*bit_size):
            if random.random()<.02:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else :
                    mating_pool[i][j]='0'
    for i in range(population_number):
        mating_pool[i]=''.join(mating_pool[i])
    # mutation done
    # propagation
    a=[]
    fitness=[]
    gl_cntl=[]
    gl_cnt=(binary_encode(0)+binary_encode(0))
    it_cnt=0
    #for i in range(iteration):
    while 1:

        #sorting_subroutine##################################################################################

        mating_pool=[list(i) for i in heapsort(mating_pool)]
        p=''.join(mating_pool[0])
        if compute(p[:bit_size],p[bit_size:],upper_limit)>compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit):
            gl_cnt=p

        #####################################################################################################
        mating_pool[population_number/2:]=mating_pool[:population_number/2]
        c_cnt=0
        while c_cnt<population_number/2:
            t1=random.randrange(population_number/2,population_number)
            t2=random.randrange(population_number/2,population_number)
            if t1!=t2:
                sp_crossover(mating_pool[t1],mating_pool[t2])
                c_cnt+=1

        # crossover complete

        #mutation initiation
        # initializing mutation
        for i in range(population_number):
            for j in range(2*bit_size):
                if random.random()<.02:
                    if mating_pool[i][j]=='0':
                        mating_pool[i][j]='1'
                    else :
                        mating_pool[i][j]='0'
        for i in range(population_number):
            mating_pool[i]=''.join(mating_pool[i])
        #mutation done
        fitness.append(sum([compute(mating_pool[i][:bit_size],mating_pool[i][bit_size:],upper_limit) for i in range(len(mating_pool))])/population_number)
        gl_cntl.append(compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit))
        ##########convergence###########
        if it_cnt>=iteration and compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit)-fitness[-1]<=0.004:
            break
        it_cnt+=1
    gl_cnt=[((float(upper_limit)/(2**bit_size))*int(gl_cnt[:bit_size],2))+(rank*(upper_limit_i/3)),((float(upper_limit)/(2**bit_size))*int(gl_cnt[bit_size:],2))+(rank*(upper_limit_i/3)),gl_cntl[-1]]
    gl_max.append(gl_cnt)
    gl_max.append(comm.recv(source=1))
    gl_max.append(comm.recv(source=2))
    print gl_max
if rank ==1:
    #print bit_size,upper_limit
    a=[]
    mating_pool=[]
    for i in range(population_number):
        r1=binary_encode(createrandom(bit_size))
        r2=binary_encode(createrandom(bit_size))
        for i in range(2):
            a.append(r1+r2)
    #population generated
            
    #selection starts
    while len(mating_pool)<population_number:
        r1=random.randrange(0,len(a))
        r2=random.randrange(0,len(a))
        if a[r1]!=a[r2]:
            if compute(a[r1][:bit_size],a[r1][bit_size:],upper_limit)>=compute(a[r2][:bit_size],a[r2][bit_size:],upper_limit):
                mating_pool.append(a.pop(r1))
            else:
                mating_pool.append(a.pop(r2))


    # mating_pool generated
    #sorting_subroutine##################################################################################

    mating_pool=[list(i) for i in heapsort(mating_pool)]


    #####################################################################################################
    mating_pool[population_number/2:]=mating_pool[:population_number/2]
    c_cnt=0
    while c_cnt<population_number/2:
        t1=random.randrange(population_number/2,population_number)
        t2=random.randrange(population_number/2,population_number)
        if t1!=t2:
            sp_crossover(mating_pool[t1],mating_pool[t2])
            c_cnt+=1

    # crossover complete

    #mutation initiation
    # initializing mutation
    for i in range(population_number):
        for j in range(2*bit_size):
            if random.random()<.02:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else :
                    mating_pool[i][j]='0'
    for i in range(population_number):
        mating_pool[i]=''.join(mating_pool[i])
    # mutation done
    # propagation
    a=[]
    fitness=[]
    gl_cntl=[]
    gl_cnt=(binary_encode(0)+binary_encode(0))
    it_cnt=0
    #for i in range(iteration):
    while 1:

        #sorting_subroutine##################################################################################

        mating_pool=[list(i) for i in heapsort(mating_pool)]
        p=''.join(mating_pool[0])
        if compute(p[:bit_size],p[bit_size:],upper_limit)>compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit):
            gl_cnt=p

        #####################################################################################################
        mating_pool[population_number/2:]=mating_pool[:population_number/2]
        c_cnt=0
        while c_cnt<population_number/2:
            t1=random.randrange(population_number/2,population_number)
            t2=random.randrange(population_number/2,population_number)
            if t1!=t2:
                sp_crossover(mating_pool[t1],mating_pool[t2])
                c_cnt+=1

        # crossover complete

        #mutation initiation
        # initializing mutation
        for i in range(population_number):
            for j in range(2*bit_size):
                if random.random()<.02:
                    if mating_pool[i][j]=='0':
                        mating_pool[i][j]='1'
                    else :
                        mating_pool[i][j]='0'
        for i in range(population_number):
            mating_pool[i]=''.join(mating_pool[i])
        #mutation done
        fitness.append(sum([compute(mating_pool[i][:bit_size],mating_pool[i][bit_size:],upper_limit) for i in range(len(mating_pool))])/population_number)
        gl_cntl.append(compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit))
        ##########convergence###########
        if it_cnt>=iteration and compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit)-fitness[-1]<=0.004:
            break
        it_cnt+=1
    gl_cnt=[((float(upper_limit)/(2**bit_size))*int(gl_cnt[:bit_size],2))+(rank*(upper_limit_i/3)),((float(upper_limit)/(2**bit_size))*int(gl_cnt[bit_size:],2))+(rank*(upper_limit_i/3)),gl_cntl[-1]]
    comm.send(gl_cnt,dest=0)
if rank ==2:
    #print bit_size,upper_limit
    a=[]
    mating_pool=[]
    for i in range(population_number):
        r1=binary_encode(createrandom(bit_size))
        r2=binary_encode(createrandom(bit_size))
        for i in range(2):
            a.append(r1+r2)
    #population generated
            
    #selection starts
    while len(mating_pool)<population_number:
        r1=random.randrange(0,len(a))
        r2=random.randrange(0,len(a))
        if a[r1]!=a[r2]:
            if compute(a[r1][:bit_size],a[r1][bit_size:],upper_limit)>=compute(a[r2][:bit_size],a[r2][bit_size:],upper_limit):
                mating_pool.append(a.pop(r1))
            else:
                mating_pool.append(a.pop(r2))


    # mating_pool generated
    #sorting_subroutine##################################################################################

    mating_pool=[list(i) for i in heapsort(mating_pool)]


    #####################################################################################################
    mating_pool[population_number/2:]=mating_pool[:population_number/2]
    c_cnt=0
    while c_cnt<population_number/2:
        t1=random.randrange(population_number/2,population_number)
        t2=random.randrange(population_number/2,population_number)
        if t1!=t2:
            sp_crossover(mating_pool[t1],mating_pool[t2])
            c_cnt+=1

    # crossover complete

    #mutation initiation
    # initializing mutation
    for i in range(population_number):
        for j in range(2*bit_size):
            if random.random()<.02:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else :
                    mating_pool[i][j]='0'
    for i in range(population_number):
        mating_pool[i]=''.join(mating_pool[i])
    # mutation done
    # propagation
    a=[]
    fitness=[]
    gl_cntl=[]
    gl_cnt=(binary_encode(0)+binary_encode(0))
    it_cnt=0
    #for i in range(iteration):
    while 1:

        #sorting_subroutine##################################################################################

        mating_pool=[list(i) for i in heapsort(mating_pool)]
        p=''.join(mating_pool[0])
        if compute(p[:bit_size],p[bit_size:],upper_limit)>compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit):
            gl_cnt=p

        #####################################################################################################
        mating_pool[population_number/2:]=mating_pool[:population_number/2]
        c_cnt=0
        while c_cnt<population_number/2:
            t1=random.randrange(population_number/2,population_number)
            t2=random.randrange(population_number/2,population_number)
            if t1!=t2:
                sp_crossover(mating_pool[t1],mating_pool[t2])
                c_cnt+=1

        # crossover complete

        #mutation initiation
        # initializing mutation
        for i in range(population_number):
            for j in range(2*bit_size):
                if random.random()<.02:
                    if mating_pool[i][j]=='0':
                        mating_pool[i][j]='1'
                    else :
                        mating_pool[i][j]='0'
        for i in range(population_number):
            mating_pool[i]=''.join(mating_pool[i])
        #mutation done
        fitness.append(sum([compute(mating_pool[i][:bit_size],mating_pool[i][bit_size:],upper_limit) for i in range(len(mating_pool))])/population_number)
        gl_cntl.append(compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit))
        ##########convergence###########
        if it_cnt>=iteration and compute(gl_cnt[:bit_size],gl_cnt[bit_size:],upper_limit)-fitness[-1]<=0.004:
            break
        it_cnt+=1
    gl_cnt=[((float(upper_limit)/(2**bit_size))*int(gl_cnt[:bit_size],2))+(rank*(upper_limit_i/3)),((float(upper_limit)/(2**bit_size))*int(gl_cnt[bit_size:],2))+(rank*(upper_limit_i/3)),gl_cntl[-1]]
    comm.send(gl_cnt,dest=0)
    

