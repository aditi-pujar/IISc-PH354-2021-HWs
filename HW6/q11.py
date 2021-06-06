#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:50:47 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

'''
This does not seem to work and may only be considered an an attempt
'''

UNIT_E = 1.6e-19 #J
UNIT_L = 1e-11 #m
UNIT_t = 1 #s

UNIT_m = UNIT_E*UNIT_t**2/(UNIT_L**2)

V0 = 50 #units
a = 1 #units
x = np.linspace(-10,10,1000) #x in units

hbar = 1.0545718e-34 #Js
m = 9.10938356e-31 #kg

k = hbar**2/2*m #Jm^2
k = k/(UNIT_E*UNIT_L**2) #units

def f(x,PSI,V,E):
    dpsi_dx = PSI[1]
    d2psi_dx2 = (V(x[0])-E)*PSI[0]/k
    return np.array([dpsi_dx,d2psi_dx2])

def eigenstate(E0,V):
    E1 = E0; delE = 0.1*E0; E2 = E0 + delE; 

    PSI_0 = np.array([0.001,0])
    #psi_1 = RK4.RK4(f,PSI_0,x,V,E1)
    psi_2 = RK4.RK4(f,PSI_0,x,V,E2)

    while (abs(E2-E1)/E1)>=1e-3:
        psi_1 = np.copy(psi_2)
        E1 = E2
        E2 = E1 + delE
        psi_2 = RK4.RK4(f,PSI_0,x,V,E2)
        val1 = psi_1[0,-1];val2 = psi_2[0,-1];

        if (val1*val2 < 0):
            delE = delE/2
        if np.abs(val2)>np.abs(val1):
            delE = -delE
    return E1, psi_1

def first_n_states(n,V,E_ground):
    Evals = [];
    PSI = [];

    E0, psi0 = eigenstate(E_ground,V); i = 1;
    Evals.append(E0); PSI.append(psi0)

    Eold = E0; Enew = E0; fac = 0.5;

    while (i<n):
        Eold = Enew
        Enew_guess = Eold+fac*V0
        Enew, psi_new = eigenstate(Enew_guess,V)
        if (Enew != Eold):
            i+=1
            Evals.append(Enew); PSI.append(psi_new)
        fac += 0.5
    return Evals, PSI
######################################################

#a
def V_harmonic(x):
    return V0*x*x

# E_ground = 100 #units
# E_h, psi_h = first_n_states(3,V_harmonic,E_ground)

#b
def V_anharmonic(x):
    return V0*x**4

