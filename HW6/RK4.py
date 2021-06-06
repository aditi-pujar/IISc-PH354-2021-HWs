#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 01:27:50 2021

@author: aditi
"""

import numpy as np
import matplotlib.pyplot as plt

def RK4(f,x0,t,*args):
    x0 = np.array(x0)
    t = np.array(t)
    x = np.zeros((len(t),np.size(x0)))
    x[0,:] = x0
    h = t[1]-t[0]

    for i in range(len(t)-1):
        xval = x[i,:]
        tval = t[i]*np.ones(np.size(x0))

        k1 = f(tval,xval,*args)
        k2 = f(tval+h/2,xval+h*k1/2,*args)
        k3 = f(tval+h/2,xval+h*k2/2,*args)
        k4 = f(tval+h,xval+h*k3,*args)

        x[i+1,:] = x[i,:] + (h/6)*(k1+2*(k2+k3)+k4)
    return np.array(x)

#######################################################
def euclidean_error(x1,x2):
    e = abs(x1-x2)/30
    error = np.sqrt(e[0]**2+e[1]**2)
    return error

def threebody_error(x1,x2):
    e1 = euclidean_error(x1[0:2],x2[0:2])
    e2 = euclidean_error(x1[2:4],x2[2:4])
    e3 = euclidean_error(x1[4:6],x2[4:6])
    return e1+e2+e3

def RK4_adaptive(f,x0,t,error,delta,*args):
    x0 = np.array(x0)
    t = np.array(t)
    
    # x = np.zeros((len(t),np.size(x0)))
    # x[0,:] = x0

    h = t[1]-t[0]
    TMAX = t[-1]

    tval=[]; xval = [];
    tval.append(t[0]); xval.append(x0);
    i = 0

    while (tval[i] <= TMAX):
        x1 = RK4(f,xval[i],[tval[i],tval[i]+h,tval[i]+2*h],*args)[-1,:]
        x2 = RK4(f,xval[i],[tval[i],tval[i]+2*h],*args)[-1,:]

        e = error(x1,x2)
        rho = (h*delta/e)**(1/4)

        if rho < 1:
            h = h*rho
        else:
            h = h*min(rho,2)
            xval.append(np.array(x1))
            tval.append(tval[i]+2*h)
            i += 1
    return np.array(xval), np.array(tval)


