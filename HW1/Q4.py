#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:40:20 2021

@author: aditi
"""

#Q4 (As it was not specified, unit of time here = years.

import math
print('Exercise 4: Time Dilation in Relativistic Systems')
x=float(input('Enter distance of planet (in light-years units) >>'))
v=float(input('Enter relativistic speed of spaceship as a fraction of c >>'))

t = x/v; gamma_inv = math.sqrt(1-v*v); tbar = t*gamma_inv; 
print('For a spaceship travelling at',v,'times speed of light, c, to a planet',x,'light years away,\n\
      time taken to reach as seen by:')
#(a)
print('(a) Observer on Earth = ',t,'years.')
#(b)
print('(b) Passenger onboard spaceship = ',tbar,'years.')

###########################################################################
'''
For x = 10, v = 0.99:
    
For a spaceship travelling at 0.99 times speed of light, c, to a planet 10.0 light years away,
      time taken to reach as seen by:
(a) Observer on Earth =  10.1010101010101 years.
(b) Passenger onboard spaceship =  1.424922826228878 years.
'''
############################################################################
