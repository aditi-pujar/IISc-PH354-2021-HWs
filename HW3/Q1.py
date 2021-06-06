#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:30:24 2021

@author: aditi
"""

#Q1
from cmath import sqrt
print('(a)To solve the quadratic equation\n\
ax^2 + bx + c = 0, input coefficients:')

a=float(input('Enter (non zero) a >> '))
while (a==0):
    a=float(input('Please enter (non zero) a only >> '))
b=float(input('Enter b >> '))
c=float(input('Enter c >> '))

def std_quadratic(a,b,c):
    det = sqrt(b*b-4*a*c)
    r1 = (-b+det)/(2*a)
    r2 = (-b-det)/(2*a)
    return r1,r2

def m_quadratic(a,b,c):
    det = sqrt(b*b-4*a*c)
    r1 = 2*c/(-b-det)
    r2 = 2*c/(-b+det)
    return r1,r2

y1,y2 = std_quadratic(a,b,c)
y1m,y2m = m_quadratic(a,b,c)

print('Using standard quadratic formula:\n\
root1 =',y1,'root2 =',y2)
print('Using modified quadratic formula:\n\
m_root1 =',y1m,'m_root2 =',y2m)
####################################################
#(b)
'''
For 
0.001x^2+1000x+0.001
'''
a = 10**-3
b = 10**3
c = 10**-3

y1,y2 = std_quadratic(a,b,c)
y1m,y2m = m_quadratic(a,b,c)
print('\n\n(b) For 0.001x^2+1000x+0.001')
print('\nUsing standard quadratic formula:\n\
root1 =',y1,'root2 =',y2)
print('\nUsing modified quadratic formula:\n\
m_root1 =',y1m,'m_root2 =',y2m)

'''
We can therefore see that the two forumlas give us \
    slightly different roots. As the determinant is very small
    => we are subtracting two almost equal numbers in either\
        the numerator or the denominator.
    As this effect is more pronounced in numerator than denominator
    Standard quadratic formula gives less accurate estimates.
    
    Taking average over 2 methods could help be the better estimate in all cases
    (both large as well as small determinant)
'''

#c

def ud_quadratic(a,b,c):
    r1,r2 = std_quadratic(a,b,c)
    mr1,mr2 = m_quadratic(a,b,c)
    return (r1+mr1)/2,(r2+mr2)/2
