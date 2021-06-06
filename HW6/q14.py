#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:10:04 2021

@author: aditi
"""

#q14
import numpy as np
import matplotlib.pyplot as plt


def newtonraphson_lin(F,J,x0):
    X0 = x0;
    invJ = np.linalg.inv(J)
    xnew = x0-invJ@F(x0,J,X0)

    #val = int((np.sum((xnew-x0)>=eps*np.ones(len(x0))))/len(x0))
    counter = 0
    while (abs(xnew[0]-x0[0])>0.0001)and(abs(xnew[1]-x0[1])>0.0001):
        x0 = xnew
        xnew = x0-invJ@F(x0,J,X0)
        counter+=1
    return xnew

def F(x,J,X0):
    val = J@x - X0
    return val


def backward_euler(A,x0,t):
    x0 = np.array(x0)
    t = np.array(t)

    x = np.zeros((len(t),np.size(x0)))
    x[0,:] = x0
    h = t[1]-t[0]
    J = np.identity(np.shape(A)[0]) - h*A
    
    for i in range(len(t)-1):
        x[i+1,:] = newtonraphson_lin(F,J,x[i,:])
    return np.array(x)


def forward_euler(A,x0,t):
    x0 = np.array(x0)
    t = np.array(t)

    x = np.zeros((len(t),np.size(x0)))
    x[0,:] = x0
    h = t[1]-t[0]

    for i in range(len(t)-1):
        x[i+1,:] = x[i,:] + h*A@x[i,:]
    return np.array(x)

##################################################

A = np.array([[998,1998],[-999,-1999]])
# J = lambda h: np.array([[1-998*h,-1998*h],[+998*h,1+1999*h]]) #this is Jacobian of the root finding function, F

X0 = np.array([1,0])

'''
Forward Euler method stable for h<= 2/(min|lambda|), where 
lambda are the eigen values. Here, 
lambda = -1, -1000
=> h_stable <= 2/1000

For h_stable = 0.001
h_stab/2 = 0.0005
10*h_stab = 0.01
'''

h1 = 0.0005; h2 = 0.01;

t1 = np.arange(0,1,h1)
t2 = np.arange(0,1,h2)

f_X1 = forward_euler(A,X0,t1)
f_X2 = forward_euler(A,X0,t2)

plt.figure()
plt.plot(t1,f_X1[:,0],t1,f_X1[:,1])
plt.legend(['u(t)','v(t)'])
plt.xlabel('t'); plt.ylabel('Function Values')
plt.title('(Q14) Forward Euler Method: h = 0.0005')
plt.savefig('Q14_FowardEuler_Stable.png')

plt.figure()
plt.plot(t2,f_X2[:,0],t2,f_X2[:,1])
plt.legend(['u(t)','v(t)'])
plt.xlabel('t'); plt.ylabel('Function Values')
plt.title('(Q14) Forward Euler Method: h = 0.01')
plt.savefig('Q14_FowardEuler_Unstable.png')

analytic_u = lambda t: 2*np.exp(-t)-np.exp(-1000*t)
analytic_v = lambda t: -np.exp(-t)+np.exp(-1000*t)

########################################################

b_X1 = backward_euler(A,X0,t1)
b_X2 = backward_euler(A,X0,t2)

plt.figure()
plt.plot(t1,b_X1[:,0],t1,b_X1[:,1])
plt.plot(t1,analytic_u(t1),'.',t1,analytic_v(t1),'.')
plt.legend(['u(t)','v(t)','an_u(t)','an_v(t)'])
plt.xlabel('t'); plt.ylabel('Function Values')
plt.title('(Q14) Backward Euler Method: h = 0.0005')
plt.savefig('Q14_BackwardEuler_h1.png')

plt.figure()
plt.plot(t2,b_X2[:,0],t2,b_X2[:,1])
plt.plot(t2,analytic_u(t2),'.',t2,analytic_v(t2),'.')
plt.legend(['u(t)','v(t)','an_u(t)','an_v(t)'])
plt.xlabel('t'); plt.ylabel('Function Values')
plt.title('(Q14) Backward Euler Method: h = 0.01')
plt.savefig('Q14_BackwardEuler_h2.png')

'''
The analytic solutions are almost completely
 coincident onto the solutions obtained by backwards 
 Euler method
 '''