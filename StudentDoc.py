# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:54:33 2020

@author: ucobiz
"""

from Student import Student

def main():
    test1 = Student("Jane", 22, 3.2)
    print(test1.get_age())
    print(test1.__doc__)
    print(test1.__init__.__doc__)
    print(test1.get_age.__doc__)
    
main()