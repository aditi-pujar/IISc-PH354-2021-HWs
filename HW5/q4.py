#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:15:49 2021

@author: aditi
"""
#4
import numpy as np
import random as rd

N = int(1e4)
f = lambda x: np.sin(np.floor(1/(x*(2-x))))
I1 = 0; A = 2; I2 = 0; varI2 = 0;

for i in range(N):
    #xval = rd.random(); yval = rd.random()
    if (f(rd.uniform(0.0,2.0))<= rd.uniform(0.0,2.0)):
        I1 = I1+1
    val = f(rd.uniform(0.0,2.0))
    I2 = I2 + val
    varI2 = varI2 + val*val

I1 = 2*I1/N
std_devI1 = np.sqrt(2*I1-I1*I1)
I2 = 2*I2/N
varI2 = 4*varI2/N
std_devI2 = np.sqrt(varI2 - I2*I2)

print('(4a) Integral using hit-and-miss Monte Carlo:', I1,'\n\
\tStandard Deviation =',std_devI1)
print('(4b) Integral using Mean Value Method:', I2,'\n\
\tStandard Deviation =',std_devI2)

'''
As expected, the error is slightly less \
for the mean value method over hit-and-miss
'''
