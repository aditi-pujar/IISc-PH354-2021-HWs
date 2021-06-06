#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 00:34:23 2021

@author: aditi
"""
#q13

import numpy as np
import cmath

R1,R3,R5,R2,R4,R6 = 1e3,1e3,1e3,2e3,2e3,2e3
C1 = 1e-6; C2 = 0.5e-6
xplus = 3
w = 1e3

a11 = complex(1/R1+1/R4,w*C1)
a12 = complex(0,-w*C1)

a21 = complex(0,-w*C1)
a22 = complex(1/R2+1/R5,w*(C1+C2))
a23 = complex(0,-w*C2)

a32 = complex(0,-w*C2)
a33 = complex(1/R3+1/R6,w*C2)

A = np.array([[a11,a12,0],[a21,a22,a23],[0,a32,a33]])
b = xplus*np.array([1/R1,1/R2,1/R3])

X = np.linalg.solve(A,b)

print('(Q13)\nV\tAmplitude (V)\tPhase (rad)\n')
for i in range(len(b)):
    val = cmath.polar(X[i])
    print('V%d\t%f\t\t\t%f'%(i+1,val[0],val[1]))