#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:29:23 2021

@author: aditi
"""
##################################################################
#Q8
import math 
import time
start_time=time.time()
print('Exercise 8: the Madelung Constant')
L=int(input('Enter the number of cells in each direction, L >> '))
M=0.0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if (i==0) and (j==0) and (k==0):
                continue
            M+=(-1)**((i+j+k)%2)*1/math.sqrt(i**2+j**2+k**2)
            
print('For the given value of L ='+str(L)+'\nthe Madelung constant for Na\n=',M)
print('---',(time.time()-start_time),' seconds ---')

#################################################################
'''
The run time is also printed and for setting L = 175:
Result:
    
Enter the number of cells in each direction, L >> 175
For the given value of L =175
the Madelung constant for Na
= -1.7475645945934088
--- 66.05314540863037  seconds ---
'''
################################################################