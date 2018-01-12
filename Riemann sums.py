# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:38:06 2018

@author: cdonovan
"""

# Python 2.7

# this code calculates the lower and upper Riemann sums for a given function
# as well as a function, the "riemann" function also expects a domain in list form (showing the min and max of the domain)
# and also the step size with which the domain is partitioned

import numpy as np
from itertools import product

f1 = lambda x:x**2
import math
f2 = lambda x:math.sin(x)
f3 = lambda x:x

domain = [0,3]

def riemann(fn, dom, steps):    
    partition = filter(lambda x:x>=dom[0] and x<=dom[1],np.arange(dom[0], dom[1]+1, steps))
    if max(partition)!=dom[1]:
        partition.append(dom[1])
    zip1 = zip(range(len(partition)), partition)
    part2 = map(lambda y:(y[0][1], y[1][1]),filter(lambda x:x[0][0]+1==x[1][0],product(zip1, zip1)))
    map1 = map(lambda x:(abs(x[0]-x[1]), fn(x[0]), fn(x[1])),part2)
    map2 = map(lambda x:(x[0]*min(x[1], x[2]), x[0]*max(x[1], x[2])), map1)
    l_riemann = sum(map(lambda x:x[0],map2))
    u_riemann = sum(map(lambda x:x[1],map2))
    return l_riemann, u_riemann

for step in [2,1,0.5,0.1,0.05,0.01,0.001,0.0001, 0.00001, 0.000001]:
    print riemann(f3, domain, step)
