# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 02:24:06 2020

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
    
    sportcar = Vehicle(2, 14, 12)
    range2 = sportcar.get_range()
    print("Sportcar passenger:", sportcar.passengers)
    print("Sportcar fuelcap:", sportcar.fuelcap)
    print("Sportcar mpg:", sportcar.mpg)
    print("Sportcar can carry " + str(sportcar.passengers) + " with a range of " + str(range2))
        
main()

