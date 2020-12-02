# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:56:01 2020

@author: ucobiz
"""

from Counter import Counter

one = Counter()
two = Counter()

one.increment()
two.increment()
two.increment()

print("one's total", one.my_total)
print("class total", one.__class__.overall_total)
print("two's total", two.my_total)
print("class total", two.__class__.overall_total)