# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 02:37:17 2020

@author: ucobiz
"""

from Vehicle import Vehicle

def main():
    DISTANCE = 252
    
    minivan = Vehicle(7, 16, 21)
    gallons = minivan.fuel_needed(DISTANCE)
    print("To go "+str(DISTANCE)+" miles, minivan needs "+str(gallons)+" gallons of fuel.")
    
    sportcar = Vehicle(2, 14, 12)
    gallons = sportcar.fuel_needed(DISTANCE)
    print("To go "+str(DISTANCE)+" miles, sportcar needs "+str(gallons)+" gallons of fuel.")
        
main()

