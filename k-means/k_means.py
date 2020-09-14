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

def calculate_distance(data, centroid):
    dis = np.zeros(centroid.shape[0])
    for i in range(centroid.shape[0]):
        temp = 0
        for j in range(centroid.shape[1]):
            temp += (data[j] - centroid[i][j])**2
        dis[i] = math.sqrt(temp)
   
    return dis

def kmeans(centroid, data, num_cluster):
    cluster = np.zeros(data.shape[0])
    for iter in range((10)):
        # assignment
        for i in range(data.shape[0]):
            distance = calculate_distance(data[i], centroid)
            cluster[i] = np.argmin(distance)
        # update
        for i in range(num_cluster):
            curr_cluster = data[np.where(cluster == i)]
            new_centroid = np.mean(curr_cluster, 0) 
            centroid[i] = new_centroid
        iter += 1
        print(cluster)

def initial(num_cluster, data):
    centroids = np.zeros((num_cluster,data.shape[1]))
    min_value = np.min(data)
    max_value = np.max(data)
    for i in range(num_cluster):
        for j in range(data.shape[1]):
            centroids[i][j] = random.uniform(min_value, max_value)
    return centroids

def main():
    mat = scipy.io.loadmat('D:\hw5_p1a.mat')
    data = mat['X'][:30]
    num_cluster = 3
    
  
    centroids = initial(num_cluster, data)
    kmeans(centroids, data, num_cluster)

if __name__ == '__main__':
    main()
