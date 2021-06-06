#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:07:17 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt

def verlet(f,X0,t,*args):
    mid = int(np.size(X0)/2)
    x = np.zeros((len(t),mid))
    v = np.zeros((len(t),mid))
    x[0,:] = X0[:mid]; v[0,:] = X0[mid:]

    h = t[1]-t[0]
    vhalf = v[0,:] + (h/2)*f(t[0],x[0,:],*args)

    for i in range(len(t)-1):
        x[i+1,:] = x[i,:] + h*vhalf
        k = h*f(t[i+1],x[i+1,:])
        v[i+1,:] = vhalf + k/2
        vhalf += k
    return x, v

def earth_orbit(t,X):
    r = np.sqrt(np.sum(X*X))
    G = 6.6738e-11
    M = 1.9891e30
    k = -G*M/r**3
    return k*X

#####################################################

G = 6.6738e-11
M = 1.9891e30
TMAX = 5*365.25*24*3600
h = 3600 #seconds

t = np.linspace(0,TMAX+h,h)
X0 = np.array([1.471e11,0,0,3.0287e4])

X,V = verlet(earth_orbit,X0,t)

plt.figure(figsize=[5,5])
plt.scatter(X[:,0],X[:,1],s=1,c=t)
plt.title('(Q10a) Orbit of Earth: (coloring shows time passage)')
plt.xlabel('x(t)'); plt.ylabel('y(t)')
plt.savefig('Q10a_Orbit.png')

m = 5.9722e24
r = np.sqrt(np.sum(X*X,axis=1))

PE = -G*M*m/r
KE = m*np.sum(V*V,axis=1)/2
TE = PE+KE

plt.figure()
plt.plot(t,PE,t,KE,t,TE)
plt.title('(Q10b) KE, PE and TE over time')
plt.xlabel('t (s)'); plt.ylabel('Energies (J)');
plt.legend(['Potential Energy','Kinetic Energy','Total Energy'])
plt.savefig('Q10b_All_Energies.png')

plt.figure()
plt.plot(t,TE)
plt.plot(t,TE[0]*np.ones(len(t)))
plt.title('(Q10c) Total Energy over Time')
plt.xlabel('t (s)'); plt.ylabel('Total Energy (J)')
plt.legend(['TE(t)','TE(0)'])
plt.savefig('Q10c_Total_Energy.png')