#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:14:44 2018

@author: yang
"""

import pickle
import numpy as np

with open('test.pickle', 'rb') as f:
    inp = pickle.load(f)
x = np.array([i[0] for i in inp])

cluster = np.zeros(x.shape[0])
minv = np.min(x, axis = 0)
maxv = np.max(x, axis = 0)

k = 3
center = np.zeros((k, x.shape[1]))
for i in range(k):
    for j in x.shape[1]:
        center[i,j] = np.random.randint(minv, maxv)
        
center_old = np.zeros(center.shape)

while err != 0:
    for i in range(len(x)):
        distances = eucl_dist(x[i], center)
        clust = np.argmin(distances)
        cluster[i] = clust
        
    center_old = np.copy(center)
    
    for i in range(k):
        points = [x[j] for j in range(len(x)) if cluster[j] == i]
        if points:
            center[i] = np.mean(points, axis = 0)
            
    err = eucl_dist(center, center_old, None)