#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:17:49 2021

@author: aditi
"""

'''
I have mislabelled it, this is actually Q4, could not correct it, my apologies
'''

import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt('./dow.txt')
time = np.arange(0,len(dow),1)

plt.figure()
plt.plot(time,dow)
plt.title('Dow Jones Industrial Average')
plt.xlabel('No of Days'); plt.ylabel('Value of DJIA')
plt.savefig('Q5(1)_DowJones_Plot.png')

N = len(dow)
freq = np.linspace(0,1,N//2+1)
fftdow = np.fft.rfft(dow)
powspec = np.abs(fftdow)**2

plt.figure()
plt.plot(freq,powspec)
plt.title('Power Spectrum of Dow Jones Industrial Average')
plt.xlabel('k'); plt.ylabel('$|c(k)|^2$')
plt.savefig('Q5(2)_PowerSpectrum_DowJones.png')

def modify(fftval,freq,percentage):
    N = len(fftval)
    n = int((percentage/100)*N)
    new_fftval = np.append(np.array(fftval[0:n]),np.zeros(N-n))
    new_freq = np.append(np.array(freq[0:n]),np.zeros(N-n))
    return new_fftval, new_freq

fftdow1,freq1 = modify(fftdow,freq,10)
fftdow2,freq2 = modify(fftdow,freq,2)

dow0 = np.fft.irfft(fftdow)
dow1 = np.fft.irfft(fftdow1)
dow2 = np.fft.irfft(fftdow2)

plt.figure()
plt.plot(time,dow,time,dow1)
plt.title('Comparing DOW data and Inv Transformed DOW (10%)')
plt.legend(['DOW Data','Inv transf DOW (10%)'])
plt.xlabel('t (Days)'); plt.ylabel('f(t)')
plt.savefig('Q5(3).png')

plt.figure()
plt.plot(time,dow,time,dow2)
plt.title('Comparing DOW data and Inv Transformed DOW (2%)')
plt.legend(['DOW Data','Inv transf DOW (2%)'])
plt.xlabel('t (Days)'); plt.ylabel('f(t)')
plt.savefig('Q5(4).png')

'''
We can see that setting Fourier coefficients to 0 
smoothens the function we get, upon taking an inverse transform.

This is to be expected as we are abandoning higher frequency contributions.
The fewer coefficients we take,
Smoother the function,

But more artefacts and wiggles set in too
As the high frequency terms are important for cancelling these out.
'''

######################################################
from math import floor

sq = np.array([(-1)**floor(2*t) for t in np.linspace(0,1,1000)])
FFT_sq = np.fft.rfft(sq)
frequency = np.linspace(0,1,1000)
modFFTsq,modfreq = modify(FFT_sq,frequency,1)

inv_sq = np.fft.irfft(modFFTsq)
xaxis = np.arange(1000)
plt.figure()
plt.plot(xaxis,sq,xaxis,inv_sq)
plt.title('Square Wave and its Reconstruction')
plt.xlabel('f(t)'); plt.ylabel('t')
plt.legend(['Square Wave','Reconstruction from Inv FT'])
plt.savefig('Q5(5).png')

'''
The wiggles come about because, now our function is a
sum of only a few functions with low frequencies.

Initially they would have been cancelled out
had we included higher frequency Fourier components. As we did not consider those,
these are no longer cancelled out. 

The sharper a function is in time space, the more extended it is in Fourier space and vice versa.

'''
