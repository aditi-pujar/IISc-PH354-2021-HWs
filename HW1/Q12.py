#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 03:18:28 2021

@author: aditi
"""

#Q12
print('Exercise 12: Recursion')

#(a) Catalan numbers using recursion:
# This function calculates the n-th Catalan number:
def catalan_recursive(n):
    if n%1!=0:
        print('Invalid, please give positive integer inputs only.')
        return 0
    else:
        if n==0:
            return 1
        else:
            return (4*n-2)/(n+1)*catalan_recursive(n-1)

print('(a) Catalan numbers using recursion:\nC100 is obtained as\n=',catalan_recursive(100))

#(b) Finding GCD using recursion:
def g(m,n):
    if m%1!=0 or n%1!=0:
        print('Invalid, please give non-negative integer inputs only.')
    else:
        if n==0:
            return m
        else:
            return g(n,m%n)

print('(b) Finding GCD using recursion:\nThe greatest common divisor of 108 and 192 is\n=',g(108,192))
