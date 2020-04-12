#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:05:24 2020

@author: antonio.pisante
"""

#%%
def problem3_7(csv_pricefile, flower):
    import csv
    
    f = open(csv_pricefile)
    for row in csv.reader(f):
        if row[0] == flower:
            print(row[1])
        pass
    
#%%