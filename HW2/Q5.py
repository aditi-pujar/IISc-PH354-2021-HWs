#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 08:51:59 2021

@author: aditi
"""

#Q5
print('Exercise 5: Error on Trapezoidal Rule for integrating\n\
(x^4-2x+1) over 0 to 2:')

def f(x):
    return (x**4-2*x+1)

def TrapezoidalRule(a,b,n):
    I=0
    h=(b-a)/n
    for i in range(n):
        x0 = a+i*h; x1 = x0+h;
        f0 = f(x0); f1 = f(x1);
        I+= f0+f1
    I*=h/2
    return I

print('n\t\tI\t\t\tError\t\t|I-4.4|')
a=0; b=2;
I1=TrapezoidalRule(a,b,10)
I2=TrapezoidalRule(a,b,20)
I1err = (I2-I1)*(4/3)
I2err = I1err/4
I1err0 = abs(I1-4.4)
I2err0 = abs(I2-4.4)

print('10\t\t%f\t\t%.5f\t\t%.5f' %(I1,I1err,I1err0))
print('20\t\t%f\t\t%.5f\t\t%.5f' %(I2,I2err,I2err0))

print('\nThe error thus calculated is not exactly equal to |I-4.4| because:\n\
In the above calculation, we have only assumed leading order in h to calculate error\n\
while the difference has taken into consideration all the terms of h.')

####################################################
# Checking for consistency before using this error estimate in Q7:
'''
I3=TrapezoidalRule(a,b,40)
I4=TrapezoidalRule(a,b,80)

I3err1 = (I4-I3)*(4/3)
I3err2 = (I3-I2)*(1/3)

print('Is I3err1 = I3err2? >> ', (I3err1==I3err2))

'''