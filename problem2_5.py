#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:37:07 2020

@author: antonio.pisante
"""

#%%

import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    random.seed(171)
    for i in range(0,10):
        print(random.randint(1,6)) 
    
#%%