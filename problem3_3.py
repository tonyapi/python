#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:30:49 2020

@author: antonio.pisante
"""

#%%
def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    tmonths = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    call = int(month - 1)
    print(tmonths[call], day, end="")
    print(",", year)

#%%