#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:05:00 2021

@author: aditi
"""
#Q3c
from math import exp
from numpy import arange

print('Q3')
print('(c) Fixed point iteration with Steffensen method for accelerated convergence:')
print('c\t\tx*\t\t no of iterations \n')
def f(x,c):
    return x - (1-exp(-c*x))

def Steffenson(x,c,f):
    n=0
    while abs(f(x,c))>10**-7:
        g = f(x+f(x,c),c)/(f(x,c))-1
        xn = x - f(x,c)/g
        x = xn
        n+=1
    return x,n

cval = arange(0,3.01,0.01)
for c in cval:
    xval,n=Steffenson(1,c,f)
    print(' %.2f\t\t%f\t\t%d' % (c,xval,n))

