#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:49:39 2021

@author: aditi
"""
import numpy as np
from math import sin, pi

N = int(1.0e3)

sqwave = np.append(np.ones(int(N/2)),-1*np.ones(int(N/2)))
fft_sqwave = np.abs(np.fft.fft(sqwave))

sawtooth = np.linspace(1,N,num=N)
fft_sawtooth = np.abs(np.fft.fft(sawtooth))


modsine = np.array([sin(n*pi/N)*sin(20*n*pi/N) for n in range(1,N+1)])
fft_modsine = np.abs(np.fft.fft(modsine))

xaxis = np.linspace(0,1,N)

from matplotlib import pyplot as plt

plt.figure()
plt.plot(xaxis,sqwave)
plt.title('Square Wave')
plt.xlabel('n'); plt.ylabel('yn');
plt.savefig('Q1_SquareWave.png')

plt.figure()
plt.plot(xaxis,fft_sqwave)
plt.title('FFT Square Wave')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.savefig('Q1_FFTSquareWave.png')

plt.figure()
plt.plot(xaxis,sawtooth)
plt.title('Sawtooth Wave')
plt.xlabel('n'); plt.ylabel('yn');
plt.savefig('Q1_SawtoothWave.png')

plt.figure()
plt.plot(xaxis,fft_sawtooth)
plt.title('FFT Sawtooth Wave')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.savefig('Q1_FFTSawtoothWave.png')

plt.figure()
plt.plot(xaxis,modsine)
plt.title('Modulated Sine Wave')
plt.xlabel('n'); plt.ylabel('yn');
plt.savefig('Q1_ModSineWave.png')

plt.figure()
plt.plot(xaxis,fft_modsine)
plt.title('FFT Modulated Sine Wave')
plt.xlabel('k'); plt.ylabel('|c(k)|');
plt.savefig('Q1_FFTModSineWave.png')