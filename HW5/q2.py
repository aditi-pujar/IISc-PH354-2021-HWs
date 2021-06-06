#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:17:26 2021

@author: aditi
"""
#2
import numpy as np
import random as rd
T = int(1e4)
dt = 1

tau_Bi = 46*60
tau_Tl = 2.2*60
tau_Pb = 3.3*60

nBi = np.zeros(T+1)
nTl = np.zeros(T+1)
nPb = np.zeros(T+1)
nBi_stable = np.zeros(T+1)

nBi[0] = int(1e4)
nTl[0] = 0
nPb[0] = 0
nBi_stable[0] = 0


def toss(tau):
    return (rd.random() <= (1-2**(-dt/tau) ))

def decay(nX,tau_X):
    d_X = 0
    for i in range(nX):
        if (toss(tau_X)):
            d_X += 1
    return d_X


for t in np.arange(1,T+1):
    if nPb[t-1] != 0:
        d_Pb = decay(int(nPb[t-1]),tau_Pb)
        nPb[t] = nPb[t-1] - d_Pb
        nBi_stable[t] = nBi_stable[t-1] + d_Pb

    if nTl[t-1] != 0:
        d_Tl = decay(int(nTl[t-1]),tau_Tl)
        nTl[t] = nTl[t-1] - d_Tl
        nPb[t] = nPb[t-1] + d_Tl

    if nBi[t-1] != 0:
        decay_Pb = 0; decay_Tl = 0;
        for i in range(int(nBi[t-1])):
            if (toss(tau_Bi)): #decides to decay
                if (rd.random()<= 0.9791): #decays to Pb
                    decay_Pb += 1
                else:
                    decay_Tl += 1

        nBi[t] = nBi[t-1] - decay_Tl - decay_Pb
        nPb[t] = nPb[t-1] + decay_Pb
        nTl[t] = nTl[t-1] + decay_Tl

from matplotlib import pyplot as plt
time = np.arange(T+1)

plt.figure()
plt.plot(time,nBi,time,nPb,time,nTl,time,nBi_stable)
plt.legend(['Bi-213 (unstable)','Tl-209','Pb-209','Bi-209 (stable)'])
plt.title('(Q2) Time Evolution of Element Conc.')
plt.xlabel('Time (s)'); plt.ylabel('No of Atoms')
#plt.savefig('Q2.png')
