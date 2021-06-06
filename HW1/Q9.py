#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:29:57 2021

@author: aditi
"""

#Q9
from Q9_functions import max_BEn, binding_energy
print('Exercise 9: The semi-empirical mass formula')
######################################################

A=float(input('Enter mass number of element (A) >> '))
if A<=0.0:
    print('Invalid, please enter a positive value of A\n')
else:
    Z=float(input('Enter atomic number of element (Z) >> '))
    if Z<=0.0 or Z%1!=0.0:
        print('Invalid, please enter a positive integer value of Z\n')
    elif Z>A:
        print('Invalid, Z <= A always. Please enter a Z value > A.')
    else:
        B=binding_energy(A,Z)
        print('For atom with A =',A,'and Z ='\
              ,Z,':')
        print('(a) Binding energy, B =',B,'MeV')
        print('(b) Binding energy per nucleon (B/A) =',B/A,'MeV/nucleon')

'''
Verifying for A = 58, Z = 28:
For atom with A = 58.0 and Z = 28.0 :
(a) Binding energy, B = 493.93560680136824 MeV

Thus, BE ~ 490 MeV obtained.
'''
#######################################################

print('(c) For a given Z, to return A ∈ [Z,3Z] with \
maximum binding energy per nucleon (B/A):')
Z=float(input('Enter atomic number of element (Z) >> '))
if Z<=0.0 or Z%1!=0.0:
    print('Invalid, please enter a positive value of Z')
else:
    BE_max, A_max = max_BEn(Z)
    print('The maximum binding energy per nucleon obtained for:\n\
A =',A_max,'\nBinding Energy per Nucleon (B/A)_max =',BE_max,'MeV')

##########################################################
print('(d) For Z = 1,2,...,100, A ∈ [Z,3Z] that\n\
maximises binding energy per nucleon (B/A) is reported:')
print('Z\tA_max\t(B/A)_max (MeV)')
be_max,amax = max_BEn(1); zmax=1;
for zval in range(1,101):
    be_val,aval = max_BEn(zval)
    print(str(zval)+'\t'+str(aval)+'\t\t'+str(be_val))
    if be_val > be_max:
        be_max = be_val
        amax = aval
        zmax = zval
print('***')
print('The atom with greatest binding energy per nucleon here is:\n\
Z = ',zmax,' at A = ',amax,'with (B/A) =',be_max,'(MeV)')

'''
Though we theoretically know it to be Ni-62 as opposed to
some isotope of Cr (Z = 24) as the above suggests, this could be
because of different errors in calculations.
'''