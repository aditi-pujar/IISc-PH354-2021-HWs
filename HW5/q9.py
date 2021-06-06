#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:18:49 2021

@author: aditi
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt
#from matplotlib import animation

def cooling(t):
    T0 = 1
    tau = int(1e2)
    return T0*np.exp(-t/tau)

###########################################################

def pick_pair(lattice):
    L = np.size(lattice,1)
    x, y = rd.randint(0,L-1), rd.randint(0,L-1)
    neighX = [x+1,x,x,x-1]
    neighY = [y,y+1,y-1,y]
    k = rd.randint(0,3)
    val = (0<=neighX[k]<=L-1) and (0<=neighY[k]<=L-1)
    while not(val):
        k = rd.randint(0,3)
        val = (0<=neighX[k]<=L-1) and (0<=neighY[k]<=L-1)
    x2, y2 = neighX[k], neighY[k]
    return x, y, x2, y2

#############################################################

def time_step(dimers,lattice,E,T,t):
    kb = 1;
    x1, y1, x2, y2 = pick_pair(lattice)
    old_lattice = lattice
    old_E = E
    old_dimers = dimers
    # changing the lattice
    if lattice[x1][y1] == lattice[x2][y2]:
        if lattice[x1][y1] == 0.0: #empty
            dimers.append((x1,x2,y1,y2))
            lattice[x1][y1] = lattice[x2][y2] = t+1
        else: #exists a dimer
            try:
                dimers.remove((x1,x2,y1,y2))
                lattice[x1][y1] = lattice[x2][y2] = 0
            except ValueError:
                pass
    E = -np.count_nonzero(lattice)
    #toss
    if E>old_E:
        try:
            prob = np.exp(-(E-old_E)/(kb*T))
        except RuntimeWarning:
            prob = 0
        if rd.random() > prob:
            lattice = old_lattice; E = old_E; dimers = old_dimers;
    T = cooling(t)
    return dimers,lattice,E,T
#######################################################

L = 50
N = int(1e6)
lattice = np.zeros((L,L))
E = -np.count_nonzero(lattice)
dimers = []
T = 1

LATTICE = [];
LATTICE.append(lattice)
DIMERS = [];
DIMERS.append(dimers)

for t in range(N):
    dimers,lattice,E,T = time_step(dimers,lattice,E,T,t)
    #if bit == 1:
    #    break
    LATTICE.append(lattice)
    DIMERS.append(dimers)

'''
Could not create video correctly. 
Following code could be used to visualise lattice
at any given time point = t0
''' 
t0 = N
lattice = LATTICE[t0]
dimers = DIMERS[t0]

plt.xlim([-2,51])
plt.ylim([-2, 51])
#hm = sns.heatmap(np.zeros((L,L)),linewidths=4)
for i in range(len(dimers)):
    plt.plot(dimers[i][0:2],dimers[i][2:4],linewidth = 2)
    plt.scatter(dimers[i][0:2],dimers[i][2:4],12)
plt.title('Time=1e6 Decay Time Scale=1e2')

'''
As cooling schedules get faster (i.e tau decreases):
    A slight decrease in packing efficiency seen
'''