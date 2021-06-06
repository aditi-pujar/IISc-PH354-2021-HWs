#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:55:45 2021

@author: aditi
"""

#Q7
print('Exercise 7:')
import math
def f(x):
    fval = (math.sin(math.sqrt(100*x)))**2
    return fval

def TrapezoidalRule(a,b,n):
    I=0
    h=(b-a)/n
    for i in range(n):
        x0 = a+i*h; x1 = x0+h;
        f0 = f(x0); f1 = f(x1);
        I+= f0+f1
    I*=h/2
    return I

def adaptive_TR(a,b,whole,eps):
    n=2
    while abs(TrapezoidalRule(a,b,n)-whole) > eps:
        print(n,'\t\t',whole,'\t\t',TrapezoidalRule(a,b,n)-whole)
        whole = TrapezoidalRule(a,b,n)
        n*=2

print('(a) Adaptive Trapezoidal Rule:')
print('n\t\t\tI\t\t\t\t\tError')
a = 0; b = 1; eps = 10e-6
whole = TrapezoidalRule(a,b,1)
adaptive_TR(a,b,whole,eps)