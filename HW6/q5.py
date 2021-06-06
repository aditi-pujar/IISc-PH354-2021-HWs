#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 02:32:45 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def projectile(t,X,R,p,C,m):
    #x = X[0]; y = X[1]; 
    vx = X[2]; vy = X[3];

    dxdt = vx; dydt = vy;

    k = -(np.pi*(R**2)*p*C/(2*m))*np.sqrt(vx*vx+vy*vy)
    dvxdt = k*vx
    dvydt = -9.80665 +k*vy
    return np.array([dxdt,dydt,dvxdt,dvydt])

R,p,C,m = 0.08,1.22,0.47,1

'''
Exact way to solve for trajectory would be to
keep solving for solution until 
y = 0 => ball has hit the ground.

Approximate way can be to set upper limit of time interval as
T = 4vy0/g
(Time of Flight not considering air resistance).

We expect this time of flight to be
 necessarily lesser than T
'''

x0 = 0; y0 = 0;
vx0 = 100*np.cos(np.pi/6)
vy0 = 100*np.sin(np.pi/6)
X0 = np.array([x0,y0,vx0,vy0])

T = 4*vy0/(9.80665)
t = np.linspace(0,T,1000)

X = RK4.RK4(projectile,X0,t,R,p,C,m)

plt.figure()
plt.plot(X[:,0],X[:,1])
plt.title('(Q5) Full Solution for Trajectory (m = 1)')
plt.plot(np.zeros(int(X[-1,0])+1))
plt.xlabel('x(t) (m)'); plt.ylabel('y(t) (m)')
plt.savefig('Q5_(i).png')

'''
To plot trajectory, we need to truncate before y(t*) < 0
'''
yt = X[:,1]
val = np.size([yt[yt>=0]]) + 1

plt.figure()
plt.plot(X[:val,0],X[:val,1])
plt.plot(np.zeros(int(X[val,0])+1))
plt.title('(Q5) Trajectory of Projectile: y(t) v/s x(t)')
plt.xlabel('x(t) (metre)'); plt.ylabel('y(t) (metre)')
plt.savefig('Q5_(ii).png')

m = 2
X2 = RK4.RK4(projectile,X0,t,R,p,C,m)
val2 = np.size([X2[:,1][X2[:,1]>=0]]) + 1

m = 3
X3 = RK4.RK4(projectile,X0,t,R,p,C,m)
val3 = np.size([X3[:,1][X3[:,1]>=0]]) + 1

m = 4
X4 = RK4.RK4(projectile,X0,t,R,p,C,m)
val4 = np.size([X4[:,1][X4[:,1]>=0]]) + 1

m = 5
X5 = RK4.RK4(projectile,X0,t,R,p,C,m)
val5 = np.size([X5[:,1][X5[:,1]>=0]]) + 1

plt.figure()
plt.plot(X[:val,0],X[:val,1])
plt.plot(X2[:val2,0],X2[:val2,1])
plt.plot(X3[:val3,0],X2[:val3,1])
plt.plot(X4[:val4,0],X4[:val4,1])
plt.plot(X5[:val5,0],X5[:val5,1])
plt.title('(Q5) Trajectories for differemt masses')
plt.xlabel('x(t) (metre)'); plt.ylabel('y(t) (metre)')
plt.legend(['m=1','m=2','m=3','m=4','m=5'])
plt.savefig('Q5_(iii).png')

plt.figure()
plt.plot(range(1,6),[X[val-1][0],X2[val2-1][0],X3[val3-1][0],X4[val4-1][0],X5[val5-1][0]])
plt.title('(Q5) Range of Projectiles v/s Mass')
plt.xlabel('m (kg)'); plt.ylabel('R(m) (metre)')
plt.savefig('Q5_(iv).png')
