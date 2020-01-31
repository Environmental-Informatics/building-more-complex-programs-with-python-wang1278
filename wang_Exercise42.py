#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:20:17 2020

@author: wang1278
"""

import turtle

from polygon import arc

# Define the function to draw a petal using 2 arcs.
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

# Define the function to draw a flower using the petal function.
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

# Define the function to move the pointer by a distance.
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

# Assemble the functions to draw all 3 flowers.
bob = turtle.Turtle()

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()