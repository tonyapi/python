#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:37:12 2020

@author: antonio.pisante
"""

#%%
def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    dmonths = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    print(dmonths[mon], end="")
    print("/", end="")
    print(day, end="")
    print("/", end="")
    print(year)

#%%