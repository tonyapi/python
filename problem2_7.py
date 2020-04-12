#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:18:20 2020

@author: antonio.pisante
"""

#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter lenght of side one: "))
    b = float(input("Enter lenght of side two: "))
    c = float(input("Enter lenght of side three: "))
    s = 0.5 * (a+b+c)
    x = s * (s-a) * (s-b) * (s-c)
    Area = x**.5
    print("Area of a triangle with sides", a, b, c, "is", Area)
    
#%%