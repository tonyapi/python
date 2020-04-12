#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:37:35 2020

@author: antonio.pisante
"""

#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    random.seed(431)
    for i in range (0,100):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = a + b
        print(c)
   
#%%