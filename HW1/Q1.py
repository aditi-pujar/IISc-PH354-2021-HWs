#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 00:46:40 2021

@author: aditi
"""
###############################################################
''' PH354 HW1
Aditi Ajith Pujar
14740 '''
###############################################################

import math
from scipy.constants import g
#Q1
print('Exercise 1: A ball dropped from a tower')
h=float(input('Enter height of tower in meters >> '))
#g = acceleration due to gravity, physical constant
t = math.sqrt(2*h/g)
print('Ball hits the ground in',t,'seconds.')

########################################################