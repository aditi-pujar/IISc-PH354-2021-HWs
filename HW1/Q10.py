#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 01:34:01 2021

@author: aditi
"""

#Q10
print('Exercise 10: Binomial Coefficients')
# without using recursion or defining the factorial function
#(a)
def binomial(n,k):
    nval=int(n); kval=int(k);
    num=1; den=1;
    for i in range(0,kval):
        num = (nval-i)*num
        den = (i+1)*den
    Cnk = num/den
    return int(Cnk)
######################################################
#(b)

def print_sameline(k):
    print(str(k), end='\t', flush = True)
######################################################

print('Printing out the first 20 lines of Pascal triangle:')
for n in range(1,21):
    for m in range(1,n+2):
        print_sameline(binomial(n,m-1))
    print('\n')
print('***')

######################################################
#(c)
print('(c)\na. Probability that when a coin is tossed 100 times,\n\
heads comes up 60 times \n= binomial(100,60)/(2^(100))\n\
=',binomial(100,60)/(2**(100)) )

prob=0
for i in range(60,101):
    prob+=binomial(100,i)
prob/=2**100

print('\nb. Probability that when a coin is tossed 100 times,\n\
heads comes up 60 times or more \n\
= summing over probabilities it occurs 60, 61, ... 100 times\n\
=', prob)
#######################################################
