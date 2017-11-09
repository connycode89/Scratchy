# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 01:39:54 2017

@author: Conor
"""

# Python 2.7

list1 = [4,5,6,2,1,3,7]
n = 5 # so should return the 5th smallest element - also 5

import random
r1 = random.choice(list1)
small = filter(lambda x:x<r1, list1)
large = filter(lambda x:x>r1, list1)
p = random.choice(0,1)
if p==0:
    small+=filter(lambda x:x==r1, list1)
else:
    large+=filter(lambda x:x==r1, list1)