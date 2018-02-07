import time
from math import sin
import numpy as np
import numexpr as ne

a=np.arange(1000000000)
t=time.time()
np.sin(a)
print time.time()-t

t=time.time()
ne.evaluate('sin(a)')
print time.time()-t
