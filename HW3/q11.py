#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 05:23:10 2021

@author: aditi
"""
#q11

import numpy as np

def partial_pivoting(A_input,b_input):
    #print('\nA=\n',A,'\n\nb=',b)
    A = np.copy(A_input); b = np.copy(b_input)
    N = len(b)
    for i in range(N):
        index = np.argmax(np.abs(A[i:,i]))
        if (index != 0):
            A[[i,i+index]] = A[[i+index,i]]
            tmpB = b[i]; b[i] = b[i+index]; b[i+index] = tmpB;

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
    return x

###################################################
print('(Q11)')

#a From Q10:
Vplus = 5
A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],dtype=np.float32)
b = np.array([Vplus,0,Vplus,0],dtype = np.float32)

x = partial_pivoting(A,b)
q10_ans = np.array([3.,1.66666675,3.33333325,2.])
print('(a)')
print('A =\n',A,'\n\nb=',b)
print('\nPartial Pivoting Solution:\n',x)
print('\nGaussian Elimination without Partial Pivoting:\n', q10_ans)
print('Thus, both methods give the same solution.\n\n')

#b
A = np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,2]],dtype=np.float64)
b = np.array([-4,3,9,7],dtype=np.float64)
x = partial_pivoting(A,b)

print('(b)')
print('A =\n',A,'\n\nb=',b)
print('Partial Pivoting Solution:',x)
