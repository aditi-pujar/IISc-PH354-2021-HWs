#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:12:08 2021

@author: aditi
"""
#####################################################
#Q2
print('Exercise 2:\n')
#from common_functions import SimpsonRule, TrapezoidalRule

def f(x):
    return x**4-2*x+1

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
        I*=h/3
        x3 = x2+h; f3=f(x3);
        final_interval=(h/2)*(f2+f3) #treated using Trapezoidal
        I+=final_interval
        return I

def TrapezoidalRule(a,b,n):
    I=0
    h=(b-a)/n
    for i in range(n):
        x0 = a+i*h; x1 = x0+h;
        f0 = f(x0); f1 = f(x1);
        I+= f0+f1
    I*=h/2
    return I

#(a)
print('(a) Integrating using Simpson\'s\
rule with 10 slices:')

a = 0
b = 2
I = SimpsonRule(a,b,10)
#(b)
print('I =',I,'\n\n(b) Analytical value = 4.4\n%\
 Error =',abs(I-4.4)*100/4.4)

#(c)

print('\n(c)\n\
n\t\tSimpson\'s Rule\t\t\t\tTrapezoidal Rule\n\
\t\tI\t\t\t% Error\t\t\tI\t\t\t% Error')
sr=[]; tr=[]; sr_err=[]; tr_err=[];

for i in [10,100,1000]:
    srval = SimpsonRule(a,b,i)
    srval_err = abs(srval-4.4)*100/4.4
    trval = TrapezoidalRule(a,b,i)
    trval_err = abs(trval-4.4)*100/4.4
    
    print('%d\t\t%f\t\t%.6f\t\t\t%f\t\t%.6f'%(i,srval,srval_err,trval,trval_err))

print('Thus we can see Simpson\'s Rule does significantly\
 better than Trapezoidal Rule.')
####################################################
