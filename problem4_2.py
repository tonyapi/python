#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:45:10 2020

@author: antonio.pisante
"""

#%%   
def problem4_2(ran_list):
    """ Compute the mean and standard deviation of a list of floats """
    import statistics
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))