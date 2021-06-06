#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:48:56 2021

@author: aditi
"""
####################################################
#Q3
print('Exercise 3:')
from math import exp
#from common_functions import SimpsonRule
def SimpsonRule(a,b,n):
    I=0
    h=(b-a)/n
    if n%2==0:
        for i in range(0,n,2):
            x0 = a+i*h; x1 = x0+h; x2 = x1+h;
            f0 = f(x0); f1 = f(x1); f2 = f(x2);
            I+=f0+4*f1+f2
        I*=h/3
        return I
    else:
        for i in range(0,n-1,2):
            x0 = a+i*h; x1 = x0+h; x2 = x1+h;
            f0 = f(x0); f1 = f(x1); f2 = f(x2);
            I+=f0+4*f1+f2
        I*=h/3
        x3 = x2+h; f3=f(x3);
        final_interval=(h/2)*(f2+f3) #treated using Trapezoidal
        I+=final_interval
        return I

def TrapezoidalRule(a,b,n):
    if n>0 and b>a:
        I=0
        h=(b-a)/n
        for i in range(n):
            x0 = a+i*h; x1 = x0+h;
            f0 = f(x0); f1 = f(x1);
            I+= f0+f1
        I*=h/2
        return I

def f(t):
    return exp(-t**2)

'''I will choose the Simpson's Rule because it has 
increased accuracy over Trapezoidal Rule (O(h^4) over O(h^2))'''

print('(a) Calculating E(x) for given range of x\
 using Simpson\'s 1/3rd Rule:\n\n\
x\t\tE(x)')
# Number of slices should be a function of size of interval
# n = (b-a)*100
E=[0]; x=[0];
print('%.1f\t\t%f' %(x[0],E[0]))
for k in range(1,31):
    xval = k*0.1
    n = int(xval*100)
    x.append(xval)
    E.append(SimpsonRule(0,xval,n))
    print('%.1f\t\t%f'%(x[k],E[k]))

from matplotlib import pyplot as plt
print('(b) Plotting E(x) v/s x:\nWe can see it rapidly saturates\
 to (\u03C0)^(1/2)/2, as expected for a half Gaussian.')
plt.figure(1)
plt.plot(x,E,x,E,'ro')
plt.title('Q3(b) E(x) v/s x')
plt.xlabel('x')
plt.ylabel('E(x)')

