#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:31:43 2021

@author: aditi
"""
#q13

import numpy as np
import matplotlib.pyplot as plt
import RK4

r'''
This code throws a lot of runtime errors due to overflow that
do not affect the output (as we only plot till \xi_star)
Thus, supressing warnings by un-commenting next 2 lines
may be desirable
'''

# import warnings
# warnings.filterwarnings("ignore")

def lane_emden(xi,X,n):
    xival = xi[0];
    theta = X[0]; m = X[1]
    dm_dxi = xival*xival*(theta**n)
    dtheta_dxi = -m*m/xival*xival
    return np.array([dtheta_dxi,dm_dxi])

n = 3
theta0 = np.arange(1,11)
eps = 1e-3
m0 = eps**3*theta0
t = np.linspace(eps,3,100)

soln = []; legend = [];


plt.figure()
for i in range(len(theta0)):
    X0 = np.array([theta0[i],m0[i]])
    X = RK4.RK4(lane_emden,X0,t,n)

    val = len(X[:,0][X[:,0]>=0])

    plt.plot(t[:val+1],X[:val+1,0])
    soln.append(X)
    legend.append(r'$\theta_0 =$%d'%X0[0])
plt.plot(t,np.zeros(len(t)),'--')
plt.title(r'(Q13) $\theta$ v/s $\xi$ for different $\theta_0$')
plt.xlabel(r'$\xi$'); plt.ylabel(r'$\theta(\xi)$')
plt.legend(legend)
plt.savefig('Q13a_shooting_by_hand.png')

'''
Guessing that for theta0 = 1.1, xi* = 2
'''

thetaval = 1.1; mval = eps**3*thetaval
X = RK4.RK4(lane_emden,np.array([thetaval,mval]),t,n)
val = len(X[:,0][X[:,0]>=0])

plt.figure()
plt.plot(t[:val+1],X[:val+1,0],t[:val+1],np.zeros(len(t[:val+1])))
plt.title(r'(Q13)  Shooting by Hand $\theta$ v/s $\xi$ for $\theta_0 =$ %f'%thetaval)
plt.xlabel(r'$\xi$'); plt.ylabel(r'$\theta(\xi)$')
plt.savefig('Q13_by_hand_theta0=1.1.png')

#automated shooting

def g(theta0):
    eps = 1e-3; n = 3;
    m0 = eps**3*theta0
    t = np.linspace(eps,3,100)
    X = RK4.RK4(lane_emden,np.array([theta0,m0]),t,n)

    res = len(X[:,0][X[:,0]>=0])
    xi_star = t[res]
    return xi_star - 2

def secant(f,x0,x1):
    tol = 1e-3
    while (abs(f(x1))>tol)and((f(x1)-f(x0))!=0):
        xnew = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
        x1 = xnew; x0 = x1;
    return x1

auto_theta = secant(g,1,1.3)

mval = eps**3*auto_theta
X = RK4.RK4(lane_emden,np.array([auto_theta,mval]),t,n)
val = len(X[:,0][X[:,0]>=0])

plt.figure()
plt.plot(t[:val+1],X[:val+1,0],t[:val+1],np.zeros(len(t[:val+1])))
plt.title(r'(Q13) Automated Shooting: $\theta$ v/s $\xi$ for $\theta_0 =$ %f'%auto_theta)
plt.xlabel(r'$\xi$'); plt.ylabel(r'$\theta(\xi)$')
plt.savefig('Q13_automated_theta0=%f.png'%auto_theta)

'''
The theta0 value given by automated shooting is
much more precise but otherwise similiar to the value
obtained when shooting by hand (~1.1)
'''