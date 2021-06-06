#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:28:09 2021

@author: aditi
"""
import numpy as np
import random as rd
import matplotlib.pyplot as plt

def cooling(t):
    T0 = 1
    tau = 10
    return T0*np.exp(-t/tau)

f1 = lambda x: x*x - np.cos(4*np.pi*x)
f2 = lambda x: np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)


kb = 1
T = 1

def finding_minima(f,x0,T):
    N = int(2e5)
    x = np.zeros(N+1)
    x[0] = x0
    E = f(x[0])
    for t in range(N):
        dx = rd.normalvariate(0,1)
        tmp1 = x[t]; tmp2 = E
        x[t+1] = tmp1 + dx
        E = f(x[t+1])
        if (E > tmp2):
            try:
                prob = np.exp(-(E-tmp2)/(kb*T))
            except RuntimeWarning:
                prob = 0
            if (rd.random() > prob):
                x[t+1] = tmp1
                E = tmp2
        T = cooling(t)
    #print('Minima is found to be at:',x[N])
    plt.figure()
    plt.plot(x,'.',1)
    plt.title('Walker Position over number of iterations: (f2)')
    plt.xlabel('n'); plt.ylabel('Minima')
    return x[N]

x1 = finding_minima(f1,2,1)
x2 = finding_minima(f2,2,1)

print('For function 1:\n Minima is found at', x1)
print('For function 1:\n Minima is found at', x2)



'''
x = np.zeros(N+1)
x[0] = 2
E = f1(x[0])

for t in range(N):
    dx = rd.normalvariate(0,1)
    tmp1 = x[t]; tmp2 = E
    x[t+1] = tmp1 + dx
    E = f1(x[t+1])
    if (E > tmp2):
        try:
            prob = np.exp(-(E-tmp2)/(kb*T))
        except RuntimeWarning:
            prob = 0
        if (rd.random() > prob):
            x[t+1] = tmp1
            E = tmp2
    T = cooling(t)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(x,'.',1)
'''