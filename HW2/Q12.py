#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:57:09 2021

@author: aditi
"""

from gaussxw import gaussxwab
import math
#Q9
print('Exercise 12: Stephan Boltzmann constant')
#(a)
def integrand(x):
    try:
        val=(x**3/(math.exp(x)-1))/(1+x*x)
        return val
    except:
        return 0

'''
    y=x/(1+x)
    numval = (y**3)
    denval = (math.exp(y/(1-y))-1)*((1-y)**5)
    val = numval/denval
'''


b = math.pi/2
a = 0
N = 50
y,w = gaussxwab(N,a,b)
I=0
x=[]; val=[];
for i in range(N):
    xval=math.tan(y[i])
    I+= w[i]*integrand(xval)
#    x.append(xval)
#    print(integrand(xval))
print(I)

'''
for j in range(N):
    ii = w[j]*integrand(x[j])
    print(ii)
'''