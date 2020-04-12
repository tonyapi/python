#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:54:35 2020

@author: antonio.pisante
"""
        
#%%
            
digits = {'0':'zero', '1':'one', '2':'two','3':'three','4':'four', \
          '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

new = {'1':'eleven', '2':'twelve', '3':'thirteen', '4':'fourteen', \
          '5':'fifteen', '6':'sixteen', '7':'seventeen', '8':'eighteen', \
          '9':'nineteen'}

units = {2:'hundred', 3:'thousand', 6:'million', 9:'billion', \
         12:'trillion', 15:'quadrillion', 18:'quintillion', \
         21:'sextillion', 24:'septillion', 27:'octillion', \
         30:'nonillion', 33:'decillion', 36:'undecillion', \
         39:'duodecillion', 42:'tredecillion', 45:'quattor-decillion', \
         48:'quindecillion', 51:'sexdecillion', 54:'septen-decillion', \
         57:'octodecillion', 60:'novemdecillion', 63:'vigintillion'}

decine = {'1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', \
          '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

def write_number(number):

    if number.isdigit():
        if number == '0':
            print('zero')
        elif number == '10':
            print('ten')
        else:
            print_number(number)
    else:
        print("This is not a number, bye.")
        
def print_number(number):
    counti = 0
    for i in range(len(number)):
        counti = counti + 1
        n = len(number) - counti
        if number[i] == '0':
            pass
        else:
            if n != 0:
                if n % 3 == 0:
                    if number[i-1] != '1':
                        print(digits[number[i]], "", end="")
                    else:
                        pass
                    print_units(number, counti)
                elif n % 3 == 1:
                    if number[i] == '1':
                        print_new(number, counti)
                    else:
                        print (decine[number[i]], "", end="")
                else:
                    if i == '0':
                        pass
                    else:
                        print(digits[number[i]],'hundred', "", end="")  
            else:
                if number[i] == '0':
                    break
                elif number[i-1] == '1':
                    break
                else:
                    print(digits[number[i]])
                break
        
def print_units(number, i):
    n = len(number) - i
    print(units[n])
    
def print_new(number, i):
    print(new[number[i]], "", end="")
        
        
        
        
        
        
        
        
        
        
        
    
