#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 01:25:12 2021

@author: aditi
"""
def binding_energy(A,Z):
    a1=15.67; a2=17.23; a3=0.75; a4=93.2;
    if A%2!=0:
        a5=0
    elif Z%2==0:
        a5=12.0
    else:
        a5=-12.0
        
    B=a1*A-a2*(A**(2/3))-a3*(Z**2)/(A**(1/3))\
            -a4*((A-2*Z)**2)/A+a5/(A**(1/2))
    return B
#######################################################
def max_BEn(Z):
    A_max=Z
    BE_max=binding_energy(A_max,Z)/A_max
#    print(BE_max,'\t',A_max)
    for Aval in range(int(Z+1),int(3*Z+1),1):
        BE_new=binding_energy(Aval,Z)/Aval
#        print(BE_new,'\t',Aval)
        if BE_new > BE_max:
            BE_max = BE_new
            A_max = Aval
    return BE_max, A_max
#######################################################
