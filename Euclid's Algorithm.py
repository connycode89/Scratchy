# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 00:09:14 2017

@author: Conor
"""

def euclid(num1, num2):
    while True:
        sorted1 = sorted([num1, num2])
        rem1 = num2%num1
        if rem1==0:
            break
        else:
            num2 = num1
            num1 = rem1
    return num1
    
euclid(60,106)