#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:11:58 2021

@author: aditi
"""

#Q14
print('Exercise 14: Gravitational Pull of Uniform Sheet ')

from gaussxw import gaussxwab
from scipy.constants import G
from numpy import linspace
import sympy
#(b)
def Fz(z):
    y = sympy.symbols('y')
    L = 10
    a = -L/2
    b = L/2
    N = 100
    
    pts,w=gaussxwab(N,a,b)
    Fx=0
    for i in range(N):
        xval=pts[i]
        Fx+= w[i]/((xval**2+z**2+y**2)**(3/2))
    
    I = 0
    for j in range(N):
        yval=pts[i]
        Fyval=float(Fx.subs(y,yval))
        I+=Fyval

    k = G*(10*1000)/(L*L)
    F = k*z*I
    return F

####################################################
zval = linspace(0,10,10)
Fzval=[]
for z in zval:
    Fzval.append(Fz(z))

from matplotlib import pyplot as plt
plt.figure()
plt.plot(zval,(Fzval))
plt.title('(Q14) Gravitational along Z axis at distance z')
plt.xlabel('z Distance (m)')
plt.ylabel('Fz (N)')