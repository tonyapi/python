#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:15:17 2020

@author: antonio.pisante
"""

#%%
def problem1_7():
    b1 = float(input("Enter the lenght of one of the bases: "))
    b2 = float(input("Enter the lenght of the other base: "))
    h = float(input("Enter the height: "))
    A = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases", b1, "and", b2, end=" ")
    print("and height", h, "is", A)




