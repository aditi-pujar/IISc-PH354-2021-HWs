#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:43:29 2021

@author: aditi
"""

import numpy as np

def solve_banded1(A_input,b_input):
    A = np.copy(A_input); b = np.copy(b_input)
    N = len(b)
    for i in range(N):
        aival = float(A[i,i])
        A[i,:] = A[i,:]/aival; b[i] /=aival

        if i!=N-1:
            m = len(A[i+1:,i][A[i+1:,i]!=0])
            for j in range(i+1,i+m+1):
                ajval = float(A[j,i])
                A[j,:] = A[j,:] - ajval*A[i,:]; b[j] -= ajval*b[i]

#back substitution
    x = np.zeros(N)
    for k in range(N):
        kval = (N-1)-k
        x[kval] = b[kval]
        b[:kval]= b[:kval] - A[:kval,kval]*x[kval]
    return x

vplus = 5

#a
A = np.array([[3,-1,-1,0,0,0],[-1,4,-1,-1,0,0],\
[-1,-1,4,-1,-1,0],[0,-1,-1,4,-1,-1],[0,0,-1,-1,4,-1],\
[0,0,0,-1,-1,3]],dtype=np.float32)
b = np.array([vplus,vplus,0,0,0,0],dtype = np.float32)
x = solve_banded1(A,b)

print('\nA=\n',A,'\n\nb=',b)
print('*******************************')
print('We get solution as x =',x)
print('Verifying Ax = b:\nAx =\n', A@x)
print('b=\n',b)

def matrixAb(N,vplus):
    firstA1 = np.hstack((np.array([3,-1,-1]),np.zeros(N-3)))
    firstA2 = np.hstack((np.array([-1,4,-1,-1]),np.zeros(N-4)))
    firstA = np.vstack((firstA1,firstA2))

    lastA1 = np.hstack( (np.zeros(N-4),np.array([-1,-1,4,-1])) )
    lastA2 = np.hstack( (np.zeros(N-3),np.array([-1,-1,3])) )
    lastA = np.vstack((lastA1,lastA2))

    main = np.array([-1,-1,4,-1,-1])

    A = np.copy(firstA)
    for i in range(N-4):
        zero1 = np.zeros(i)
        zero2 = np.zeros(N-(5+i))
        Ai = np.hstack((zero1,main,zero2))
        A = np.vstack((A,Ai))
    A = np.vstack((A,lastA))
    B = np.append(np.array([vplus,vplus]),np.zeros(N-2))
    return A,B

'''
Here we can see that the symmetry of A is such that
upon solving by Thomas Algorithm,
A is almost np.identity(N),
Thus no need for back-substitution step for large N
'''

def solve_banded2(A_input,b_input):
    A = np.copy(A_input); b = np.copy(b_input)
    N = len(b)
    for i in range(N):
        aival = float(A[i,i])
        A[i,:] = A[i,:]/aival; b[i] /=aival

        if i!=N-1:
            m = len(A[i+1:,i][A[i+1:,i]!=0])
            for j in range(i+1,i+m+1):
                ajval = float(A[j,i])
                A[j,:] = A[j,:] - ajval*A[i,:]; b[j] -= ajval*b[i]
    x = b
    return x


N = 1000
AN,bN = matrixAb(N,vplus)
VN = solve_banded1(AN,bN)
np.savetxt('potentials.txt', np.transpose(VN))