#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:07:52 2021

@author: aditi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:55:45 2021

@author: aditi
"""

#Q7
print('Exercise 8:')
import math
def f(x):
    fval = (math.sin(math.sqrt(100*x)))**2
    return fval

def SimpsonRule(a,b,n):
    I=0
    h=(b-a)/n
    if n%2==0:
        for i in range(0,n,2):
            x0 = a+i*h; x1 = x0+h; x2 = x1+h;
            f0 = f(x0); f1 = f(x1); f2 = f(x2);
            I+=f0+4*f1+f2
        I*=h/3
        return I
    else:
        for i in range(0,n-1,2):
            x0 = a+i*h; x1 = x0+h; x2 = x1+h;
            f0 = f(x0); f1 = f(x1); f2 = f(x2);
            I+=f0+4*f1+f2
            print(x2)
        I*=h/3
        x3 = b
        f3=f(x3)
        final_interval=(h/2)*(f(b-h)+f3) #treated using Trapezoidal
        I+=final_interval

def adaptive_SR(a,b,whole,eps):
    n=2
    while abs(SimpsonRule(a,b,n)-whole) > eps:
        print(n,'\t\t',whole,'\t\t',SimpsonRule(a,b,n)-whole)
        whole = SimpsonRule(a,b,n)
        n*=2

print('(a) Adaptive Simpson Rule:')
print('n\t\t\tI\t\t\t\t\tError')
a = 0; b = 1; eps = 10e-6
whole = SimpsonRule(a,b,1)
adaptive_SR(a,b,whole,eps)