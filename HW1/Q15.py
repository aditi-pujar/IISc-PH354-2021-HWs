#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:56:34 2021

@author: aditi
"""

#Q15 
print('Exercise 15: Plotting STM measurements of Si (111) surface:')
M=[]
with open('stm.txt') as f:
    i=0;
    for line in f:
        Mi=[]; M.append(Mi)
        j=0; index=0; prev_index=0;
        while line[index]!="\n":
            if line[index]==" ":
                Mij=float(line[prev_index:index])
                Mi.append(Mij)
                prev_index=index+1
                j+=1
                index+=1
            else:
                index+=1
        i+=1
# We have therefore read the datafile into a grid of floats, M
# Verifying all rows:
# lengths=[len(M[ii]) for ii in range(0,len(M))] 


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


x=range(0,len(Mi))
y=range(0,len(M))

plt.figure(1)
X,Y = np.meshgrid(x,y)
Z = np.array(M)
plt.contour(X,Y,Z,colors='black')
plt.title('STM measurements of Si (111) surface\nContour Plot')
plt.xlabel('x-axis'); plt.ylabel('y-axis');


plt.figure(2)
ax=plt.axes(projection='3d')
ax.plot_surface(Y,X,np.array(M), rstride=1, cstride=1, cmap='viridis',edgecolor='none')
plt.title('STM measurements of Si (111) surface\nSurface Plot')
plt.xlabel('x-axis'); plt.ylabel('y-axis');

plt.figure(3)
ax = plt.axes()
sns.heatmap(Z)
ax.set_title(str('STM measurements of Si (111) surface\nHeat Map'))

'''
Thus, the third heat map gave the best understanding of Si
structure with hexagonal motifs clearly visible
'''