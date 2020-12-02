# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:45:26 2020

@author: ucobiz
"""
# import Dog
from Dog import Dog

dog_A = Dog("Fido")
dog_A.add_tricks("roll over")

print(dog_A.name)
print(dog_A.tricks)

dog_B = Dog("Buddy")
dog_B.add_tricks("play dead")

print(dog_B.name)
print(dog_B.tricks)
