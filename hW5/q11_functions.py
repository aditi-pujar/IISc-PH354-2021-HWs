#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:24:09 2021

@author: aditi
"""


import numpy as np
import random as rd
#########################################################
'''
def brownian1(lattice,i):
    L = np.size(lattice,1)
    x = int(L/2); y = int(L/2);
    boundary = False
    anchor = is_anchor(x,y,lattice)
# if (anchor): break loop of adding more particles
    while (not(boundary) and not(anchor)):
        x, y = shift_fn(x,y)
        boundary = is_boundary(x,y,L)
        if not(boundary):
            anchor = is_anchor(x,y,lattice)
        else:
            break
    lattice[x][y] = i+1
    return lattice
'''

def is_anchor(x,y,lattice):
    L = np.size(lattice,1)
    neighX = [x+1,x,x,x-1]; neighY = [y,y+1,y-1,y];
    val = 0
    for k in range(4):
        xn = neighX[k]; yn = neighY[k];
        if (xn>L-1)or(xn<0)or(yn>L-1)or(yn<0):
            continue
        else:
            tmp = bool(lattice[neighX[k]][neighY[k]])
            val = val + tmp
    return bool(val)

def is_boundary(x,y,L):
    return bool((x==L-1)or(x==0)or(y==L-1)or(y==0))

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

def shift_fn2(x,y,L):
    xnew, ynew = shift_fn(x,y)
    val = (0<=xnew)and(xnew<=L-1)and(0<=ynew)and(ynew<=L-1)
    while not(val):
        xnew, ynew = shift_fn(x,y)
    return xnew, ynew

'''
brownian that returns the trajectory

def brownian(i,j):
    #while check if adjacent to any anchored points
    #keep moving. return new and final lattice.
'''

def brownian1(lattice,i):
    L = np.size(lattice,1)
    x = int(L/2); y = int(L/2);
    boundary = False
    anchor = is_anchor(x,y,lattice)
# if (anchor): break loop of adding more particles
    while (not(boundary) and not(anchor)):
        x, y = shift_fn(x,y)
        boundary = is_boundary(x,y,L)
        if not(boundary):
            anchor = is_anchor(x,y,lattice)
        else:
            break
    lattice[x][y] = i+1
    return lattice

###########################################################

def brownian2(lattice,i):
    L = np.size(lattice,1)
    x = int(L/2); y = int(L/2);
    boundary = False
    anchor = is_anchor(x,y,lattice)
    if (anchor): 
        return lattice,1
    else:
        while (not(boundary) and not(anchor)):
            x, y = shift_fn(x,y)
            boundary = is_boundary(x,y,L)
            if not(boundary):
                anchor = is_anchor(x,y,lattice)
            else:
                break
        lattice[x][y] = i+1
        return lattice,0

#######################################################

def brownian3(lattice,n,r,t):
    L = np.size(lattice,1)
    x_ic, y_ic, n_ic = circumferance(r+1,L) #set of neighbours at a distance r
    kval = rd.randrange(n_ic)
    x = x_ic[kval]; y = y_ic[kval];
    rad_boundary = False
    anchor = is_anchor(x,y,lattice)

    while not(anchor):
        x, y = shift_fn2(x,y,L)
        rad_boundary = is_radboundary(x,y,r,L)
        if (rad_boundary):
           # bit = 0;
            break
        else:
            anchor = is_anchor(x,y,lattice)
    if (rad_boundary):
        return lattice,n,r,t+1
    else:
        lattice[x][y] = n+1
        n = n+1
        rnew = int(((x-int(L/2))**2+(y-int(L/2))**2)**0.5) 
        if (rnew > r):
            r = rnew
        return lattice,n,r,t+1
#########################################################
def is_radboundary(x,y,r,L):
    return bool( (x-int(L/2))**2+(y-int(L/2))**2 >= 4*r*r) 
#######################################################
import math
def circumferance(r,L):
    x0 = int(L/2); y0 = int(L/2);
    x_ic=[]; y_ic=[];
    
    for x in range(x0-r,x0+r+1):
        for y in range(y0-r,y0+r+1):
            if math.floor( math.sqrt((x-x0)**2+(y-y0)**2) ) == r:
                x_ic.append(x); y_ic.append(y);
    n_ic = len(x_ic)
    return x_ic,y_ic,n_ic

#####################################################
'''
L=101
lattice = np.zeros((L,L))

x,y,n = circumferance(49,L)
for i in range(n):
    lattice[x[i]][y[i]] = 1

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure()
hm = sns.heatmap(lattice)
plt.title('Q11c(i) Points sampled for a given r = 49')
plt.show()
plt.savefig('Q11c(i).png')
'''