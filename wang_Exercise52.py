#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:52:41 2020

@author: wang1278
"""

def check_fermat(a,b,c,n):
    if (a**n + b**n == c**n) and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No,that doesn't work.")

def check_numbers():
    a=int(input("Please choose input value for a: "))
    b=int(input("Please choose input value for b: "))
    c=int(input("Please choose input value for c: "))
    n=int(input("Please choose input value for n: "))
    return check_fermat(a,b,c,n)

check_numbers()