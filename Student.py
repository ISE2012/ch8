# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:46:31 2020

@author: ucobiz
"""

class Student:
    """This is a class for a student"""
    MAX_ID_LENGTH = 4
    numStudents = 0
    
    def __init__(self, name, age, gpa):
        """Constructor for a student"""
        self.full_name = name
        self.age = age
        self.gpa = gpa
        
    def get_age(self):
        """Method to get an age for a student
            return an age 
        """
        return self.age