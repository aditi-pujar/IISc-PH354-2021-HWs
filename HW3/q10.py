#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:42:29 2021

@author: aditi
"""

import numpy as np

def gaussian_elimination(A_input,b_input):
    A = np.copy(A_input); b = np.copy(b_input)
    N = len(b)
    for i in range(N):
        aival = float(A[i,i])
        A[i,:] = A[i,:].astype(float)/aival; b[i] /=aival
        for j in range(i+1,N):
            ajval = float(A[j,i])
            A[j,:] = A[j,:] - ajval*A[i,:]; b[j] -= ajval*b[i]
#back substitution
    x = np.zeros(N)
    for k in range(N):
        kval = (N-1)-k
        x[kval] = b[kval]
        b[:kval]= b[:kval] - A[:kval,kval]*x[kval]
        #b[kval+1:]= b[kval+1:] - A[kval+1:,kval]*x[kval]
    return x

Vplus = 5
A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],dtype=np.float32)
b = np.array([Vplus,0,Vplus,0],dtype=np.float32)

x = gaussian_elimination(A,b)

print('(Q10)')
print('A =\n',A,'\n\nb=',b)
print('By Gaussian Elimination, voltages =\n', x)