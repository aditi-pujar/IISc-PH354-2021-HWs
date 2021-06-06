#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:24:44 2021

@author: aditi
"""

import numpy as np

Vplus = 5
A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],dtype='float')
b = np.array([Vplus,0,Vplus,0])

x = np.linalg.solve(A,b)
q10_ans = np.array([3.,1.66666675,3.33333325,2.])
print('(Q12)')
print('A =\n',A,'\n\nb=',b)
print('Using numpy.linalg.solve :\n',x)
print('\nGaussian Elimination without Partial Pivoting:\n', q10_ans)
print('\nThus, both methods give the same solution.\n')

