#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:03:08 2021

@author: aditi
"""
from numpy import linspace, zeros
from matplotlib import pyplot as plt

#constants
G = 6.674*10**-11
Me = 5.974*10**24
Mm = 7.348*10**22
R = 3.844*10**8
w = 2.662*10*-6

def f(rr):
    r = rr*10**8
    val = r - (G/(w*w))*( Me/(r*r)-Mm/((R-r)*(R-r)) )
    return val

rval = linspace(0.001,1)
x_ax=zeros(len(rval))
fR=[]
for r in rval:
    fR.append(f(r))


plt.figure()
plt.plot(rval,fR,rval,x_ax)

print('Lagrange value point r =')


def secant(x0,x1,f):
    while f(x1)>10**-5:
        x = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x
    return x1
