#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:40:04 2021

@author: aditi
"""
#Q4
import math
import numpy as np
print('Exercise 4: The diffraction limit of a Telescope:')
def f_J(m,x,theta):
    return math.cos(m*theta-x*math.sin(theta))

def J(m,x):
    if m%1==0 and m>-1 and x >= 0:
        a = 0; b = math.pi; N = 1000;
        #Simpson Rule integration
        I=0
        h=(b-a)/N
        for i in range(0,N,2):
            theta0 = a+i*h
            theta1 = theta0+h
            theta2 = theta1+h
            f0 = f_J(m,x,theta0)
            f1 = f_J(m,x,theta1)
            f2 = f_J(m,x,theta2)
            I+=f0+4*f1+f2
        I*=h/3
        
        Jmx = I/math.pi
        return Jmx
######################################################
#(a)
print('(a) Plotting Bessel functionc, J0(x), J1(x),J2(x):')
J0=[]; J1=[]; J2=[];
xval = np.linspace(0,20,100).tolist()
for x in xval:
    J0val=J(0,x); J0.append(J0val)
    J1val=J(1,x); J1.append(J1val)
    J2val=J(2,x); J2.append(J2val)
    
    
from matplotlib import pyplot as plt
plt.figure(1)
plt.plot(xval,J0,xval,J1,xval,J2)
plt.title('Q4(a) Bessel Functions: J0, J1 and J2')
plt.xlabel('x')
plt.ylabel('Jm(x)')
plt.legend(['J0','J1','J2'])

########################################################
########################################################

#(b) 500 nm = 0.5 micrometer
print('(b) Density plot of diffraction pattern of telescope:')
I=[];
k = 2*math.pi/0.5
for xval in np.linspace(-1,1,100):
    Ix=[]
    for yval in np.linspace(-1,1,100):
        rval = (xval**2+yval**2)**(1/2)
        Ival = (J(1,k*rval)/(k*rval))**2
        Ix.append(Ival)
    I.append(Ix)
Ivalues=np.array(I)

import seaborn as sns
plt.figure(2)
ax = plt.axes()
sns.heatmap(Ivalues)
ax.set_title(str('(Q4b)(i) Diffraction Pattern of a Telescope'))

plt.figure(3)
ax = plt.axes()
sns.heatmap(Ivalues,vmax=0.01)
ax.set_title(str('(Q4b)(ii) Diffraction Pattern of a Telescope\n\
Setting vmax = 0.01'))
