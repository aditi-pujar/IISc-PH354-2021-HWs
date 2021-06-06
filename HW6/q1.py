#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:25:06 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

#########################################################################

def diff_vo(t,vo,RC):
    vin = (-1)**np.floor(2*t)
    return (vin-vo)/RC


t = np.linspace(0,10,1000)
plt.figure()
plt.plot(t,(-1)**np.floor(2*t))
plt.title('Q1 Input Signal Vin')
plt.xlabel('t'); plt.ylabel('Vin')
plt.savefig('Q1_Vin.png')


'''
As RC sets timescale for problem,
step size is taken accordingly
h = 0.1*RC

RC = [0.01,0.1,1]
=> h = [0.001,0.01,0.1]
'''

v0 = 0

RC = 1
h = RC*1e-2
t = np.arange(0,10,h)

v = RK4.RK4(diff_vo,v0,t,RC)
plt.figure()
plt.plot(t,v)
plt.title('Q1 Vout v/s t (RC  = %f)'% RC)
plt.xlabel('t'); plt.ylabel('Vin')
plt.savefig('Q1_RC=%f.png'%RC)

RC = 0.1
h = RC*1e-2
t = np.arange(0,10,h)

v = RK4.RK4(diff_vo,v0,t,RC)
plt.figure()
plt.plot(t,v)
plt.title('Q1 Vout v/s t (RC  = %f)'% RC)
plt.xlabel('t'); plt.ylabel('Vin')
plt.savefig('Q1_RC=%f.png'%RC)


RC = 0.01
h = RC*1e-2
t = np.arange(0,10,h)

v = RK4.RK4(diff_vo,v0,t,RC)
plt.figure()
plt.plot(t,v)
plt.title('Q1 Vout v/s t (RC  = %f)'% RC)
plt.xlabel('t'); plt.ylabel('Vin')
plt.savefig('Q1_RC=%f.png'%RC)

'''
Circuit acts like a low pass filter, allowing only those
with low frequencies to pass through with increasing values of
RC
thus the square shape form is distorted due to loss of higher
frequencis
'''