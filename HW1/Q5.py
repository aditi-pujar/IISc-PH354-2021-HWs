#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:07:03 2021

@author: aditi
"""

#Q5
print('Exercise 5: Quantum potential step')
import math

#Given
E = 10 #eV
V = 9 #eV
m = 9.11*10**-31 #kg
'''
Actually calculating could lead to loss of precision.
We are only interested in ratios, so:
'''
k1 = math.sqrt(E)
k2 = math.sqrt(E-V)
eps = k2/k1

T = 4*eps/((1+eps)**2)
R = ((1-eps)/(1+eps))**2
print('When an electron with energy, E =',E,'eV encounters\
 a potential step of V =',V,'eV:\n')
print('Transmission probability |T|^2 =',T)
print('Reflection probability |R|^2 =',R)