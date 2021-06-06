#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:31:49 2021

@author: aditi
"""
from gaussxw import gaussxwab
from scipy import constants
import math
from numpy import linspace
#Q9
print('Exercise 9: Heat Capacity of a Solid')
#(a)
def integrand(x):
    if x==0:
        xval = 0
    else:
        xval = (x**4)*(math.exp(x))/(math.exp(x)-1)**2
    return xval

def cv(T):
    b = 428/T
    a = 0
    x,w = gaussxwab(50,a,b)
    I=0
    for i in range(50):
        I+= w[i]*integrand(x[i])

    k = 9*(10**(-3))*(6.022*10**28)\
        *constants.Boltzmann*(T**3)/(428**3)
    return k*I

#(b)
Tval = linspace(5,500,1000)
CVval=[]
for t in Tval:
    CVval.append(cv(t))

from matplotlib import pyplot as plt
plt.figure()
plt.plot(Tval,CVval)
plt.title('(Q9b) Heat Capacity Cv v/s Temperature T')
plt.xlabel('T (K)')
plt.ylabel('Cv (Joule per K)')