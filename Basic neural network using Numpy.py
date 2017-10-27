# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:52:46 2017

@author: cdonovan
"""

# Python 3.5
# Basic neural network using Numpy

import numpy as np

# activation functions

def relu(arr):
    return np.maximum(arr,0)

relu(arr1)