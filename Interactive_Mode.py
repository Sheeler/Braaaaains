# -*- coding: utf-8 -*-
"""
Created on Fri May 02 11:11:30 2014

@author: Me!
"""

"""
Tack this code one where ever a network lives (Like in 
30NeuronNetowrk). It will let you interact with said network through
the drawing input
"""
    
from Helpers import *

while True:
    """This loop allows the user to interact with the network"""
    print "Draw your number in the new window\n"
    execfile('drawer.py')
    
    execfile('read_jpeg.py')
    
    interactive_test3(nn, smaller)
    b = raw_input("Type n if you'd like to quit, any other key otherwise \n")
    if b == "n":
        break