#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:33:44 2021

@author: aditi
"""

import numpy as np
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = np.loadtxt('./sunspots.txt')
time = data[:,0]
sunspots = data[:,1]
N = len(sunspots)

plt.figure()
plt.plot(time,sunspots)
plt.title('Sunspots Measured per Month (since January 1749)')
plt.xlabel('Time (in Months)'); plt.ylabel('# of Sunspots');
plt.savefig('Q2_1.png')

'''
Between 1500 - 2000 months, there are \
3 + 1/2 + 1/2 = 4 cycles 
=> estimate of time period ~ (2000-1500)/4
= 125 months.
'''

fft_sunspots = np.abs(np.fft.fft(sunspots))**2 # |ck|**2
#We want to plot |c(k)|^2 v/s t(k) (the time period corresponding to k)
delk = time[1]-time[0]
t = 1/np.linspace(0,1/delk,N) # in months

plt.figure()
plt.plot(t[1:],fft_sunspots[1:])
plt.title('FFT of Sunspots Measured per Month')
plt.xlabel('Time (in Months) (t(k))'); plt.ylabel('Contributions by each Frequency k (|c(k)|^2)');
plt.savefig('Q2_2.png')

# Ignoring peak at t = 0 (corresponding to infinite frequency)
plt.figure()
plt.plot(t[-50:-1],fft_sunspots[-50:-1])
plt.title('Power Spectrum of Sunspots (Zoomed in)')
plt.xlabel('Time (in Months) (t(k))'); plt.ylabel('Contributions by each Frequency k (|c(k)|^2)');
plt.savefig('Q2_3.png')

print('Dominant time period = ', t[np.argmax(fft_sunspots[1:])],' months.')

