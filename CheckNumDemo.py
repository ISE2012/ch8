# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 02:48:27 2020

@author: ucobiz
"""

from CheckNum import CheckNum

def main():
    num = CheckNum()
    
    if(num.isEven(10)):
        print("10 is even.")
        
    if(num.isEven(9)):
        print("9 is even.")
    
    if(num.isEven(8)):
        print("8 is even.")
        
main()

