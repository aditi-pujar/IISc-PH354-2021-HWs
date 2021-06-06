#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:35:19 2021

@author: aditi
"""

#Q2
#Q2 (a)
import math
from astropy.constants import G, M_earth, R_earth
Gval=G.value; Me_val=M_earth.value; Re_val=R_earth.value;

print('Exercise 2: Altitude of a satellite')
T = float(input('Enter desired time period in seconds >> '))
#T=inputval*u.second
h = ( (math.sqrt(Gval*Me_val))*T/(2*math.pi))**(2/3)-Re_val

if h > 0:
    print('Required altitude of satellite, with time period',T,'seconds is', h,'m.' )
else:
    print('The given time period',T,'seconds is too small, leading to absurd values of altitude.')

#######################################################################
#Q2 (b)
'''
(1) "Geosynchronous orbit" satellite: frequency = 1/day
    T1 = 24*3600 seconds = 86400 s
    Substituting gives 
    h(T1) = 35862994.19769288 m.
    
(2) Frequency = 1/90 minutes
    T2 = 90*60 seconds = 5400 s
    Substituting gives
    h(T2) = 274455.46878318116 m.
    
(3) Frequency = 1/45 minutes
    T3 = 45*60 seconds = 2700 s
    Substituting gives:
    
"The given time period 2700.0 seconds is too small, leading to absurd values of altitude."

Therefore, for a satellite to orbit the earth once every 45 minutes \
is impossible - the value of altitude obtained in above calculation \
    h(T3) < 0
    
########################################################################
#Q2 (c)
If frequency = 1/sidereal day (= 1/23.93 hours):
    T' = 23.93*3600 seconds = 86148.0 s
    
    h(T') = 35780818.75794734 m.
    h(T1) = 35862994.19769288 m.
    
We can see that for satellite to orbit every sidereal day, it needs \
to be slightly lower in altitude, closer to earth, so:
    h(T1) - h(T') = 82175.43974553794 m
    A difference of ~ 82.2 km

Sidereal time period of orbit is truly geosynchronous as it
is the time taken to complete a rotation with respect to
stars further away than the sun (with which we measure the solar day)
- a true rest frame.

'''
#############################################################8