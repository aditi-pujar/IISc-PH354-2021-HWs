#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:17:11 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt

def myfft(x):
    N = len(x)
    if N%2 == 0 and N!=0:
        if N/2 == 1:
            return mydft2(x)
        else:
            xeven = [x[2*i] for i in range(0,int(N/2))]
            xodd = [x[2*i+1] for i in range(0,int(N/2))]
            E = myfft(xeven)
            O = myfft(xodd)
            factor = np.exp(-2j*np.pi*np.arange(N//2)/N)
            return np.append(np.array([E+factor*O]),np.array([E-factor*O]))
    else:
        raise ValueError('Length of input must be of form 2^m for some non zero m')


def mydft2(x):
    if (len(x)!=2):
        raise ValueError('Length of input must be 2')
    else:
        x=np.array(x)
        val = x[0]+x[1]*np.exp(-2j*np.pi*1/2)
        return val

data = np.loadtxt('./pitch.txt')
myfft_pitch = np.abs(myfft(data))
fft_pitch = np.abs(np.fft.fft(data))

freq = np.arange(0,len(data),1)

plt.figure()
plt.plot(freq,myfft_pitch,freq,fft_pitch)
plt.title('Comparing user defined and built in FFT')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.legend(['User Defined','Python Fn'])
plt.savefig('Q6_1.png')

'''
As they are almost coincident, they have been plotted separately
'''
plt.figure()
plt.plot(freq,myfft_pitch)
plt.title('User Defined FFT')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.savefig('Q6_2.png')

plt.figure()
plt.plot(freq,fft_pitch)
plt.title('Built In Python FFT')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.savefig('Q6_3.png')