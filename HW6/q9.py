#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:08:27 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt

def leapfrog(f,X0,t,*args):
    X = np.zeros((len(t),np.size(X0)))
    X[0,:] = X0

    h = t[1]-t[0]
    hval = X0 + (h/2)*f(t[0],X0,*args)

    for i in range(len(t)-1):
        X[i+1,:] = X[i,:] + h*(f(t[i]+h/2,hval))
        hval = hval + h*f(t[i]+h,X[i+1,:])
    return X

def eqn(t,X):
    x = X[0]; v = X[1];

    dxdt = v
    dvdt = v*v -x -5
    return np.array([dxdt,dvdt])

h = 0.001
t = np.arange(1,50+h,h)
X0 = np.array([1,0])

X = leapfrog(eqn,X0,t)

plt.figure()
plt.plot(t,X[:,0])
plt.title('(Q9) x(t) v/s t')
plt.xlabel('t'); plt.ylabel('x(t)');
plt.savefig('Q9.png')