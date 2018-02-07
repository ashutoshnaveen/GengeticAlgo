import numpy as np
import sys
import time

s=10000000

start=time.time()
b=range(s)
for i in b:
    i+=1
print time.time()-start



start=time.time()
a=np.arange(s)
a+=1
print time.time()-start
