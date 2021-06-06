#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:04:15 2021

@author: aditi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 08:51:59 2021

@author: aditi
"""

#Q6
print('Exercise 6: Error on Simpson Rule for integrating\n\
(x^4-2x+1) over 0 to 2:')

def f(x):
    return (x**4-2*x+1)

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
####################################################
print('n\t\tI\t\t\tError\t\t\t|I-4.4|')
a=0; b=2;
I1=SimpsonRule(a,b,10)
I2=SimpsonRule(a,b,20)
I1err = (I2-I1)*(16/15)
I2err = I1err/16
I1err0 = abs(I1-4.4)
I2err0 = abs(I2-4.4)

print('10\t\t%f\t\t%f\t\t%f' %(I1,I1err,I1err0))
print('20\t\t%f\t\t%f\t\t%f' %(I2,I2err,I2err0))

print('\nHere the error obtained in both is exactly the same unlike in Trapezoidal rule, because:\n\
Here the I\'s are much closer to the exact analytic value (as  Simpson\'s is more accurate.)')