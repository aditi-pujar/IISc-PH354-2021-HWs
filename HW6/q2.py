#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:23:08 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def F(t,X,a,b,c,d):
    x = X[0]; y = X[1]
    dxdt = a*x-b*x*y
    dydt = c*x*y - d*y
    return np.array([dxdt, dydt])

alpha, beta, gamma, delta = 1, 0.5, 0.5, 2
X0 = np.array([2,2])
t = np.linspace(0,30,1000)

X = RK4.RK4(F,X0,t,alpha,beta,gamma,delta)

plt.figure()
plt.plot(t,X[:,0],t,X[:,1])
plt.title('Q2 Lotka Volterra System')
plt.xlabel('t'); plt.ylabel('Populations (in 1000s)')
plt.legend(['Rabbits','Foxes'])
plt.savefig('Q2.png')

'''
The solutions are oscillatory and out of phase;
as rabbit populations grow, so do the foxes
=> causes rabbits to die out
=> soon, not enough food for foxes so they too start dying out
=> less foxes so rabbits aren't being hunted as much
=> rabbit population grows again
and thus the cycle continnues

Foxes also die out faster.
'''