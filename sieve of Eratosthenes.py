# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 00:58:34 2017

@author: Conor
"""

# python 2.7

def comp(mult, tup):
    if tup[0] in mult:
        return (tup[0], False)
    else:
        return tup

def sieve(n):
    int_list = range(2,n+1)
    bool_init = [True for item in int_list]
    zip1 = zip(int_list,bool_init)
    num1 = zip1[0][0]
    while True:
        print num1
        mult_list = filter(lambda y:y in int_list,[num2*num1 for num2 in int_list])
        zip1 = map(lambda x:comp(mult_list,x),zip1)
        filt1 = filter(lambda x:x[0]>num1 and x[1],zip1)
        if len(filt1)==0:
            break
        else:
            num1 = filt1[0][0]
    prime_list = map(lambda y:y[0],filter(lambda x:x[1],zip1))
    return prime_list
        
s100 = sieve(100)
s10000 = sieve(10000)
