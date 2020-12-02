# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:58:34 2020

@author: ucobiz
"""

from Student import Student

def main():
    a = Student("John", 19)
    print(a.full_name)
    print(a.get_age())
    
    b = Student("Peter", 21)
    print(b.full_name)
    print(b.get_age())
    
main()