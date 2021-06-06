#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 03:55:15 2021

@author: aditi
"""

#Q13
print('Exercise 13: Plotting experimental data')
import matplotlib.pyplot as plt

t=[]; sunspot=[];
########################################################
#(a)

with open('sunspots.txt') as f:
    for line in f:
        l1=line.index('\t')
        l2=line.index('\n')
        tval=int(line[0:l1])
        t.append(tval)
        sunspotval=float(line[l1+1:l2])
        sunspot.append(sunspotval)
print('(a) Plotting all the data points over all times:')
plt.figure()
plt.plot(t,sunspot)
plt.xlabel('Time (t) (in months)')
plt.ylabel('No. of sunspots seen')
plt.title('(Q12a) No of Sunspots v/s time (for all t)')
plt.show 

del t, sunspot, tval, sunspotval
########################################################
#(b)
t=[]; sunspot=[];
with open('sunspots.txt') as f:
    for i in range(0,1000):
        string=f.readline()
        l1=string.index('\t')
        l2=string.index('\n')
        tval=int(string[0:l1])
        t.append(tval)
        sunspotval=float(string[l1+1:l2])
        sunspot.append(sunspotval)
print('(b) Plotting over first 1000 data points only')
plt.figure()
plt.plot(t,sunspot)
plt.xlabel('(Q12b) Time (t) (in months)')
plt.ylabel('No. of sunspots seen')
plt.title('No of Sunspots v/s time (for first 1000 data points only)')
plt.show 

##############################################################
#(c)
'''for kth value in an array, takes the running average over all 
available values with index [k-r,k+r]
'''
def running_avg(x,r):
    y=[]
    for k in range(0,len(x)):
        val=0; no_r=0;
        for kr in range(-r,r):
            index=k+kr
            if index<0 or index>=len(x):
                pass
            else:
                val+=x[index]
                no_r=no_r+1;
        yk=val/(no_r-1)
        y.append(yk)
    return y

avg_sunspot = running_avg(sunspot,5)
print('(c) Plotting observations as well as \
their running average (over +- 5 observations) for 1000 data points:')
plt.figure()
plt.plot(t,sunspot,label='Observations')
plt.plot(t,avg_sunspot,label='Running Average over r=5')
plt.xlabel('Time (t) (in months)')
plt.ylabel('No. of sunspots seen')
plt.title('(Q12c) No of Sunspots v/s time (for first 1000 data points only)')
plt.legend()
plt.show 

