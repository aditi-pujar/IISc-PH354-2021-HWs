#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:44:50 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = np.pi/20e-6
w = 200e-6
W = 200e-5

Lambda = 500e-9
f = 1
N = int(1000)

un_w = np.arange(-w/2,w/2,w/N)
seq = np.sin(alpha*un_w)
yn_w = np.sqrt(seq*seq)
yn = np.hstack((np.zeros(int(9*N/2)),seq,np.zeros(int(9*N/2))))

I = (W*W/(N*N))*(np.abs(np.fft.fft(yn))**2)

# number of points that would be visible on screen
spacing = Lambda*f/W
n = 10e-2/spacing

# k = 0 would correspond to xk = 0,i.e. 
#at the centre of the screen:

xval = np.arange(-5e-2,5e-2,spacing)
#x = np.hstack((np.flip(-xval[:int(n/2)]),xval[:int(n/2)]))
Inew = np.hstack((np.flip(I[:int(n/2)]),I[:int(n/2)]))

plt.figure()
plt.plot(xval,Inew)
plt.title('(Q7) Intensity v/s x')
plt.xlabel('x'); plt.ylabel('I(x)');
plt.savefig('Q7_Diffraction_Plot.png')

pattern = np.zeros((50,len(Inew)))
for i in range(50):
    pattern[i,:] = Inew

plt.figure()
plt.pcolor(xval,np.arange(50),pattern,cmap='gray')
plt.title('(Q7) Diffraction Pattern')
plt.savefig('Q7_Diffraction_Pattern.png')


'''
y = np.linspace(-0.8,0.8,10) #cm
XX,YY = np.meshgrid(x,y)
line = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        line[j,i] = I[i]

plt.figure(figsize=(13,1))
plt.pcolor(x*1e-7,y,line*1e-10,cmap='gray',vmax=0.1)
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('7_2.png')
plt.show()
'''


'''
d = 20*1e3 #nm
alpha = np.pi/d 
slits = 10
wavl = 500 #nm
f = 1*1e9 #nm
N = 1000
w = slits*d
enlarge_factor = 10
W = enlarge_factor*w

q = lambda u: np.sin(alpha*u)**2

u = np.linspace(-w/2,w/2,N)
q = q(u)
q = np.hstack((np.zeros(int(N*((enlarge_factor-1)/2))),q,np.zeros(int(N*((enlarge_factor-1)/2)))))

N *= enlarge_factor
width = np.linspace(-W/2,W/2,N)

y = np.abs(np.sqrt(q))
xlim = (N-1)*wavl*f/W
x = np.linspace(0,xlim,N)
I = (W/N)**2*np.abs(np.fft.fft(y))**2
L = 5*1e7 #nm
till = int(L/(wavl*f/W))


xnew = np.hstack((np.flip(-x[:till]),x[:till]))
Inew = np.hstack((np.flip(I[:till]),I[:till]))
'''