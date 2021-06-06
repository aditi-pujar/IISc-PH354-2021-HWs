#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 05:34:47 2021

@author: aditi
"""

from math import sqrt,tan,pi
from scipy.constants import m_e,hbar,e
from numpy import linspace
from matplotlib import pyplot as plt

w = 10**-9
V0 = 20*e
u0sq = m_e*(w**2)*V0/(2*hbar**2)

def f1(v):
    return sqrt(u0sq-v**2) - v*tan(v)

def f2(v):
    return sqrt(u0sq-v**2)*tan(v) + v

#graphing to get initial guesses
f1val = []
f2val = []
x_ax = []
vval = linspace(0.01,2*pi-0.01,50)
for v in vval:
    f1val.append(f1(v))
    f2val.append(f2(v))
    x_ax.append(0)

plt.figure()
plt.plot(vval,f1val,vval,f2val,vval,x_ax)
plt.title('Q6 Graphing to get intervals of roots')
plt.xlabel('v')
plt.ylabel('Symmetric and Antisymmetric Functions of v')
plt.legend(['f1(v)','f2(v)','X Axis'])

'''
Thus, intervals obtained for first 5 roots to for\
False Position root finding are approximately:
* f1(v) (Symmetric wavefns):
    [a1,b1] = [1,1.5]
    [a2,b2] = [3,4.5]
* f2(v) (Asymmetric wavefns):
    [a3,b3] = [2.5,4.2]
    [a4,b4] = [5,6]
    [a5,b5] = [0,1.5]
'''

def false_position(a,b,f):
    if f(a)*f(b)>0:
        return 999999
    i=0
    while i<1000:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        #print(b-a,'\t',c,'\t',f(c))
        if abs(f(c)) < (10**-5):
            break
        elif f(a)*f(c)<0:
            b = c
        else:
            a = c
        i+=1
    return c

def E(x):
    val = (2*hbar**2/(m_e*w**2))*x*x
    return val/e

print('First 5 eigen values of energy:')
a = [1,3,2.5,5,0]
b = [1.5,4.5,4.2,5.6,1.5]
for i in range(2):
    x = false_position(a[i],b[i],f1)
    Eval = E(x)
    print('E(',i,') = ',Eval)
    
for i in range(2,5):
    x = false_position(a[i],b[i],f2)
    Eval = E(x)
    print('E(',i,') = ',Eval)

def bisection(a,b,f):
    if f(a)*f(b)>0:
        return 999999
    while (b-a) >= 10**-6:
        c = (a+b)/2
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
    return c

