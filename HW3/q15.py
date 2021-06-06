#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:28:31 2021

@author: aditi
"""
#q15
import numpy as np

def QR(A):
    N = np.shape(A)[0]
    r = np.zeros((N,N))
    q = np.zeros((N,N))
    u = np.zeros(N)

    for i in range(N):
        sum = np.zeros(N)
        for j in range(i):
            r[j,i] = np.dot(q[:,j],A[:,i])
            sum = sum + r[j,i]*q[:,j]

        u = A[:,i] - sum
        r[i,i] = np.sqrt(np.dot(u,u))
        q[:,i] = u/r[i,i]

    return (q,r)

def offdiag_max(A):
    a = np.copy(A)
    minval = a.min()
    np.fill_diagonal(a,minval-1)
    return a.max()

def eigen_decomposition(A,eps):
    V = np.identity(np.shape(A)[0])
    while (offdiag_max(A)>=eps):
        Q,R = QR(A)
        A = R@Q
        V = Q@V

    return (A,V)

####################################################

A = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]])
Q,R = QR(A)
print('(Q15)\n(a)\nA =\n',A,'\n\nQR Decomposition gives:')
print('Q =\n',Q,'\n\nR =\n',R)

eps = 1e-6
D,V = eigen_decomposition(A,eps)
print('(b)\nEigen Values =',[D[i,i] for i in range(np.shape(A)[0])])
print('\n Corresponding Eigen Vectors =\n')

for i in range(np.shape(A)[0]):
    print(V[:,i])

###########################################################
