#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:24:56 2021

@author: aditi
"""

#Q11
from math import sqrt, nan
print('Exercise 11: Prime Numbers')
print('Printing out the list of all primes less than 10^4:')
primes=[2]

for n in range(3,10000+1):
    lim = int(sqrt(n))
    last_prime = primes[len(primes)-1]
    for m1 in primes:
        #to check if divisible by all primes so far
        if n%m1==0:
            break
    if m1==last_prime: 
        #implies above loop didn't break, not divisible by any primes so far OR divisible by m1
        m2=0
        for m2 in range(m1,lim+1):
            if n%m2==0:
                break
        if (m2==lim and n%m2!=0) or(m2==0): #second condition means m1=lim, loop wasn't entered
            #implies above loop also didn't break AND not divisible by sqrt(n) \ implies no factors between biggest prime so far and sqrt(n)
            primes.append(n)
            #print(primes)
print(primes)