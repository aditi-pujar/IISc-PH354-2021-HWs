#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:03:41 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def coupled_springs(t,X,N,k,m):
    # len(F) == N necessarily
    F = np.zeros(N)
    w = 2
    F[0] = np.cos(w*t[0])

    x_array = np.empty(N); v_array = np.empty(N)

    x_array[0] = X[N]
    v_array[0] = (k*(X[1]-X[0]) + F[0])/m

    x_array[1:N-2] = X[N+1:2*N-2]
    v_array[1:N-2] = (k*(X[2:N-1]+X[1:N-2]-2*X[1:N-2]) - F[1:N-2])/m

    x_array[N-1] = X[2*N-1]
    v_array[N-1] = (k*(X[N-2]-X[N-1]) + F[N-1])/m

    return np.append(x_array,v_array)

k,m = 6,1
N = 5
X0 = np.zeros(2*N)

t = np.linspace(0,20,1000)

X = RK4.RK4(coupled_springs,X0,t,N,k,m)

plt.figure()
legendstr = [];
for i in range(N):
    plt.plot(t,X[:,i])
    string = 'Spring %d'%(i+1)
    legendstr.append(string)
plt.title('(Q7) x(t) v/s t for all springs')
plt.xlabel('t'); plt.ylabel('x(t)');
plt.legend(legendstr)
plt.savefig('Q7.png')