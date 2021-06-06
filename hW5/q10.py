#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:21:32 2021

@author: aditi
"""
#q10
import numpy as np
import matplotlib.pyplot as plt

N = int(1e4)
phi = 2*np.pi*np.random.random(N)*(180/np.pi)
z = np.random.random(N)
# if z <=1/2:
#     theta = [np.math.acos(1-2*val)*(180/np.pi) for val in z]
# else:
#     theta = [np.pi-np.math.acos(2*val-1)*(180/np.pi) for val in z]

theta = [np.math.acos(1-2*val)*(180/np.pi) for val in z]

xval = np.sin(theta)*np.cos(phi)
yval = np.sin(theta)*np.sin(phi)
zval = np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xval,yval,zval,s=0.1)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('(Q10) Random points on globe')
plt.show()
#plt.savefig('Q10.png')