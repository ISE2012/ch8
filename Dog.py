# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:37:43 2020

@author: ucobiz
"""

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_tricks(self, trick):
        self.tricks.append(trick)