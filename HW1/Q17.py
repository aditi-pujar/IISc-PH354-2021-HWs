#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:10:44 2021

@author: aditi
"""

#Q17
import numpy as np
from matplotlib import pyplot as plt
import cmath
import seaborn as sns

def Mandelbrot(x,y):
    c = complex(x,y)
    Z0 = complex(0,0)
    for i in range(1,101):
        Zn = Z0**2+c
        r,theta = cmath.polar(Zn)
        if r>2.0:
            return i
        elif i==100:
            return i
        Z0=Zn
        i+=1

###############################################################################
print('Exercise 17: the Mandelbrot set')

#trial: coarse grained grid
resolution = 1000
xval=np.linspace(-2,2,num=resolution)
yval=np.linspace(-2,2,num=resolution)

MS=[]; MSbw=[];

for x in xval:
    ms=[]; MS.append(ms); msbw=[]; MSbw.append(msbw)
    for y in yval:
        eta1 = Mandelbrot(y,x) #this is because heat map is plotting an array meaning the (row,column) indices exchanged with (x,y)
        if eta1 == 100:
            eta2 = True
        else:
            eta2=False
        ms.append(eta1)
        msbw.append(eta2)

MS_col=np.array(MS)
MS_bw=np.array(MSbw)
MS_log=np.log(MS_col)

##################################################################################

plt.figure(1)
ax = plt.axes()
sns.heatmap(MS_col)
ax.set_title(str('Mandelbrot Set (Graining: N='+str(resolution)+')\n(# of iterations to cross 2)'))

plt.figure(2)
ax = plt.axes()
sns.heatmap(MS_bw)
ax.set_title(str('Mandelbrot Set (Graining: N='+str(resolution)+')'))

plt.figure(3)
ax = plt.axes()
sns.heatmap(MS_log)
ax.set_title(str('Mandelbrot Set (Graining: N='+str(resolution)+')\n(log scale (# of iterations to cross 2))'))

#################################################################################