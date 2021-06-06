#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:54:42 2021

@author: aditi
"""

from gaussxw import gaussxwab
from scipy import constants
import math
from numpy import linspace
#Q9
print('Exercise 10: Time Period of Anharmonic Oscillator')
#(a)
def V(x):
    return x**4

def integrand(x,m,a):
    if x==a:
        xval = 0
    else:
        xval = math.sqrt(m/2)/(math.sqrt(V(a)-V(x)))
    return xval

def T(amplitude):
    m = 1
    b = 0
    a = amplitude
    x,w = gaussxwab(20,a,b)
    I=0
    for i in range(20):
        I+= w[i]*integrand(x[i],m,amplitude)
    time_period = 4*I
    return time_period

#(b)
aval = linspace(0,2,100)
Tval=[]
for a in aval:
    Tval.append(T(a))

from matplotlib import pyplot as plt
plt.figure()
plt.plot(aval,Tval)
plt.title('(Q10b) Time Period of Oscillator (T) v/s Amplitude (a)')
plt.xlabel('Amplitude (a)')
plt.ylabel('Time Period (T)')