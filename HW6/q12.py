#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 09:36:00 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def threebodyproblem(t,X,M):
    x1,y1,x2,y2,x3,y3,vx1,vy1,vx2,vy2,vx3,vy3 = X.tolist()
    m1,m2,m3 = M
    xdot = X[6:]

    r1 = X[0:2]; r2 = X[2:4]; r3 = X[4:6];
    r12 = np.sqrt(np.sum((r1-r2)**2))
    r23 = np.sqrt(np.sum((r2-r3)**2))
    r31 = np.sqrt(np.sum((r3-r1)**2))

    a1 = m2*(r2-r1)/(r12**3) + m3*(r3-r1)/(r31**3)
    a2 = m3*(r3-r2)/(r23**3) + m1*(r1-r2)/(r12**3)
    a3 = m1*(r3-r1)/(r31**3) + m2*(r2-r3)/(r23**3)
    vdot = np.hstack((a1,a2,a3))
    return np.append(xdot,vdot)

M = [150,200,250]
X0= np.append(np.array([3,1,-1,-2,-1,1]),np.zeros(6))

delta = 1e-3
t = np.linspace(0,2,1000)

X,T = RK4.RK4_adaptive(threebodyproblem,X0,t,RK4.threebody_error,delta,M)

plt.figure()
plt.plot(X[:,0],X[:,1],X[:,2],X[:,3],X[:,4],X[:,5])
plt.title('(Q12) Star Trails: y(t) v/s x(t)')
plt.xlabel('x(t)'); plt.ylabel('y(t)');
plt.legend(['Star 1','Star 2','Star 3'])
plt.savefig('Q12.png')