#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:39:08 2020

@author: antonio.pisante
"""

#%%
def problem2_8(temp_list):
    sum_ = 0
    for i in temp_list:
        sum_ = sum_ + i
    max_= max(temp_list)
    min_ = min(temp_list)
    count_ = len(temp_list)
    average_ = sum_ / count_
    print("Average:",average_)
    print("High:",max_)
    print("Low:",min_)
    
#%%