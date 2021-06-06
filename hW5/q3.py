#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:15:00 2021

@author: aditi
"""

import numpy as np
import random as rd

#########################################################
def shift_fn(x,y):
    direction = rd.randint(1,4)
    if direction == 1:
        xnew, ynew = x+1,y
    elif direction ==2:
        xnew, ynew = x, y+1
    elif direction == 3:
        xnew, ynew = x-1, y
    else:
        xnew, ynew = x, y-1
    return xnew, ynew
##########################################################
def move(lattice,t,x,y):
    xnew, ynew = shift_fn(x,y)
    while not( (xnew<100 and xnew>0)and(ynew<100 and ynew>0)):
        xnew, ynew = shift_fn(x,y)
    lattice[xnew][ynew] = t+1
    return lattice, xnew, ynew
#####################################################
N=int(1e3)
L = 101
lattice = np.zeros((L,L))
xt = np.zeros(N+1)
yt = np.zeros(N+1)
T = np.arange(N+1)

i = 50;
j = 50;
xt[0] = i; 
yt[0] = j;

lattice[i][j] = 0
for t in range(N):
    lattice, i, j = move(lattice,t,i,j)
    xt[t+1] = i; yt[t+1] = j;
######################################################

from matplotlib import pyplot as plt

'''
import seaborn as sns

plt.figure()
plt.title('Brownian Motion: Colorbar shows Time Evolution')
xlabel = False; ylabel = False;
hm = sns.heatmap(data=lattice,xticklabels=xlabel,yticklabels=ylabel)
plt.plot(range(101))
plt.show()
plt.savefig('Q3a')
'''

plt.figure()
plt.title('Brownian Motion: Colorbar shows Time Evolution')
plt.scatter(xt,yt,1,c = T)
plt.colorbar()
plt.xlim([0,101]); plt.ylim([0,101])
plt.savefig('Q3(i)T=1e6.png')

'''
As we can see, the walker covers almost the entire 
lattice in 1e6 steps. But the nature of path taken
over time is better seen for smaller time period (1e3)
'''