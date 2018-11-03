#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:14:44 2018

@author: yang
"""

import numpy as np
import scipy.io
import random as random
import matplotlib.pyplot as plt
import math

def calcuate_distance(x, center):
    dis = []  
#    print x.shape, center
    for i in range(len(center)):
        temp = 0
        for j in range(x.shape[0]):
            temp += (x[j] - center[i][j])**2
        dis.append(math.sqrt(temp))
    return dis
  
def kmeans(data, mean, cluster):
    iteration = 0
#while True:
    while iteration <= 5:
        for i in range(N):
            distance = calcuate_distance(data[i], mean)
            loc = np.argmin(distance)
            cluster[i] = loc
            
        for i in range(num_cluster):
            each_cluster = data[np.where(cluster == i)]
            new_centroid = np.mean(each_cluster, 0)
            mean[i] = new_centroid
        iteration += 1
            
    plt.scatter(data[:,0], data[:,1], c = cluster)
    plt.show
    
def initialcentra(num_cluster, num_feature, N):
    mean = np.zeros((num_cluster, num_feature))
    
    min_value = np.min(data)
    max_value = np.max(data)
    cluster = np.zeros((N))  
    for i in range(num_cluster):
        for j in range(num_feature):
            mean[i][j] = random.uniform(min_value, max_value)
    return cluster, mean
    
if __name__ == "__main__":
    mat = scipy.io.loadmat('hw5_p1a.mat')
    data = mat['X']
    num_cluster = 3
    num_feature = data.shape[1]
    N = data.shape[0]
    
    cluster, mean = initialcentra(num_cluster, num_feature, N)   
    kmeans(data, mean, cluster)

