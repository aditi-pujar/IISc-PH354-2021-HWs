#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:55:43 2021

@author: aditi
"""

#Q18
print('Exercise 18: Least squares fitting and the photoelectric effect')

from matplotlib import pyplot as plt
import numpy as np

x=[]; y=[];
with open('millikan.txt') as f:
    N=0; Ex=0; Ey=0; Exx=0; Exy=0;
    for line in f:
        l1=line.index(' ')
        l2=line.index('\n')
        xval=float(line[0:l1])
        x.append(xval)
        yval=float(line[l1+1:l2])
        y.append(yval)
        Ex+=xval; Exx+=xval**2; Ey+=yval; Exy+=xval*yval;
        N+=1

Ex/=N; Exx/=N; Ey/=N; Exy/=N;
m = (Exy-Ex*Ey)/(Exx-Ex**2)
c = (Exx*Ey-Ex*Exy)/(Exx-Ex**2)

xval = np.linspace(0,1.2e15)
tmp = []
for xx in xval:
    yvalue=m*xx+c
    tmp.append(yvalue)
yval = np.array(tmp)

##############################################################
#(a)
print('(Q18a) Plot of data points:\n')
plt.figure(1)
plt.scatter(x,y)
plt.title('(Q18a) Data from millikan.txt')
plt.xlabel('x axis')
plt.ylabel('y-axis')

#(b)
print('(Q18b) Using least squares method, the best linear fit obtained is\n\
y = m*x + c, where\nm =',m,'\nc =',c,'\ni.e.')
print('y = ',m,'*x + ',c)

#(c)
print('\n(Q18c) Plot of data points with linear fit:')
plt.figure(2)
plt.scatter(x,y)
plt.plot(xval,yval)
plt.title('(Q18c) Data from millikan.txt with linear fit')
plt.xlabel('x axis')
plt.ylabel('y-axis')

#(d)
from scipy.constants import e,h
h_expt = m*e
err = abs(h-h_expt)/h*100
print('\n(Q18d) We now know the slope, m =(',m,') is actually (h/e)\n\
Given e =',e,'Coulombs\nTherefore, experimentally obtained Plancks constant (h)')
print('=',h_expt)
print('\nLiterature value h =',h)
print('% error =', err,'%')

#################################################################################


