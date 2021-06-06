#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:05:45 2021

@author: aditi
"""
from math import exp
from matplotlib import pyplot as plt
from numpy import linspace

#constants
vplus = 5
R1 = 1*10**3
R2 = 4*10**3
R3 = 3*10**3
R4 = 2*10**3
Vt = 0.05
I0 = 3*10**-9

alpha = R2*R3-R4*R1
beta = -(R1+R2)*(R3+R4)
gamma = -(R1*R2*(R3+R4)+R3*R4*(R1+R2))

def i3(x):
    return I0*(exp(x/Vt)-1)

def Di3(x):
    return (I0/Vt)*(exp(x/Vt))

def f(x):
    return alpha*vplus + beta*x + gamma*i3(x)

def df(x):
    return beta + gamma*Di3(x)


fval = []
x_ax = []
xval = linspace(0,0.7)
for x in xval:
    fval.append(f(x))
    x_ax.append(0)

plt.figure()
plt.plot(xval,fval,xval,x_ax)
plt.title('Graphing to get guesses')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)','X Axis'])

'''
Thus, initial guesses obtained for the roots of \
f(x) (the voltage drop across diode)
(for using Newton Method):
    x = 0.6
'''

def Newton(x,eps,f,df):
    while ((f(x)>eps)): #and (df(x)!=0)):
        #print(x,f(x))
        xn = x - f(x)/(df(x))
        x = xn
    return x

eps = 10**-5
x1 = Newton(0.6,eps,f,df)
print('\n\n Voltage across diode (x) =', x1)
print('The above agrees with the engineers thumb rule.\n\
Now:')

V1 = (R1*R2/(R1+R2))*(vplus/R1-i3(x1))
V2 = V1-x1
print('V1 =',V1)
print('V2=',V2)
