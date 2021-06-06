#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:51:41 2021

@author: aditi
"""

#Q18
print('Exercise 18: First 20 derivatives of given function\
around z = 0:')
print('m\tdf/dz|(z=0)')
import math
import cmath
N=10**4

def Z(k):
    return complex(math.cos(2*cmath.pi*k/N),math.sin(2*cmath.pi*k/N))

def f(z):
    return cmath.exp(2*z)

def dfdz(m):
    if (m%1 == 0) and (m>=0):
        kk = math.factorial(m)/N
        I=0
        for k in range(N):
            I+=f(Z(k))*complex(math.cos(-2*cmath.pi*k*m/N),math.sin(-2*cmath.pi*k*m/N))
        val=kk*I
        return val

derivf=[]
for i in range(1,21):
    val = dfdz(i)
    derivf.append(val)
    print(i,'\t',val)
