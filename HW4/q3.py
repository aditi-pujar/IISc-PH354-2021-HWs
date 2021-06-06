#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:15:37 2021

@author: aditi
"""

import numpy as np
from matplotlib import pyplot as plt

piano = np.loadtxt('./piano.txt')
trumpet = np.loadtxt('./trumpet.txt')

N = len(piano)
omega = 44100
t0 = 1/omega
t = np.arange(t0,(N+1)*t0,t0)

plt.figure()
plt.plot(t,piano)
plt.title('Piano Notes Played')
plt.xlabel(r'Time (s)'); plt.ylabel(r'Piano Notes $f_P(t)$')
plt.savefig('Piano_Notes.png')

plt.figure()
plt.plot(t,trumpet)
plt.title('Trumpet Notes Played')
plt.xlabel(r'Time (s)'); plt.ylabel(r'Trumpet Notes $f_T(t)$')
plt.savefig('Trumpet_Notes.png')

frequency = np.linspace(0,omega,N)
fftpiano = np.abs(np.fft.fft(piano))
ffttrumpet = np.abs(np.fft.fft(trumpet))

Nn = 10000 #plotting only first 10,000 coefficients

plt.figure()
plt.plot(frequency[0:Nn],fftpiano[0:Nn])
plt.title('Piano FFT (First 10,000 coefficients)')
plt.xlabel('$\omega$ (Hz)'); plt.ylabel('$\~f(\omega)$');
plt.savefig('Piano_FFT.png')

plt.figure()
plt.plot(frequency[0:Nn],ffttrumpet[0:Nn])
plt.title('Trumpet FFT (First 10,000 coefficients)')
plt.xlabel('$\omega$ (Hz)'); plt.ylabel('$\~f(\omega)$');
plt.savefig('Trumpet_FFT.png')

'''
Peaks are evenly spaced in the Fourier transform plot
=> multiple harmonics (integer multiples) of the 
same frequency being played.

We can conclude that in trumpet, for a given note.
more harmonics are played compared to piano (greater number of peaks)
=> richer sound but less clear notes

Note being played can be found by taking difference between peaks:
'''
from scipy.signal import find_peaks
peak_piano = find_peaks(fftpiano[0:Nn],distance=100*omega/N, threshold=1e6)[0]
peak_trumpet = find_peaks(ffttrumpet[0:Nn],distance=100*omega/N,threshold=1e7)[0]

f0_piano = np.diff(np.array([frequency[i] for i in peak_piano]))
f0_trumpet = np.diff(np.array([frequency[i] for i in peak_trumpet]))

'''
f0_piano =
array([ 526.11826118,  527.00027   , 1075.16875169])

f0_trumpet =
array([520.82620826, 523.03123031, 522.14922149, 522.14922149,
       520.38520385])

Therefore, fundamental frequency ~= 522Hz.
As this is double the frequency of the middle C note
(261 Hz), this could be the "high" C note of the next octave.
'''
print('Fundamental frequency ~= 522Hz.')