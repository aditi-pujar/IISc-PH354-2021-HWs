#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:08:04 2021

@author: aditi
"""

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

'''
Energy scale = eV
Length Scale = Angstrom
Time scale = 1s
'''

#e = 1.6022e-19
UNIT_E = 1.6022e-19 
UNIT_L = 1e-10

L = 5 #A
a = 10 #eV

mval = 9.1094e-31 #kg
hbar = 1.054571817e-34

k_SIunits = hbar**2/(2*mval) #dimensions =[Energy*L^2]
k = k_SIunits/(UNIT_E*UNIT_L**2)

# Now, L, a, k are in required units

def H(m,n):
    if m==n:
        return k*(n*np.pi/L)**2 + a/2
    elif (m+n)%2 != 0:
        return -8*m*n*a/(np.pi**2*((m*m-n*n)**2))
    else:
        return 0

def Hamiltonian_Matrix(N):
    Hmatrix = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            Hmatrix[i,j] = H(i+1,j+1)

    return Hmatrix

#####################################################
print('Q16:')
N = 10
Hmat = Hamiltonian_Matrix(N)
evals10 = scipy.linalg.eigh(Hmat,eigvals_only=True)
print('For size of H matrix =',N,'x',N)
print('First 10 eigen values =\n',evals10)

N = 100
Hmat = Hamiltonian_Matrix(N)
evals10 = scipy.linalg.eigh(Hmat,eigvals=(0,9),eigvals_only=True)
print('\n\nFor size of H matrix =',N,'x',N)
print('First 10 eigen values =\n',evals10)

evals3, evectors3 = scipy.linalg.eigh(Hmat,eigvals=(0,2))

x = np.linspace(0,L,1000)
n = np.arange(1,101,1)*np.pi/L
basis_fn = lambda xval: np.sin(n*xval)

PSI = []
for xval in x:
    basis_fnval = basis_fn(xval)
    psi0 = np.dot(evectors3[:,0],basis_fnval)
    psi1 = np.dot(evectors3[:,1],basis_fnval)
    psi2 = np.dot(evectors3[:,2],basis_fnval)
    PSI.append([psi0,psi1,psi2])

PSI = np.array(PSI)
density = PSI*np.conjugate(PSI)

plt.figure()
plt.plot(x,density[:,0],x,density[:,1],x,density[:,2])
#plt.legend([r'\psi_0',r'\psi_1',r'\psi_3'])
plt.legend(['GS','1st ES','2nd ES'])
plt.title(r'(Q16) $|\psi(x)|^2$ v/s x')
plt.xlabel('x'); plt.ylabel(r'$|\psi(x)|^2$ (Unnormalised)')
plt.savefig('Q16_Not_Normalised.png')

'''
It is not normalised as 
the basis functions (sin(n*pi/L)) are not normalised.
We can see from both, the basis functions and
the calculation of H:
that L/2 is the correct normalisation factor
'''

density = density/(L/2)
plt.figure()
plt.plot(x,density[:,0],x,density[:,1],x,density[:,2])
#plt.legend([r'\psi_0',r'\psi_1',r'\psi_3'])
plt.legend(['GS','1st ES','2nd ES'])
plt.title(r'(Q16) $|\psi(x)|^2$ v/s x')
plt.xlabel('x'); plt.ylabel(r'$|\psi(x)|^2$ (Normalised)')
plt.savefig('Q16_Normalised.png')

area_trapezoidal = (x[1]-x[0])*np.sum(2*density,axis=0)/2
print('\n\nAreas under normalised wave functions =', area_trapezoidal)