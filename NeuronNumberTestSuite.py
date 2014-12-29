# -*- coding: utf-8 -*-
"""
Created on Thu May 01 17:52:40 2014

authors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye

This code was used to determine the number of neurons a network
should have in it's hidden layers. Best results were in the 
range 25-35.
"""
from Network import *
import numpy as np
np.set_printoptions(threshold=np.nan)
from Helpers import *

n1 = NeuralNetwork(.7, 64, 2, 40, 10)
n2 = NeuralNetwork(.7, 64, 2, 30, 10)
n3 = NeuralNetwork(.7, 64, 2, 25, 10)
n4 = NeuralNetwork(.7, 64, 2, 20, 10)

nns = [n1,n2,n3,n4]

print ("All networks have 2 hidden layers, 64 input neurons, " +
       "and 10 output neurons. Network one has 40 neurons per hidden" +
       " layer, 2->30, 3->25, 4->20")

i = 0
for e in nns:
    print str(i+1)
    print 'test1'
    print test1(e, 'shortsamples.txt')
    print 'test3'
    print test3(e, 'shortsamples.txt')
    i+=1
    
i = 0
print "Loop 1"
while i<2:
    print ("Training Round " + str(i+1))
    a = 0
    for net in nns:
        a +=1
        print a
        multitrain(net, 'shortsamples.txt')
    i+=1
    
i = 0
for e in nns:
    print str(i+1)
    print 'test1'
    print test1(e, 'shortsamples.txt')
    print 'test3'
    print test3(e, 'shortsamples.txt')
    e.speed_update(.4)
    i+=1

i=0
    
print "Loop 2"
while i<2:
    print ("Training Round " + str(i+1))
    a = 0
    for net in nns:
        a +=1
        print a
        multitrain(net, 'shortsamples.txt')
    i+=1
    
i = 0
for e in nns:
    print str(i+1)
    print 'test1'
    print test1(e, 'shortsamples.txt')
    print 'test3'
    print test3(e, 'shortsamples.txt')
    e.speed_update(.2)
    i+=1

i=0
    
print "Loop 3"
while i<2:
    print ("Training Round " + str(i+1))
    a = 0
    for net in nns:
        a +=1
        print a
        multitrain(net, 'shortsamples.txt')
    i+=1
    
i = 0
for e in nns:
    print str(i+1)
    print 'test1'
    print test1(e, 'shortsamples.txt')
    print 'test3'
    print test3(e, 'shortsamples.txt')
    e.speed_update(.1)
    i+=1
   
i=0

    
print "Loop 4"
while i<2:
    print ("Training Round " + str(i+1))
    a = 0
    for net in nns:
        a +=1
        print a
        multitrain(net, 'shortsamples.txt')
    i+=1
    
i = 0
for e in nns:
    print str(i+1)
    print 'test1'
    print test1(e, 'shortsamples.txt')
    print 'test3'
    print test3(e, 'shortsamples.txt')
    i+=1