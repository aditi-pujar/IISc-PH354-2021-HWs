#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:44:23 2021

@author: aditi
"""
import numpy as np
import q11_functions
from matplotlib import pyplot as plt
import seaborn as sns

L = 101
r = 0
lattice = np.zeros((L,L))
n = 1
lattice[int(L/2)][int(L/2)] = 1
t=0

while (r<=int(L/2)):
    lattice, n, r, t = q11_functions.brownian3(lattice,n,r,t)

print('(q11(c) Number or particles for grid centre to become anchored:',n)
plt.figure()
plt.title('q11(c) r = 50 Lattice Size = 101')
xlabel = False; ylabel = False;
hm = sns.heatmap(data=lattice,xticklabels=xlabel,yticklabels=ylabel)
plt.show()
#plt.savefig('Q11c(iii)')

'''
Takes very long to run and so had to truncate
at r = 26 twice
'''