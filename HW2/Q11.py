#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:23:02 2021

@author: aditi
"""
from gaussxw import gaussxwab
import math
from numpy import linspace
#Q11
print('Exercise 11: Diffracted Intensity of Blocked Plane Wave')
#(a)
lambdaval = 1
z = 3

def u(x):
    return x*math.sqrt(2/(lambdaval*z))

def Cintegrand(t):
    return math.cos(math.pi*t*t/2)
def Sintegrand(t):
    return math.sin(math.pi*t*t/2)

def CT(u):
    a=0
    b=u
    N=50
    x,w = gaussxwab(N,a,b)
    I1=0; I2=0;
    for i in range(N):
        I1+= w[i]*Cintegrand(x[i])
        I2+= w[i]*Sintegrand(x[i])
    return I1,I2

def relativeI(x):
    uval=u(x)
    Cu,Su = CT(uval)
    
    val = (1/8)*((2*Cu+1)**2+(2*Su+1)**2)
    return val

xval = linspace(-5,5,100)
Ival=[]
for x in xval:
    Ival.append(relativeI(x))

from matplotlib import pyplot as plt
plt.figure()
plt.plot(xval,Ival)
plt.title('(Q11) Intensity of Diffracted Sound v/s x-position')
plt.xlabel('x (m)')
plt.ylabel('I/I0')
print('Significant variation in I/I0 seen.')