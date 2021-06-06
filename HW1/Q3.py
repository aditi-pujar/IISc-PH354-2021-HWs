#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:39:02 2021

@author: aditi
"""

#Q3 

import math
print('Exercise 3: Cartesian to Radial Coordinates {θ ∈ [0,2π)}  ')
x=float(input('Enter x-coordinate >>'))
y=float(input('Enter y-coordinate >>'))

r = math.sqrt(x*x+y*y)
if r==0:
    print('As r = ',r,'\ni.e. the point (',x,',',y,') is the origin\n theta is not defined')
else:
    if x>=0 and y>=0:
        theta = math.degrees(math.atan(y/x))
    elif x>=0 and y<=0:
        theta = math.degrees(2*math.pi+math.atan(y/x))
    elif x<=0 and y<=0:
        theta = math.degrees(math.pi+math.atan(y/x))
    else:
        theta = math.degrees(math.acos(x/r))
    print('Given Cartesian coordinates (x,y) = (',x,',',y,') -> \nRadial coordinates (in degrees) (r,θ) = (',r,',',theta,')')


##########################################################################
