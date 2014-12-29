# -*- coding: utf-8 -*-
"""
Created on Fri May 02 17:26:46 2014

authors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye
"""

"""This is a template for making an interactive network. You must
   have the weights you want already initialized/saved somewhere.
   This code will not run properly until you fill in the blanks
"""
   
from Network import *
from Helpers import *

nn = NeuralNetwork(0, 64, 0, 0, 10) #replace with desired values

nn.full_weight_update(array[[]]) #replace with true matrix

#print test3(nn, 'shortsamples.txt') These are for debugging
#print test1(nn, 'shortsamples.txt')

while True:
    execfile('drawer.py')
    
    execfile('read_jpeg.py')
    
    interactive_test3(nn, smaller)
    b = raw_input("Type n if you'd like to quit, any other key otherwise \n")
    if b == "n":
        break