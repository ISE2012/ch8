# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 02:11:28 2020

@author: ucobiz
"""

from Vehicle import Vehicle

def main():
    minivan = Vehicle(7, 16, 21)
    
    range = minivan.get_range()
    print("Minivan passenger:", minivan.passengers)
    print("Minivan fuelcap:", minivan.fuelcap)
    print("Minivan mpg:", minivan.mpg)
    print("Minivan can carry " + str(minivan.passengers) + " with a range of " + str(range))
    print(minivan.get_range.__doc__)
    
main()

