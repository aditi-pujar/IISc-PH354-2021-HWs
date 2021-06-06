#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:14:03 2021

@author: aditi
"""

#Q 16
print('Exercise 16: Deterministic chaos and the Feigenbaum plot')
import numpy as np
from matplotlib import pyplot as plt
############################################################
def recurrence_plot(r):
    x0=1/2
    xeq=[]
    for i in range(0,1000):
        xval=x_eqbm(x0,r)
        xeq.append(xval)
    return xeq

def x_eqbm(x0,r):
    for t in range(1,1000):
        xnew=r*x0*(1-x0)
        x0=xnew
    return x0

rval = np.linspace(1,4,num=300)
X=[]; R=[];

for r in rval:
    xlist = recurrence_plot(r)
    rlist = (r*np.ones(1000)).tolist()
    X=X+xlist
    R=R+rlist

Xplot=np.array(X)
Rplot=np.array(R)
plt.figure()
plt.scatter(Rplot,Xplot,s=5)
plt.title('The Feigenbaum plot\nfor Logistic Map')
plt.xlabel('r'); plt.ylabel('x')

###############################################################
'''
(a) On the Feigenbaum plot,
A stable fixed point would look like a single point for a given value of r 
As for all initial conditions, trajectories go to same fixed point

An unstable fixed point would also look like a single point:
if the range initial conditions included it.

Chaos would look like: multiple points scattered haphazardly along the 
x = r* line. This would be different from a limit cycle because, for a
limit cycle, perhaps the different x points are scattered uniformly
=> as they are in a periodic motion, they could be at any x value in the orbit
at the time their positions (x) are noted.

But for chaos, this distribution would be haphazard and non-uniform.

(b) Edge of chaos seems to be around at r = 3.6
'''