#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 05:24:28 2021

@author: aditi
"""

from scipy.constants import h,c,k, Wien
from matplotlib import pyplot as plt
from numpy import linspace
from math import exp

def f(lvalue,T):
    l = lvalue*10**-9
    const = h*c/(k*T)
    den = exp(const/l) - 1
    return l - (const/5)*(1+1/den)

''' For a given temperature T,
    f(l,T) = 0 is the equation we need to find roots of.
'''

#q5a
#testing for T = 4500K, lambda_max ~ 600 nm
T = 4500

##########################################################
#graphing to get interval for bisection method

dIval = []
x_ax = []
lval = linspace(50,2000)
for l in lval:
    dIval.append(f(l,T))
    x_ax.append(0)

plt.figure(1)
plt.plot(lval,dIval,lval,x_ax)
plt.title('(Q5) T = 4500K')
plt.xlabel(r'$\lambda$ (nm)')
plt.ylabel(r'$\frac{dI}{d\lambda}$')
plt.legend([r'$\frac{dI}{d\lambda}$','X Axis'])

####################################################
''' Thus, we get interval over which to take bisection:
    a = 500
    b = 750
'''

def bisection(a,b,T):
    if f(a,T)*f(b,T)>0:
        return 999999
    while (b-a) >= 10**-6:
        c = (a+b)/2
        if f(a,T)*f(c,T)<0:
            b = c
        else:
            a = c
    return c

lambdaval = bisection(500,750,4500)
bval = lambdaval*T*10**-9
err = abs(bval-Wien)*100/Wien
print('(5a) For T = 4500K, we got:\n\
Limits of Interval:\n\
A = 500 nm\n\
B = 750 nm\n\
lambda_max =',lambdaval,'nm\n\n\
And by Wien Displacement Law:\n\
    b =',bval,'\n\
    Literature value =', Wien,'\n\
    % Error =',err,'\n')

lambda_sun = 502*10**-9
T_sun = bval/lambda_sun

print('(5b) For Sun, given lambda_max = 502 nm\n\
=> Temperature of Sun = b/lambda_max\n\
=',T_sun,'K')
