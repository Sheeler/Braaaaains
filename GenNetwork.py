# -*- coding: utf-8 -*-
"""
Created on Fri May 02 18:06:34 2014

authors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye


This code can be used to generate a neural network trained on
the drawn number set, then save the weights somewhere if desired"""
   
   
from Network import *
import numpy as np
np.set_printoptions(threshold=np.nan)
from Helpers import *

nn = NeuralNetwork(.8, 64, 2, 28, 10)
speeds = [.6, .4, .2, .1]

for i in xrange(len(speeds)+1):
    print 1
    if i != 0:
        print 3
        nn.speed_update(speeds[i-1])
    print 2
    multitrain(nn, 'shortsamples.txt')
    multitrain(nn, 'shortsamples.txt')

print test1(nn, 'shortsamples.txt')
print test3(nn, 'shortsamples.txt')
