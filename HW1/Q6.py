#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:19:09 2021

@author: aditi
"""

#Q6
print('Exercise 6: Planetary orbits')
l1=float(input('Enter distance between planet and Sun at perihelion (l1) (in metres) >> '))
v1=float(input('Enter linear velocity at perihelion (v1) (in metres per second) >> '))

from astropy.constants import G, M_sun
Gval=G.value; Ms_val=M_sun.value;

a=1/( (2/l1)-v1**2/(Gval*Ms_val))
e=1-l1/a
l2=a*(1+e)
v2=((1-e)/(1+e))*v1
AU= 1.495978707*10**11
a_AU=(a/AU)
T=(a_AU)**(3/2) #years

print('For\nPerihelion distance l1 =',l1,'m\nPerihelion velocity v1 =',v1,'m/s')
print('\nAphelion distance l2 =', l2,'m')
print('\nAphelion velocity v2 =', v2,'m/s')
print('\nOrbital period T =', T,'years')
print('\nOrbital eccentricity e =', e,'\n***')

#############################################################
'''
Verifying for
1. Earth:
For
Perihelion distance l1 = 147100000000.0 m
Perihelion velocity v1 = 30287.0 m/s

Aphelion distance l2 = 152111350728.5926 m

Aphelion velocity v2 = 29289.18636683006 m/s

Orbital period T = 1.0000782574583424 years

Orbital eccentricity e = 0.016748531485820117 

2. Halleys comet:
For
Perihelion distance l1 = 87830000000.0 m
Perihelion velocity v1 = 54529.0 m/s

Aphelion distance l2 = 5371566481143.354 m

Aphelion velocity v2 = 891.5987704541246 m/s

Orbital period T = 77.94420677574567 years

Orbital eccentricity e = 0.9678242822981027 

    
'''