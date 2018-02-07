import copy
import math
import random
global bs,pop_size,nv,a,var
a=[(3,5),(2,3)]         #constraints
bs=5                         #bit_size controlling precision
pop_size=4              #population size
nv=2                        #number of variables
csp=0.5                 #crossover probability
def f(x1,x2):
    return (x1+x2-7)**2+(x1+x2-11)**2
def F(a):
    return float(1)/(1+a)
def A(a):
    return float(a)/F(a)

def dext(x1):
    global nv
    bs=len(x1)/nv
    global var
    var=[]
    for i  in range(nv):
        var.append(x1[int(i*bs):int((i+1)*bs)])
    #print(var)
    #return var

def venc(a):
    encv=[]
    global bs,var
    for i in range(len(a)):
        min1=a[i][0]
        max1=a[i][1]
        encv.append(min1+((max1-min1)/((2**bs)-1)*int(var[i],2)))
    return (encv)


def popgen():
    init_pool=[]
    global pop_size
    for i in range(pop_size):
        init_pool.append(str(bin(random.randint(0,2**(nv*bs)))[2:].zfill(nv*bs)))
    #print(init_pool)
    return init_pool



def main():
    for i in popgen():
        dext(i)
        venc(a)

def problem_statement():
    E=[]
    q=[]
    cp=[]
    mp=[]                                                                                                   #actual number of the roulette wheel area it belongs
    vnc=[]
    fx=[]
    Fx=[]
    seed=[]
    init_pool=['1110011001','1110011001','1001000111','0110011001']             ## remember it is for testing after crossover
    ############ previous init pool:::    init_pool=['1110011001','0001000111','1010101110','1001010000']   ######
    ####### after selection:::   mod_init_pool=['1110011001','1110011001','1110011001','0001000111']    #################
    #########after crossover mod_init_pool=['1110011001','1110011001','1001000111','0110011001']  ############
    for i in init_pool:
        dext(i)
        vnc.append(venc(a))
        fx.append((f(vnc[-1][0],vnc[-1][1])))
        Fx.append(F(fx[-1]))
        E.append(Fx[-1])
    q=[float(x)/sum(E) for x in E]                                                          #f(x)/total_sum(f(x)) giving the probability    
    cp=[sum(q[:i+1]) for i in range(len(q))]                                        #cumulative probability of the strings
    for i in range(pop_size):
        seed.append(random.random())
        for j in range(1,len(cp)):
            if seed[-1]<cp[i] and seed [-1]>cp[i-1]:
                mp.append(i)
                break
            else:
                mp.append(0)
                break
    #print(mp)
    ##seeing the results
    for i in range(4):
        print(vnc[i],'-',fx[i],'-',Fx[i],'-',q[i],'-',cp[i],'-',seed[i],'-',mp[i])
    #print(vnc,fx,Fx,q,cp,seed,mp)
    ################################################issue seen ###############################
    # a point with higher fitness dominates even average fitness value solutions##############################
    
    # crossover first generation




    
def spc(x1,x2):
    print("before crossover :: ",x1,'  ',x2)
    global csp
    a=0.7#random.random()
    if a>=csp:
        b=random.randint(0,len(x1))
        print("corssover site:: ",b)
        x3=copy.deepcopy(x1)
        x1=''.join(list(x1)[:b]+list(x2)[b:])
        x2=''.join(list(x2)[:b]+list(x3)[b:])
        print("after crossover :: ",x1,'  ',x2)
    

if __name__=='__main__':
    #main()
    problem_statement()
    #spc('1110011001','0001000111')
    
