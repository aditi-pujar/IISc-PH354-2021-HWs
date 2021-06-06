
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:32:15 2021

@author: aditi
"""

#Q 14
import math
import numpy as np
from matplotlib import pyplot as plt

print('Exercise 14: Curve plotting')
thetaval = np.linspace(0,2*math.pi, num=100)
xval=[];yval=[];
#(a)
print('(a) Parametric Plotting of Deltoid Curve:')
for theta in thetaval:
    xn=2*math.cos(theta) + math.cos(2*theta)
    yn=2*math.sin(theta) - math.sin(2*theta)
    xval.append(xn)
    yval.append(yn)

plt.figure(1)
plt.plot(xval,yval)
plt.xlabel('X-Axis'); plt.ylabel('Y-Axis')
plt.title('(Q14a) Parameteric Deltoid Curve Plotting\nx=2cosθ+cos2θ\
\ny=2sinθ-sin2θ')

###############################################
#(b)
print('(b) Radial plot of Galilean Sprial:\nr=θ^2')
thetaval = np.linspace(0,10*math.pi, num=10000)
xval=[]; yval=[];
for theta in thetaval:
     r=theta**2
     xn=r*math.cos(theta); xval.append(xn)
     yn=r*math.sin(theta); yval.append(yn)

plt.figure(2)
plt.plot(xval,yval)
plt.xlabel('X-Axis'); plt.ylabel('Y-Axis')
plt.title('(Q14b) Radial Plot\nr = θ^2\
\nGalilean Spiral')

#(c)
print('(c) Radial plot of Feys Function:\n\
r=θ^2')
thetaval = np.linspace(0,24*math.pi, num=100000)
xval=[]; yval=[];
for theta in thetaval:
     r=math.exp(math.cos(theta))-2*math.cos(4*theta)+(math.sin(theta/12))**5
     xn=r*math.cos(theta); xval.append(xn)
     yn=r*math.sin(theta); yval.append(yn)

plt.figure(3)
plt.plot(xval,yval)
plt.xlabel('X-Axis'); plt.ylabel('Y-Axis')
plt.title('(Q14c) Radial Plot\nFeys Function')

###############################################