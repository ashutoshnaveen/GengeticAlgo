from time import sleep
import random
import math
from copy import copy
import time
import numpy as np
#import matplotlib.pyplot as plt
'''def plot(a,b):
    plt.plot(a)
    plt.plot(b)
    plt.show()
'''
def createrandom(bit_size):
    return random.randrange(0,2**(int(bit_size)))

#previous function
'''
def compute(x1,x2,upper_limit):
    global bit_size,rank
    x1=(float(upper_limit)/((2**bit_size)-1))*int(x1,2)
    x2=(float(upper_limit)/((2**bit_size)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    try:
        return s(x1-2+(rank*(upper_limit_i/12)))/(x1-2+(rank*(upper_limit_i/12))) + s(x2-2+(rank*(upper_limit_i/12)))/(x2-2+(rank*(upper_limit_i/12)))+(s(x1-14+(rank*(upper_limit_i/12)))/(x1-14+(rank*(upper_limit_i/12))) + s(x2-14+(rank*(upper_limit_i/12)))/(x2-14+(rank*(upper_limit_i/12))))
    except ZeroDivisionError:
        x1+=0.0000001
        x2+=0.0000001
        return s(x1-2+(rank*(upper_limit_i/12)))/(x1-2+(rank*(upper_limit_i/12))) + s(x2-2+(rank*(upper_limit_i/12)))/(x2-2+(rank*(upper_limit_i/12)))+(s(x1-14+(rank*(upper_limit_i/12)))/(x1-14+(rank*(upper_limit_i/12))) + s(x2-14+(rank*(upper_limit_i/12)))/(x2-14+(rank*(upper_limit_i/12))))

'''

def compute(x,u_l,statement):                       #comprises statement as function in form of  string
    global bit_size,upper_limit_i

    #g=lambda x,y: (float(y)/((2**bit_size)-1))*int(x,2)
    f=[]
    for i in xrange(len(x)):
        f.append((float(u_l[i])/((2**bit_size)-1))*int(x[i],2))
    for i in xrange(len(f)):
        exec('x%d=f[i]'%(i+1))
        exec('x%d+=((rank*(u_l_i[%d]/n_p)))'%((i+1),i))

    p=math.pi
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    try:
        exec(statement)
        return result
        #return s(x1-2)/(x1-2) + s(x2-2)/(x2-2)+(s(x1-20)/(x1-20) + s(x2-20)/(x2-20))
        #return (-1)*(20+x1**2+x2**2-(10*(c(2*p*x1)+c(2*p*x2))))                        rastrigin function see matlab documentation
    except ZeroDivisionError:
        x1+=0.00000000001
        x2+=0.00000000001
        exec(statement)
        return result
        #return s(x1-2)/(x1-2) + s(x2-2)/(x2-2)+(s(x1-20)/(x1-20) + s(x2-20)/(x2-20))        
def binary_encode(x1):
    global bit_size
    return bin(x1)[2:].zfill(int(bit_size))
def sp_crossover(x1,x2):
    for i in xrange(random.randrange(0,2*int(bit_size)),2*int(bit_size)):
        x1[i],x2[i]=x2[i],x1[i]


######### variable extractor#
def var_ext(x,bit_size):
    #global bit_size
    m=[]
    for i in xrange(len(x)/bit_size):
        exec('x%d=x[i*(bit_size):(i+1)*bit_size]'%(i+1))
        exec('m.append(x%d)'%(i+1))
    return np.array(m)





#sorting subroutine###########################################################
def build_max_heap(a):
    for i in xrange((len(a)/2)-1,-1,-1):
        max_heapify(a,i)
    return a
def left(i):
    return (2*i)+1
def right(i):
    return (2*i)+2
def max_heapify(a,i):
    l=left(i)
    r=right(i)
    if l<len(a) and compute(var_ext(a[l],bit_size),u_l,statement)>compute(var_ext(a[i],bit_size),u_l,statement):
        largest=l
    else:
        largest=i
    if r<len(a) and compute(var_ext(a[r],bit_size),u_l,statement)>compute(var_ext(a[largest],bit_size),u_l,statement):
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        max_heapify(a,largest)

def heapsort(a):
    b=[]
    build_max_heap(a)
    for i in xrange(0,len(a)-1):
        a[0],a[-1]=a[-1],a[0]
        b.append(a.pop(-1))
        max_heapify(a,0)
    b.append(a.pop(-1))
    return b
############################################################################
from mpi4py import MPI
comm=MPI.COMM_WORLD
global rank
rank=comm.rank
size=comm.size


global np
n_p=12
l=math.log
global statement
statement="result=math.sin(x1)+math.sin(x2)+math.sin(x3)+math.sin(x4)"
accuracy=0.1#input('Accuracy needed : ')
u_l=np.array([20,20,20,20])#input('Upper Limit ::')
u_l_i=u_l
u_l=((rank+1)*u_l_i/float(n_p))-(rank*(u_l_i/float(n_p)))

if rank in range(12):
    bit_size=3#int(round(l((max(u_l)/(12))/accuracy)/l(2)))
    if bit_size>0:
        pass
    elif bit_size==0:
        bit_size=1
iteration=100#2**bit_size
population_number=10# int(round(1.5*bit_size))
if population_number%2==0:
    population_number=population_number
else:
    population_number-=1

gl_max=[]
a=[]
mating_pool=[]

if rank in range(12):
    for i in xrange(population_number):
        r=''
        for i in xrange(len(u_l)):
            exec('r%d=binary_encode(createrandom(bit_size))'%(i+1))
            exec('r+=r%d'%(i+1))
        for i in xrange(2):
            a.append(r)
    #population generated
            
    #selection starts
    while len(mating_pool)<population_number:
        r1=random.randrange(0,len(a))
        r2=random.randrange(0,len(a))
        if a[r1]!=a[r2]:
            if compute(var_ext(a[r1],bit_size),u_l,statement)>=compute(var_ext(a[r2],bit_size),u_l,statement):
                mating_pool.append(a.pop(r1))
            else:
                mating_pool.append(a.pop(r2))


    # mating_pool generated
    #print [compute(mating_pool[i][:4],mating_pool[i][4:],50) for i in range(len(mating_pool))]
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
    for i in xrange(population_number):
        for j in xrange(len(u_l)*bit_size):
            if random.random()<.02:
                if mating_pool[i][j]=='0':
                    mating_pool[i][j]='1'
                else :
                    mating_pool[i][j]='0'
    for i in xrange(population_number):
        mating_pool[i]=''.join(mating_pool[i])
    # mutation done
    # propagation
    a=[]
    fitness=[]
    gl_cnt=''
    for i in xrange(len(u_l)):
        gl_cnt+=binary_encode(0)
    gl_cntl=[]
    it_cnt=0
    for i in xrange(iteration):
    #while 1:
        #a=copy(mating_pool)
        #selection starts
        '''while len(mating_pool)<population_number:
            r1=random.randrange(0,len(a)/2)
            r2=random.randrange(len(a)/2,len(a))
            if a[r1]!=a[r2]:
                if compute(a[r1][:bit_size],a[r1][bit_size:],upper_limit)>=compute(a[r2][:bit_size],a[r2][bit_size:],upper_limit):
                    mating_pool.append(a.pop(r1))
                else:
                    mating_pool.append(a.pop(r2))
            else:
                pass
        '''
        # mating_pool generated
        #print [compute(mating_pool[i][:4],mating_pool[i][4:],50) for i in range(len(mating_pool))]

        #sorting_subroutine##################################################################################

        mating_pool=[list(i) for i in heapsort(mating_pool)]
        p=''.join(mating_pool[0])
        if compute(var_ext(p,bit_size),u_l,statement)>compute(var_ext(gl_cnt,bit_size),u_l,statement):
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
        for i in xrange(population_number):
            for j in xrange(len(u_l)*bit_size):
                if random.random()<.04:
                    if mating_pool[i][j]=='0':
                        mating_pool[i][j]='1'
                    else :
                        mating_pool[i][j]='0'
        for i in xrange(population_number):
            mating_pool[i]=''.join(mating_pool[i])
        #mutation done
        fitness.append(sum([compute(var_ext(mating_pool[i],bit_size),u_l,statement) for i in xrange(len(mating_pool))])/population_number)
        gl_cntl.append(compute(var_ext(gl_cnt,bit_size),u_l,statement))
        ##########convergence###########
        if  compute(var_ext(gl_cnt,bit_size),u_l,statement)-fitness[-1]<=0.04:           #it_cnt>=iteration and 
            break
        it_cnt+=1
        
    gl_cnt=(gl_cnt,compute(var_ext(gl_cnt,bit_size),u_l,statement),rank,bit_size)
    print gl_cnt
    #comm.send(gl_cnt,dest=0)
    #var_ext(gl_cnt)
    #gl_cnt=[((float(upper_limit)/(2**bit_size))*int(gl_cnt[:bit_size],2))+(rank*(upper_limit_i/12)),((float(upper_limit)/(2**bit_size))*int(gl_cnt[bit_size:],2))+(rank*(upper_limit_i/12)),gl_cntl[-1]]
    #gl_cnt=[((float(upper_limit)/(2**bit_size))*int(gl_cnt[:bit_size],2))+(rank*(upper_limit_i/12)),((float(upper_limit)/(2**bit_size))*int(gl_cnt[bit_size:],2))+(rank*(upper_limit_i/12)),gl_cntl[-1]]
    #comm.send(gl_cnt,dest=0)





'''if rank==0:
    for i in xrange(1,12):
        gl_max.append(comm.recv(source=i))
    gl_max_l=gl_max[0]
    for i in xrange(len(gl_max)):
        if gl_max[i][1]>gl_max_l[1]:
            gl_max_l=gl_max[i]
           
        else:
            pass
           
    gl_cnt_l,rank_l=gl_max_l[0],gl_max_l[2]
    #print gl_cnt_l
    for i in xrange(len(gl_cnt_l)/gl_max_l[3]):
        exec('x%d=gl_cnt_l[i*(bit_size):(i+1)*bit_size]'%(i+1))
        exec('x%d=(float(u_l[i])/((2**gl_max_l[3])-1))*int(x%d,2)+(rank_l*(float(u_l_i[%d])/12))'%((i+1),(i+1),i))
        exec('print  x%d'%(i+1))
    print time.time()-start_time
    print rank_l

    
'''
