#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:15:30 2021

@author: aditi
"""
from numpy import linspace
from matplotlib import pyplot as plt

def P(x):
    return 924*x**6-2772*x**5+3150*x**4-\
        1680*x**3+420*x**2-42*x+1

def dP(x):
    return 924*6*x**5-2772*5*x**4+3150*4*x**3-\
        1680*3*x**2+420*2*x-42

#graphing to get initial guesses
Pval = []
x_ax = []
xval = linspace(-0.01,1,1000)
for x in xval:
    Pval.append(P(x))
    x_ax.append(0)

plt.figure(1)
plt.plot(xval,Pval,xval,x_ax)
plt.title('Graphing to get intervals of roots')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend(['P(x)','X Axis'])

'''
Thus, initial guesses obtained for the 6 roots of \
polynomial (for using Newton Method):
x1* = 0
x2* = 0.2
x3* = 0.4
x4* = 0.6
x5* = 0.8
x6* = 1
'''

def Newton(x,eps,f,df):
    while ((f(x)>eps) and (df(x)!=0)):
        #print(x,f(x))
        xn = x - f(x)/(df(x))
        x = xn
    return x

print('Roots of Polynomial:')
eps = 10**-10
xvalue = [0,0.2,0.4,0.6,0.8,1]
for i in range(6):
    val = Newton(xvalue[i],eps,P,dP)
    print('x(',i+1,') =', val)
