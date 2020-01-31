#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:12:07 2020

@author: wang1278
"""

def gcd(a,b):
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)

print(gcd(150,45))