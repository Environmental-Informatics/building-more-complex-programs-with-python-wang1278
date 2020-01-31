#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:18:11 2020

@author: wang1278
"""
import math

def mysqrt(a):
    a = float(a)
    x = a/2
    while True:
        sqr= (x + a/x) / 2
        if x == sqr:
            break
        x = sqr
    return x
# Note that in order to make the format of the table similar to the on in the book, {:<20}'.format() function was used.
def test_square_root(f):
    print('a   msqrt(a)             math.sqrt(a)         diff')
    print('-   --------             ------------         ----')

    for a in f:
        print(float(a),'{:<20}'.format(mysqrt(a)),'{:<20}'.format(math.sqrt(a)),'{:<20}'.format(abs(mysqrt(a)-math.sqrt(a))))

test_square_root(range(1,9))