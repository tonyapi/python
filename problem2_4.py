#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:36:31 2020

@author: antonio.pisante
"""

#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    a = []
    for i in range(0,10):
        i = random.random() * 5 + 30
        a.append(i)
    print (a)

#%%