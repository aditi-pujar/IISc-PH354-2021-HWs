#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:59:05 2021

@author: aditi
"""
from gaussxw import gaussxwab
from scipy import constants
def phi_pt(x0,y0):
    k = 1/(4*math.pi*constants.epsilon0)*1
    vplus = 1/(math.sqrt((x0-5)*(x0-5) + y0*y0))
    vminus = -1/(math.sqrt((x0+5)*(x0+5) + y0*y0))
    v = k*(vplus+vminus)
    return v

####################################################
def pd(potential):
    x = np.linspace(-500,500,1001)
    y = np.linspace(-500,500,1001)
    h=1
    FDX=[]; FDY=[];
    
    for xval in x:
        Fdx=[]; Fdy=[];
        for yval in y:
            fdx=math.nan; fdy=math.nan;
            if isnan(potential(xval,yval)):
                continue
            if isnan(potential(xval+1,yval) or xval == 500:
                fdx = (potential(xval,yval)-potential(xval-1,yval))
            if isnan(potential(xval,yval+1) or yval == 500:
                fdy = (potential(xval,yval)-potential(xval,yval-1))
    
            if isnan(fdx):
                fdx = potential(xval+1,yval)-potential(xval,yval)
            if isnan(fdy):
                fdy = potential(xval,yval+1)-potential(xval,yval)
            Fdx.append(fdx); Fdy.append(fdy);
        FDX.append(Fdx); FDY.append(Fdy);
    
    return FDX, FDY
########################################################
###############################################################
def sigma(x,y):
    q0=100/(100*100) #C/cm^2
    L=10 #cm
    val = q0*math.sin(2*math.pi*x/L)*math.sin(2*math.pi*y/L)
    return val

def phi_sheet_val(x,y,x0,y0):
    return sigma(x,y)/(math.sqrt((x-x0)**2+(y-y0)**2))

def phi_sheet_integrand(y,x0,y0):
    L = 10
    a = -L/2
    b = L/2-1
    N = 100
    pts,w=gaussxwab(N,a,b)
    val=0
    for i in range(N):
        xval=pts[i]
        ival=w[i]*phi_sheet_val(xval,y,x0,y0)
        val+=ival
    return val

def phi_sheet(x0,y0):
    k = 1/(4*math.pi*constants.epsilon0)
    L = 10
    a = -L/2
    b = L/2-1
    N = 100
    pts,w=gaussxwab(N,a,b)
    I=0
    for i in range(N):
        yval=pts[i]
        ival=w[i]*(phi_sheet_integrand(yval,x0,y0))
        I+=ival
    phival = k*I
    return phival
###########################################################
