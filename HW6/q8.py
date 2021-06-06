#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:57:40 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4
import timeit

def comet_orbit(t,X,M,G):
    x = X[0]; y = X[1];
    vx = X[2]; vy = X[3];

    dxdt = vx; dydt = vy;

    k = G*M/(np.power((x*x+y*y),3/2))
    dvxdt = -k*x; dvydt = -k*y;
    return np.array([dxdt,dydt,dvxdt,dvydt])

from scipy.constants import G
M = 1.989e30

X0 = np.array([4e12,0,0,500])
'''
Neptune Orbital Period = 165 years
'''
TMAX = (2*165*366*24*3600)*2/5
t = np.arange(0,TMAX,1e3)

start_time = timeit.default_timer()
X = RK4.RK4(comet_orbit,X0,t,M,G)
end_time = timeit.default_timer()
t1 = end_time-start_time

plt.figure()
plt.plot(X[:,0],X[:,1])
plt.title('(Q8a) Comet Orbit (Fixed Step Size RK4)')
plt.xlabel('x(t)'); plt.ylabel('y(t)')
plt.savefig('Q8_Fixed_Step_Size_RK4.png')

print('\n(Q8)\nTime taken for fixed step size RK4 method =', end_time-start_time,'seconds.')

################################################################################
#t = np.arange(0,TMAX,1e4)
delta = 1e3/31556952 #second inverse

start_time = timeit.default_timer()
Xadapt,Tadapt = RK4.RK4_adaptive(comet_orbit,X0,t,RK4.euclidean_error,delta,M,G)
end_time = timeit.default_timer()
t2 = end_time-start_time

plt.figure()
plt.plot(Xadapt[:,0],Xadapt[:,1])
plt.title('(Q8b) Comet Orbit (Adaptive Step Size RK4)')
plt.xlabel('x(t)'); plt.ylabel('y(t)')
plt.savefig('Q8_Adaptive_Step_Size_RK4.png')

half_index = int(len(Tadapt)/2)

plt.figure()
plt.scatter(Xadapt[:half_index,0], Xadapt[:half_index,1], s=1, c = Tadapt[:half_index])
plt.title('(Q8c) Scatter of Solution Points (Adaptive RK4)')
plt.xlabel('x(t)'); plt.ylabel('y(t)')
plt.savefig('Q8_Step_Size_Sapcing_AdaptiveRK4.png')

print('\nTime taken for adaptive step size RK4 method =', end_time-start_time,'seconds.')

'''
(b) For fixed step RK4:
Smaller step sizes led to the orbits being more coincident while
larger values meant subsequent orbits were not so.

Step size taken =  1000.0 seconds

(c)
(Fixed step RK4 takes ~4 minutes to run):
Time taken for fixed step size RK4 method = 270.1885413660202 seconds.
Time taken for adaptive step size RK4 method = 0.5578119830170181 seconds.
'''