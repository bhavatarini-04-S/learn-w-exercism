"""
Created on Wed Mar 29 05:49:57 2017
Updated on Tues Nov 9 10:39:56 2021

@author: bethanygarcia
"""

def square(number):    
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1