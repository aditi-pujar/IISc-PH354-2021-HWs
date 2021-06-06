#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:00:35 2021

@author: aditi
"""
#5
import random as rd
import numpy as np

N = int(1e6)
x= np.zeros(10)
f=0

for i in range(N):
    for j in range(10):
        x[j]=(rd.uniform(-1,1))
    fval = sum(x*x)
    if (fval<=1):
        f=f+1

I = (2**10)*f/N
print('Volume of hypersphere = ',I)
######################################################
