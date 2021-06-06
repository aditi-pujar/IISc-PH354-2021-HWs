#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:07:11 2021

@author: aditi
"""
'''
I have mislabelled it, this is actually Q5, could not crrect it, my apologies
'''
import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack


def modify2(fftval,percentage):
    N = len(fftval)
    n = int((percentage/100)*N)
    new_fftval = np.append(np.array(fftval[0:n]),np.zeros(N-n))
    #new_freq = np.append(np.array(freq[0:n]),np.zeros(N-n))
    return new_fftval

dow = np.loadtxt('./dow2.txt')
time = np.arange(0,len(dow),1)
plt.figure()
plt.plot(time,dow)
plt.title('DOW Data')
plt.xlabel('t'); plt.ylabel('f(t)')
plt.savefig('Q4(1).png')


#######################################################
fftdow = np.fft.rfft(dow)
fftdow_mod = modify2(fftdow,2)
dowDFT = np.fft.irfft(fftdow_mod)

plt.figure()
plt.plot(time,dow,time,dowDFT)
plt.title('DOW Data and its 2% DFT Reconstruction')
plt.xlabel('t'); plt.ylabel('f(t)')
plt.legend(['Data','2% Inv DFT Reconstruction'])
plt.savefig('Q4(2).png')


#########################################################
dctdow = fftpack.dct(dow,norm='ortho')
dctdow_mod = modify2(dctdow,2)
dowDCT = fftpack.idct(dctdow_mod,norm='ortho')

plt.figure()
plt.plot(time,dow,time,dowDCT)
plt.title('DOW Data and its 2% DCT Recosntruction')
plt.xlabel('t'); plt.ylabel('f(t)')
plt.legend(['Data','2% Inv DCT Reconstruction'])
plt.savefig('Q4(3).png')