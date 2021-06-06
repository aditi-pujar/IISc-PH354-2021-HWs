#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:02:22 2021

@author: aditi
"""

#6
import random as rd
import math

N = int(1e6)
fbyw = lambda x: 1/(1+math.exp(x))
f = lambda x: 1/((1+math.exp(x))*math.sqrt(x))
w = lambda x: 1/math.sqrt(x)
xfn = lambda z: (z*z)

sumval = 0
for i in range(N):
    zval = 1-rd.random()
    val = xfn(zval)
    try:
        sumval = sumval + fbyw(val)
    except OverflowError:
        sumval =sumval + 0
I = 2*sumval/N
print('Obtained value of integral:',I)
print('Expected value of integral: 0.84')