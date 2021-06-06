#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:53:49 2021

@author: aditi
"""

import numpy as np
import q11_functions
from matplotlib import pyplot as plt
import seaborn as sns

'''
L = 101
lattice = np.zeros((L,L))
#(a): for finite no of particles:
n = 1000
for k in range(n):
    lattice = q11_functions.brownian1(lattice,k)

plt.figure()
plt.title('q11(a) Trial: for n = 1e3 particles')
xlabel = False; ylabel = False;
hm = sns.heatmap(data=lattice,xticklabels=xlabel,yticklabels=ylabel)
plt.show()
plt.savefig('Q11a')
'''

#(b): Running till point at centre is anchored:
L = 101
lattice = np.zeros((L,L))
bit = 0; k=0;
while (bit==0):
    lattice,bit = q11_functions.brownian2(lattice,k)
    k = k+1

print('(q11(b)(1) Number or particles for grid centre to become anchored:',k)
plt.figure()
plt.title('q11(b) Lattice Size = 101')
xlabel = False; ylabel = False;
hm = sns.heatmap(data=lattice,xticklabels=xlabel,yticklabels=ylabel)
plt.show()
#plt.savefig('Q11b(1).png')

# L = 201
L = 201
lattice = np.zeros((L,L))
bit = 0; k=0;
while (bit==0):
    lattice,bit = q11_functions.brownian2(lattice,k)
    k = k+1

print('(q11(b)(2) Number or particles for grid centre to become anchored:',k)
plt.figure()
plt.title('q11(b) Lattice Size = 201')
xlabel = False; ylabel = False;
hm = sns.heatmap(data=lattice,xticklabels=xlabel,yticklabels=ylabel)
plt.show()
#plt.savefig('Q11b(2).png')


