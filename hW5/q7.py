#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:35:33 2021

@author: aditi
"""

#q7
import numpy as np
import random as rd

def E(lattice,J):
    L = np.size(lattice,1)
    E = 0
    for x in range(L):
        for y in range(L):
            neighX = [x+1,x,x,x-1]; neighY = [y,y+1,y-1,y];
            for k in range(4):
                xn = neighX[k]; yn = neighY[k];
                if (xn>L-1)or(xn<0)or(yn>L-1)or(yn<0):
                    continue
                else:
                    E += lattice[x][y]*lattice[xn][yn]
    return -J*E/2

L=20
T = int(1e5)
beta = 1; J = 1
lattice = np.array([rd.choices([-1,1],k=(L)) for i in range(L)])
E_init = E(lattice,1)

M = np.zeros(T+1)
M[0] = np.sum(lattice)

for t in range(T):
    tmp = E_init
    xval = rd.randint(0,L-1); yval = rd.randint(0,L-1)
    lattice[xval][yval] *= -1
    E_init = E(lattice,J)
 #   if (E_init>tmp):
    if rd.random()> np.exp(-beta*(E_init-tmp)):
         lattice[xval][yval] *= -1
         E_init = tmp
    M[t+1] = np.sum(lattice)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(t+1),M[:t+1])
plt.title('(Q7) Magnetisation v/s no of MC iterations (T = 1): Trial 2')
plt.xlabel('n'); plt.ylabel('M')
#plt.savefig('Q7b(i)')


'''
(ii)
The magnetisation developed is either +-400

For the given Hamiltonian, 
the Ising model (for T<Tc) can develop either positive or
negative magnetisation as a matter of equal, random chance.

(iii)
We can see that as T increases, the net magnetisation decreases.
We expect that for a critical temperature Tc,
net magnetisation becomes 0
=> material undergoes phase transition 
from ferromagnetic to paramagnetic
'''