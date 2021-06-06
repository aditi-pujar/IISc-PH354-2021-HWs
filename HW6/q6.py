#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:57:40 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def orbit(t,X,G,M,L):
    x = X[0]; y = X[1];
    vx = X[2]; vy = X[3];

    r = np.sqrt(x*x+y*y)
    k = G*M/(r*r*np.sqrt(r*r+L*L/4))

    dxdt = vx
    dydt = vy

    dvxdt = -k*x
    dvydt = -k*y

    return np.array([dxdt,dydt,dvxdt,dvydt])

G,M,L = 1,10,2
X0 = np.array([1,0,0,1])

t = np.linspace(0,10,1000)

X = RK4.RK4(orbit,X0,t,G,M,L)

plt.figure()
plt.plot(X[:,0],X[:,1])
plt.title('(Q6) Trajectory: y(t) v/s x(t)')
plt.xlabel('x(t)'); plt.ylabel('y(t)')
plt.savefig('Q6.png')