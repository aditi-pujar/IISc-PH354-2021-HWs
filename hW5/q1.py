#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:20:17 2021

@author: aditi
"""

#1
import random as rd
import numpy as np
print('(a) To simulate the rolling of 2 die:')
print('Dice 1:', rd.randint(1,6))
print('Dice 2:', rd.randint(1,6))

N=int(1e6)
dice1 = np.array(rd.choices(range(1,7),k=N))
dice2 = np.array(rd.choices(range(1,7),k=N))

#counting number of double sixes:
n = int(np.sum(np.floor((dice1+dice2)/12)))/N
print('(b) After',N,'rollings of 2 dice:\nFraction of double sixes obtained:',n)
print('Theoretical/Expected value', 1/36)
