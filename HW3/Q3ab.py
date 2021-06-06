#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:23:06 2021

@author: aditi
"""
print('Q3\nFor \n\
x = 1-exp(-c*x)')
from math import exp
from numpy import arange

def fp_iteration(x,c):
    val = x - (1-exp(-c*x))
    i=0
    while abs(val) > 10**-7 and i<1000:
        xn = (1-exp(-c*x))
        x = xn
        val = x - (1-exp(-c*x))
        i+=1
    return x

print('\n(a) For c = 2, x* =',fp_iteration(1,2))
print('\n(b) For a series of values of c:\n\
c\t\tx*')

cval = arange(0,3.01,0.01)
for c in cval:
    xval=fp_iteration(1,c)
    print(' %.2f\t\t%f' % (c,xval))

print('Transition from 0 to non-zero fixed point is seen at\n\
c* = 1')

'''
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
'''
