# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:23:47 2020

@author: ucobiz
"""

from Counter import Counter

def main():
    one = Counter()
    two = Counter()
    
    one.increment() # my_total = 1, overall_total = 1
    two.increment() # my_total = 1, overall_total = 2
    two.increment() # my_total = 2, overall_total = 3
    
    print("one's total", one.my_total)
    print("class total", one.__class__.overall_total)
    print("two's total", two.my_total)
    
main()
    
    