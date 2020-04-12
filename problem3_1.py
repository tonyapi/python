#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:17:42 2020

@author: antonio.pisante
"""

#%%
def problem3_1(txtfilename):
    f = open(txtfilename)
    ncar = 0
    for line in f:
        ncar = ncar + len(line)
        print(line, end="")
    print("\n")
    print("There are", ncar, "letters in the file.")

#%%