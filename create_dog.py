# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:39:04 2020

@author: ucobiz
"""

from Dog import *
#from Dog import Dog
import Dog as dog_obj


d = Dog("Fido")
e = dog_obj.Dog("Buddy")

d.add_tricks("roll over")
e.add_tricks("play dead")

print(d.tricks)
print(e.tricks)

