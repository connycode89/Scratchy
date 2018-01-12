# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:56:06 2018

@author: cdonovan
"""

# convolution

from scipy.misc import imread
from scipy.misc import imresize
from scipy.signal import convolve2d
from PIL import Image
import numpy as np

arr = imread('C:\\MyWorkingFolder\\Donovan, Conor.jpg')

data = arr[:,:,0]
data2 = imresize(data, (600,600))

img = Image.fromarray(data2)
img.show()

filter1 = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
filter2 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

data3 = convolve2d(data2, filter1, 'valid')
img2 = Image.fromarray(data3)
img2.show()

data4 = convolve2d(data2, filter2, 'valid')
img3 = Image.fromarray(data4)
img3.show()