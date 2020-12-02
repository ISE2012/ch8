# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:47:35 2020

@author: ucobiz
"""

from Student import Student

def main():
    a = Student("John", 19)
    print(a.full_name)
    print(a.get_age())
    
main()