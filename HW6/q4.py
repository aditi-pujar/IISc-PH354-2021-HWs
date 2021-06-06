#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 02:23:46 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def harmonic_oscillator(t,X,omega):
    x = X[0]; v = X[1];
    dxdt = v
    dvdt = -omega*omega*x
    return np.array([dxdt,dvdt])

t = np.linspace(0,50,1000)
omega = 1
#a
X0 = np.array([1,0])
X1 = RK4.RK4(harmonic_oscillator,X0,t,omega)

plt.figure()
plt.plot(t,X1[:,0])
plt.title('(Q4) Harmonic Oscillator: x v/s t (x0 = %d)'%X0[0])
plt.xlabel('t'); plt.ylabel('x')
plt.savefig('Q4(b)HO_x0=%d.png'%X0[0])

#b
X0 = np.array([2,0])
X2 = RK4.RK4(harmonic_oscillator,X0,t,omega)

plt.figure()
plt.plot(t,X2[:,0])
plt.title('(Q4) Harmonic Oscillator: x v/s t (x0 = %d)'%X0[0])
plt.xlabel('t'); plt.ylabel('x')
plt.savefig('Q4(b)HO_x0=%d.png'%X0[0])

#c

def anharmonic_oscillator(t,X,omega):
    x = X[0]; v = X[1];
    dxdt = v
    dvdt = -(omega**2)*(x**3)
    return np.array([dxdt,dvdt])

X0 = np.array([1,0])
X1 = RK4.RK4(anharmonic_oscillator,X0,t,omega)

plt.figure()
plt.plot(t,X1[:,0])
plt.title('(Q4) Anharmonic Oscillator: x v/s t (x0 = %d)'%X0[0])
plt.xlabel('t'); plt.ylabel('x')
plt.savefig('Q4(c)_1_(AHO_x0=%d).png'%X0[0])

X0 = np.array([2,0])
X2 = RK4.RK4(anharmonic_oscillator,X0,t,omega)

plt.figure()
plt.plot(t,X2[:,0])
plt.title('(Q4) Anharmonic Oscillator: x v/s t (x0 = %d)'%X0[0])
plt.xlabel('t'); plt.ylabel('x')
plt.savefig('Q4(b)_2_(AHO_x0=%d).png'%X0[0])

X0 = np.array([1/2,0])
X3 = RK4.RK4(anharmonic_oscillator,X0,t,omega)

plt.figure()
plt.plot(t,X3[:,0])
plt.title('(Q4) Anharmonic Oscillator: x v/s t (x0 = %.1f)'%X0[0])
plt.xlabel('t'); plt.ylabel('x')
plt.savefig('Q4(b)_3_(AHO_x0=%d).png'%X0[0])

#d

def vanderpol_oscillator(t,X,mu,w):
    x = X[0]; v = X[1];
    dxdt = v
    dvdt = mu*(1-x*x)*v -w*w*x
    return np.array([dxdt,dvdt])

t = np.linspace(0,20,10000)
w = 1
X0 = np.array([1,0])

mu = 1
X1 = RK4.RK4(vanderpol_oscillator,X0,t,mu,w)
plt.figure()
plt.plot(X1[:,0],X1[:,1])
plt.title('(Q4d) Van der Pol Phase Plot: v(t) v/s x(t) [mu = %.1f]'%mu)
plt.xlabel('x(t)'); plt.ylabel('v(t)')
plt.savefig('Q4(d)_1_mu=%.1f.png'%mu)

mu = 2
X2 = RK4.RK4(vanderpol_oscillator,X0,t,mu,w)
plt.figure()
plt.plot(X2[:,0],X2[:,1])
plt.title('(Q4d) Van der Pol Phase Plot: v(t) v/s x(t) [mu = %.1f]'%mu)
plt.xlabel('x(t)'); plt.ylabel('v(t)')
plt.savefig('Q4(d)_2_mu=%.1f.png'%mu)

mu = 4
X3 = RK4.RK4(vanderpol_oscillator,X0,t,mu,w)
plt.figure()
plt.plot(X3[:,0],X3[:,1])
plt.title('(Q4d) Van der Pol Phase Plot: v(t) v/s x(t) [mu = %.1f]'%mu)
plt.xlabel('x(t)'); plt.ylabel('v(t)')
plt.savefig('Q4(d)_3_mu=%.1f.png'%mu)

#################################################

