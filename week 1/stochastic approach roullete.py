import random
import math
def createrandom(x1,x2):
    return (x1+((x2-x1)*random.random()))
def compute(x1,x2):
    d=(math.pi)/180
    s=math.sin
    c=math.cos
    return 4*s(d*x1)+6*c(d*x1)+4*s(d*x2)+2*c(d*x2)
a=[]
b=[]
c=[]
expc=[]
cprob=[]
expccounter=0
ccounter=0
rand=[]
sumc=0
randl=[]
for i in range(8):
    a.append(round(createrandom(0,90),2))
    b.append(round(createrandom(0,90),2))
    c.append(compute(a[i],b[i]))
    sumc+=c[i]
for i in range(8):
    c[i]=c[i]/sumc
    ccounter+=c[i]
    expc.append(8*c[i])
    if expc[i]>=1:
        expccounter+=math.floor(expc[i])
        print math.floor(expc[i])
        expc[i]-=math.floor(expc[i])
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
for i in a:
    print i
for i in b:
    print i
for i in c:
    print i
for i in expc:
    print i
for i in cprob:
    print i
for i in rand:
    print i
for i in randl:
    print i
print expccounter
    
