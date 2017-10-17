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
data = np.array([[1,1,1],[1,1,2],[8,8,9],[7,8,9]])

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

def iterate_once(data, prev_clusts, cents):
    list_cents = []
    for num in range(len(cents)):
        clust_num = data[prev_clusts==num]
        if len(clust_num)!=0:
            cent2 = np.mean(clust_num,axis=0)
            list_cents.append(list(cent2))
        else:
            list_cents.append(list(random_centroids(data,1)[0]))
    new_cents = np.array(list_cents)
    return new_cents

def algorithm(data,k):
    centroids = random_centroids(data,k)        
    dists = dists_to_centroids(data,centroids)
    clusts = np.argmin(dists, axis=1)
    while True:    
        centroids = iterate_once(data, clusts, centroids)
        dists = dists_to_centroids(data,centroids)
        clusts2 = np.argmin(dists, axis=1)
        if np.all(clusts==clusts2):
            break
    wss = np.sum(np.min(dists_to_centroids(data,centroids), axis=1))
    return clusts2, wss

k = 2
algorithm(data,k)

# to add: rest of algorithm
# plotting
