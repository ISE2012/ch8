# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:54:16 2020

@author: ucobiz
"""

class Counter:
    # class attribute
    overall_total = 0
    
    def __init__(self):
        # data attribute
        self.my_total = 0
    
    def increment(self):
        self.my_total  += 1
        self.__class__.overall_total += 1