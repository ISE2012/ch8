# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 02:07:06 2020

@author: ucobiz
"""

class Vehicle:
    
    def __init__(self, passengers, fuelcap, mpg):
        """Initialize vehicle with passengers, fuelcap, mpg data"""
        self.passengers = passengers # number of passengers
        self.fuelcap = fuelcap # fuel capacity in gallons
        self.mpg = mpg # fuel consumption in miles per gallon
    
    def get_range(self):
        """Compute the range, assuming a full tank of gas 
            range = fuelcap * mpg"""
        return self.fuelcap*self.mpg
    
    def fuel_needed(self, miles):
        """Compute fuel needed for a given distance: miles/mpg"""
        return miles/self.mpg
    
