# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:39:56 2017

@author: cdonovan
"""

# python 3.5

import numpy as np

# input data here in the form of a 2D numpy array
# the array should be entirely numeric & have rows as observations & columns as features
# data = ?
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

def euclidean(pt1, pt2):
    """ Euclidean distance between 2 points, pt1 and pt2
    """
    diff = pt1-pt2
    square = diff**2
    sqrt = np.sum(square)**0.5
    return sqrt

def random_centroids(data, k):
    """ picking random initial centroids
    """
    # get the min and max values for each feature in data
    mins = np.min(data,axis=0)
    maxes = np.max(data,axis=0)
    zipper = list(zip(mins,maxes))
    k_centroids = np.array([list(map(lambda x:np.random.uniform(x[0],x[1]),zipper)) for num in range(k)])
    return k_centroids
    
def dists_to_centroids(data, centroids):
    """ generates an array of distances between the data and the k centroids
    A row for each data observation and a column for each centroid
    """
    list2 = []
    for num in range(len(centroids)):
       list1 = list(map(lambda x:euclidean(x,centroids[num]),data))
       list2.append(list1)
    dists = np.array(list2).T
    return dists

aaa = random_centroids(data,3)        
dists_to_centroids(data,aaa)

# to add: rest of algorithm
# plotting


        
    