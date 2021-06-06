#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:50:16 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def lorentz(t,X,sigma,r,b):
    x = X[0]; y = X[1]; z = X[2];
    dxdt = sigma*(y-x)
    dydt = r*x -y -x*z
    dzdt = x*y -b*z
    return np.array([dxdt,dydt,dzdt])

sigma, r, b = 10,28,8/3
X0 = np.array([0,1,0])
t = np.linspace(0,50,10000)

X = RK4.RK4(lorentz,X0,t,sigma,r,b)

plt.figure()
plt.plot(t,X[:,1])
plt.title('(Q3) Lorenz Attractor: y v/s t ')
plt.xlabel('t'); plt.ylabel('y')
plt.savefig('Q3(a).png')

plt.figure()
plt.plot(X[:,0],X[:,2])
plt.title('(Q3) Lorenz Attractor Phase Plot: z(t) v/s x(t)')
plt.xlabel('x'); plt.ylabel('z')
plt.savefig('Q3(b).png')

###################################################