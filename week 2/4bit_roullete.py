import random
import math
def createrandom():
    return random.randrange(0,16)
def compute(x1,x2):
    x1=(90/((2**4)-1))*int(x1,2)
    x2=(90/((2**8)-1))*int(x2,2)
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
def binary_encode(x1):
    return bin(x1)[2:].zfill(4)


''' reproduction operator '''
a=[]
b=[]
c=[]
cp=[]
prob=[]
rand=[]
randl=[]
F=0
cp_counter=0
for i in range(8):
    a.append(binary_encode(createrandom()))
    b.append(binary_encode(createrandom()))
    c.append(compute(a[i],b[i]))
    F+=c[i]
for i in range(8):
    prob.append(c[i]/F)
    cp_counter+=prob[i]
    cp.append(cp_counter)
    rand.append(round(random.random(),3))
for i in range(8):
    for j in range(7,-1,-1):
        if rand[i]>cp[j]:
            randl.append(j+1)
            break
        elif rand[i]<cp[0]:
            randl.append(0)
            break
print a
print b
print c
print prob
print cp
print rand
print randl

print 'using stochastic approach'

'''stochastic approach'''

c=[]
cp=[]
expc=[]
prob=[]
rand=[]
randl=[]
F=0
cp_counter=0
for i in range(8):
    c.append(compute(a[i],b[i]))
    F+=c[i]
for i in range(8):
    pr=c[i]/F
    exp=8*pr
    expc.append(exp)
    for j in range(int(math.floor(exp))):
        randl.append(i)
    prob.append(exp-math.floor(exp))
    cp_counter+=prob[i]
    cp.append(cp_counter)
print randl
l=len(randl)
for i in range(8-l):
    for j in range(7,-1,-1):
        r=random.random()*cp_counter
        if r>cp[j]:
            randl.append(j+1)
            break
        elif r<cp[0]:
            randl.append(0)
            break

print randl


print a
print b
