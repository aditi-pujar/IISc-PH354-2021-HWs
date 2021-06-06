#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:58:15 2021

@author: aditi
"""
from gaussxw import gaussxwab
import math
from numpy import linspace
#Q13
print('Exercise 13: Uncertainty in Quantum Harmonic Oscillator')
#(a)
def H(n,x):
    Hval=0
    N = math.floor(n/2)
    for l in range(0,N+1):
        num=((-1)**l)*((2*x)**(n-2*l))
        den=math.factorial(l)*(math.factorial(n-2*l))
        Hval+=num/den
    Hval*=math.factorial(n)
    return Hval

def psi(n,x):
    k=1/(math.sqrt((2**n)*math.factorial(n)\
                   *math.sqrt(math.pi)))
    val=k*math.exp(-x*x/2)*H(n,x)
    return val

from matplotlib import pyplot as plt
plt.figure(1)
Hval=[];
x=linspace(-4,4,100)
for nval in range(0,4):
    Hn=[]
    for xval in x:
        Hn.append(psi(nval,xval))
    Hval.append(Hn)
    plt.plot(x,Hn)
plt.title('(Q13a) Wave Functions of 1D Harmonic Oscillator\n\
For n = 0, 1, 2 3')
plt.xlabel('x')
plt.ylabel('psi_n(x)')
plt.legend(['n = 0','n = 1','n = 2', 'n = 3'])
plt.show()

#(b)
x=linspace(-10,10,1000000)
H30=[]
for xval in x:
    H30.append(psi(nval,xval))
plt.figure(2)
plt.plot(x,H30)
plt.title('(Q13b) Wave Functions of 1D Harmonic Oscillator\n\
For n = 30')
plt.xlabel('x')
plt.ylabel('psi_30(x)')
plt.legend(['n = 30'])
plt.show()

#(c)

def integrand(n,x):
    val = x*x*(psi(n,x)**2)
    #y = math.atan(x)
    dy = 1/(1+x*x)
    return val*dy

def uncertainty(n):
    b = math.pi/2
    a = -math.pi/2
    N = 100
    y,w = gaussxwab(N,a,b)
    I=0
    for i in range(N):
        xval=math.tan(y[i])
        I+= w[i]*integrand(n,xval)
    val = math.sqrt(I)
    return val

print('(c) For n = 5, the uncertainty in RMS position\
\n<x^2> is\n=', uncertainty(5))




