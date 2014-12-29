# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 22:17:34 2014

authors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye
"""
import numpy as np
np.set_printoptions(threshold=np.nan)


def softmax (raw):
    
    """ Normalizes a vector (represented as a 
        1 column array)"""
    
    probs = [0.]*len(raw)
    total = sum(raw)
    for i in range(len(probs)):
        probs[i] = raw[i]/total
    return probs
    
    
def test3(network, data):
    
    """Counts how many times the one of the networks's top three
       guesses is correct when run over a particular data set.
       The data must be 65 numbers seperated by commas per line, 
       with the first 64 numbers forming a vector and the final
       number to be the desired numeral to work with our code.
       Look at shortsamples.txt to see what this looks like.
       
       Output of the given network must be vector of length 
       longer than 3 (as there can't be 3 top guesses out
       of 2 possibilities)"""
       
    f = open(data)
    count = 0
    
    for line in f:
        ins = line.split(',')
        last = (ins.pop())[0]
        for i in xrange(len(ins)):
            ins[i] = [int(ins[i])]
        outs = network.propagate(np.array(ins))
        outs2 = [None]*10
        for j in range(network.out_neurons):
            outs2[j] = (outs[j], j)
        outs2.sort()
        maxis = outs2[-3:]
        for e in maxis:
            if e[1] == int(last):
                count+=1
                break
    return count
    
    
def test1(network, data):
    
    """Operates like test three, but only returns the number
       of times the first guess was correct"""
       
    f = open(data)
    count = 0
    
    for line in f:
        ins = line.split(',')
        last = (ins.pop())[0]
        for i in xrange(len(ins)):
            ins[i] = [int(ins[i])]
        outs = network.propagate(np.array(ins))
        maxi = (0,0)
        for j in range(network.out_neurons):
            if outs[j][0] > maxi[1]:
                maxi = (j,outs[j][0])
        if maxi[0] == int(last):
            count += 1
    return count
    

def interactive_test3(network, u_input):
    
    """Provides conversational voice for NeuralNetwork while
       running a network in interactive mode"""
    
    outs = network.propagate(u_input)
    outs2 = [None]*10
    for j in range(network.out_neurons):
        outs2[j] = (outs[j], j)
    outs2.sort()
    for i in xrange(3):
        a = raw_input('Was your number ' + str(outs2[i][1]) + '? Type y if so,'
                    + ' return otherwise.\n')
        if a == 'y':
            print ("Yipee! Not bad for a bunch of matrices, huh? I'm one " +
               "smart computer")
            return True
    print "Aww, I guess I'm a pretty dumb bucket of bolts :( I'll go cry now"
    return False
    
    
def multitrain(network, data):
    
    """Trains given neural network on a data set of expected format.
       Make sure dimension of input match the network.
       First arg is network, second is name of file containing data."""
       
    f = open(data)
    
    for line in f:
        ins = line.split(',')
        last = (ins.pop())[0]
        for i in xrange(len(ins)):
            ins[i] = [int(ins[i])]
        if len(ins) != network.in_neurons:
            raise Exception("Unexpected input length - does not match network")
        else: network.train(np.array(ins), int(last))
        
def doubletrain(network):
    multitrain(network, 'shortsamples.txt')
    multitrain(network, 'bigsample.txt')