#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:09:11 2021

@author: aditi
"""

#Q1
print('Exercise 1: Plotting v(t) and x(t):')
t=[]; xv=[]; x=[]; I=0;i=0;
with open('velocities.txt') as f:
    for line in f:
        l1=line.index('\t')
        l2=line.index('\n')
        tval=float(line[0:l1])
        t.append(tval)
        xvval=float(line[l1+1:l2])
        xv.append(xvval)
        if i==0 :
            xvval_prev=0; tval_prev=0;
        else:
            xvval_prev=xv[i-1]; tval_prev=t[i-1];
        I+=1/2*(tval-tval_prev)*(xvval_prev+xvval)
        x.append(I)
        i+=1

from matplotlib import pyplot as plt
plt.figure(1)
plt.plot(t,xv,t,x)
plt.title('(Q1) Velocity and Distance Travelled')
plt.xlabel('t')
plt.ylabel('v(t) or x(t)')
plt.legend(['v','distance travelled'])
