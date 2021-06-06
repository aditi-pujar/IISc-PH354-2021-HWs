#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:17:36 2021

@author: aditi
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./blur.txt')
LY = data.shape[0]
LX = data.shape[1]

xval = np.arange(0,LX,1)
yval = np.arange(0,LY,1)

plt.figure()
plt.pcolormesh(xval,-yval,data)
plt.savefig('Q8(1)_BlurredImage.png')

'''
For the spread function to be periodic over (0,LX) along X axis:
    normal(0,sigma) is symmetric across Y axis only.
    normal(LX,sigma) is symmetric about line x = L 
    => normal(0,sigma) + normal(LX,sigma) will be periodic over length LX
'''

sigma = 25
normal = lambda x, mean: np.exp(-(x-mean)**2/(2*sigma**2))
normal_sum = lambda x, l: normal(x,0)+normal(x,l)

def pt_spread_fn(x,y):
    #As x and y can be draw independantly
    fxval = np.array(normal_sum(x,LX))
    fyval = np.array(normal_sum(y,LY))
    
    fxval, fyval = np.meshgrid(fxval,fyval)
    res = fxval*fyval #summing the independant components
    return res

ptspread_val = pt_spread_fn(xval,yval)
plt.figure()
plt.pcolormesh(xval,-yval,ptspread_val)
plt.savefig('Q8(2)_PointSpreadFn.png')

####################################################

ptspread_fft = np.fft.rfft2(ptspread_val,axes=(-1,-2))
blur_fft = np.fft.rfft2(data,axes=(-1,-2))
eps = 1e-3

ptspread_fft_mod = np.piecewise(ptspread_fft,[np.abs(ptspread_fft)<eps],[eps, lambda ptspread_fft: ptspread_fft])
sharp_fft = blur_fft/ptspread_fft_mod
sharp = np.fft.irfft2(sharp_fft,axes=(-1,-2))

plt.figure()
plt.pcolormesh(xval,-yval,sharp)
plt.savefig('Q8(3)_Sharp.png')

