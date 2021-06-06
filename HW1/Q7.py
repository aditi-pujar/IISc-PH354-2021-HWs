#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:02:45 2021

@author: aditi
"""
######################################################
#Q7

print('Exercise 7: Catalan Numbers\n \
Printing all Catalan numbers < 1.0e+9 in \
increasing order:')

'''
Required to print Catalan numbers less than \
1.0e+9 in increasing order where
c0 = 1
c_(n+1) = 4n+2/(n+2)c_(n)
        = (1+3n/(n+2))c_(n)
Thus, as the sequence is increasing anyways,\
we only need to now print them out.
'''

cn=1.0; i=0;
while cn <= 10**9:
    print('C_(',i,') = ',cn)
    c_new = (4*i+2)/(2*i+2)*cn
    cn = c_new
    i+=1

######################################################
