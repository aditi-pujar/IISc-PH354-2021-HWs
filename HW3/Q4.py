#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 05:08:52 2021

@author: aditi
"""

# constants
a = 1
b = 2

# initial guesses
x = 2.1
y = 0.38
print('Rearrangement 1:')
print('n\txn\t\t\t\tyn')

# q4b

for n1 in range(50):
    xn1 = y*(a+x**2)
    yn1 = b/(a+x**2)
    x,y = xn1,yn1
    print(n1,'\t',xn1,'\t',yn1)


'''
Thus, for the given rearrangement,
relaxation method does not converge.
'''

#q4c

# re-initialise
x = 2.1
y = 0.38

print('\n\nModified Rearrangement 2:')
print('n\txn\t\t\t\tyn')
for n2 in range(20):
    xn2 = y*(a+x**2)
    yn2 = x/(a+x**2)
    x,y = xn2,yn2
    print(n2,'\t',xn2,'\t',yn2)

'''
Thus, for above rearrangement,
relaxation method quickly converges to
(x*,y*) = (2,0.4)

As obtained analytically in q4a
'''





















#Q4

