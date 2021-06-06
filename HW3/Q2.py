#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:47:10 2021

@author: aditi
"""
print('Q2:\n')

def f(x):
    return x*(x-1)

def analytical_df(x):
    return 2*x-1

def numerical_df(x,delta):
    return (f(x+delta)-f(x))/(delta)

print('For f(x) = x*(x-1) at x = 1:')
print('(a) For delta = 10^-2,\n\
Numerical f\'(1) = ',numerical_df(1,10**-2),'\n\
Analytical f\'(1) = ',analytical_df(1))

a_val = analytical_df(1)
    
print('The two values do not perfectly agree because:\n\
While calculating numerically, the delta value is still rather big and \n\
so cannot really be taken as tending to 0')

print('\n(b)\n delta\tNumerical f\'(1)\t\tError')
DELTA = [10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]

for deltaval in DELTA:
    val = numerical_df(1,deltaval)
    print(deltaval,'\t',val,'\t',abs(a_val-val))

print('\n\
(1)Initially the error value decreases because as we are taking smaller delta values\
=> better approximation, as delta tends to 0, i.e. truncation error reduces\n\
However:\n\
(2) Beyond a point, errors start to increase because:\n\
While numerically calculating derivative, we are subtracting two \
almost equal numbers and then dividing by a very small number too\n\
=> Both of which are known to cause loss in accuracy in machine representation\n\n\
Build up in round off error overcomes decrease in truncation error, leading overall increase in error')