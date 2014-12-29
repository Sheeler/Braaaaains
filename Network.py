# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 22:05:42 2014

authors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye
"""

import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pylab as mpl
import math
import random
from Helpers import *


class NeuralNetwork(object):
    
    """This class creates a general, multilayer backpropagation nerual
       network, input number of first layer neurons, number of hidden 
       layers, number of neurons in the hidden layer, and number of 
       neurons in final layer, all numbers must be ints greater
       than 0"""


    def __init__(self, speed, L1_Neurons, N_Hidden, LN_Neurons, L_end_Neurons):

        """Initializes the object"""

        self.layers = N_Hidden
        self.neurons = LN_Neurons
        self.in_neurons = L1_Neurons
        self.out_neurons = L_end_Neurons
        self.speed = speed
        self.weights = self.__gen_weights()
        self.activity = self.__gen_activity_or_membrane()
        self.membrane_potential = self.__gen_activity_or_membrane()



    """Initializer helper functions"""


    def __gen_weights(self):

        """ initializes a list of small-random matrices to 
            proper size per layer"""

        def random_array(n,m):
            x = np.zeros((n,m))
            for i in xrange(n):
                    for j in xrange(m):
                        x[i,j] = (2*random.random()-1)/((self.neurons)**(0.5))
            return x
            
        first = [random_array(self.neurons, self.in_neurons)]
        last = [random_array(self.out_neurons, self.neurons)]
        if self.layers > 1:
            mids = [random_array(self.neurons, self.neurons) 
                   for __ in xrange(self.layers - 1)]
            return first + mids + last
        else:
            return first + last
            
            
    def __gen_activity_or_membrane(self):
        
        """Generates a list of activity (activation function outputs) /
           membrane potential (activation function inputs) matrices
           of 0 upon initialization of object"""
           
        first = np.zeros((self.in_neurons, 1))
        last = np.zeros((self.out_neurons, 1))
        if self.layers > 0:
            mids = [np.zeros((self.neurons,1)) for __ in xrange(self.layers)]
            return [first] + mids + [last]
        else:
            return [first] + [last]



    """Updating functions for weights/activity matrices"""
    
    
    def speed_update(self, speed):

        """Updates training speed. Please input an int/float"""        
        
        self.speed = speed
    
    
    def __membrane_or_activity_update(self, mem_or_act, layer, new_mem_or_act):
    
        """Will update a single matrix in the membrane or activity 
           matrix lists. Argument order is the current membrane or 
           activity, layer to change, new matrix"""
        
        old_shape = mem_or_act[layer].shape
        if layer >= len(mem_or_act):
            print "Index greater than number of layers in network"
            return None
        elif old_shape == new_mem_or_act.shape:
            mem_or_act[layer] = new_mem_or_act
            return None
        else:
            print ("Your input was of dimension " + str(new_mem_or_act.shape) +
            " but the desired dimension was" + str(old_shape))
            return None


    def __full_matrix_list_update(self, self_matrices, new_matrices):
        
        """will update any matrix list given lists match in lenght
           and dimensions of each entry"""
        
        old_len = len(self_matrices)
        new_len = len(new_matrices)
        if old_len == new_len:
            for i in range(old_len):
                cur_shape = self_matrices[i].shape
                new_shape = new_matrices[i].shape
                if new_shape != cur_shape:
                    print ("Invalid input, your " + str(i) + "th element was" +
                           " of dimiension " + str(new_shape) +
                           " but the proper dimension was " + str(cur_shape))
                    return None
            return new_matrices
        else:
            print ("Invalid input, your list was of length " +
                   str(new_len) + " but the proper length was " +
                   str(old_len))
            return None        

        
    def update_weights(self, layer, weight_matrix):
        
        """updates a single matrix in the list of weights.
           First argument is the index of the weights you'd like
           to update, indexed from 0 (will reject invalid inputs). 
           Second argument is the new matrix (will reject matrix
           without proper dimensions)"""
           
        weight_shape = self.weights[layer].shape           
        if layer >= len(self.weights):
            print ("Index greater than number of weight matrices (" + 
                   str(len(self.weights)) + ") in network. Remember" + 
                   " indexed from 0")
            return None
        elif weight_shape == weight_matrix.shape:
            self.weights[layer] = weight_matrix
            return None
        else:
            print "Your input was of wrong dimension"
            print ("desired dimension was" + str(weight_shape))
            return None
            
            
    def full_weight_update(self, weight_matrices):
        
        """updates the entire list of weight matrices. Takes a weight
           matrix list as its argument. Will reject invalid matrix 
           lists"""
        
        self.weights = self.__full_matrix_list_update(self.weights, 
                                                      weight_matrices)
        return None

    
    def update_activity(self, layer, new_activity):
        
        """updates a single matrix in the list of activity. First
           argument is the index of the activity layer you'd like to 
           update, indexed from 0 (will reject invalid inputs). Second
           argument is the new activity matrix for said layer 
           (will reject invalid input)"""
           
        return self.__membrane_or_activity_update(self.activity, layer, 
                                                  new_activity)
                                                  
                                                  
    def full_activity_update(self, new_activities):
        
        """updates the entire activity matrix list. Takes only
           an activty matrix list as its argument. Will reject 
           invalid matrix lists"""

        self.activity = self.__full_matrix_list_update(self.activity, 
                                                       new_activities)
        return None
            
            
    def update_membrane_potential(self, layer, new_potential):

        """updates a single matrix in the list of membrane porentials.
           will reject invalid indices and matrices of wrong dimension
        """

        return self.__membrane_or_activity_update(self.membrane_potential, 
                                                  layer, new_potential)
    
    
    def full_update_membrane_potential(self, new_membrane_potential):
        
        """updates the entire membrane potential list. Takesonly
           a membrane potential list as its argument. Will reject
           invalid matrix lists"""
        
        self.membrane_potential = self.__full_matrix_list_update(
                               self.membrane_potential, new_membrane_potential)
        return None
        
    
    
    """Get information about Network or view in color
       get methods print the arrays/lists
       view methods display colored matrix/plot"""     
            
            
    def get_size(self):
        
        """takes no arguments. Returns size of input layer, number
           and size of hidden layers, and size of output layer"""
           
        return (self.in_neurons, self.layers, self.neurons, self.out_neurons)
        
        
    def get_weights(self):
        
        """takes no arguments. Returns the weight matrices (also 
           accesible by just object.weights, but let's pretend that 
           instance variables are private like in OCaml for fun)"""

        return self.weights
    
    
    def get_activity(self):

        """takes no arguments. Returns the activity matrices (also
           accesible by just object.activity, but let's pretend that
           instance variables are private like in OCaml for fun)"""
        
        return self.activity
        
        
    def get_membrane_potential(self):
        
        """Takes no arguments. Returns the list of 
           membrane potentials"""
           
        return self.membrane_potential

    
    def __view_general(self, matrix_list):
        
        """Makes a colored matrix disply for a matrix list.
           Takes only the matrix list as an argument"""
           
        for d in matrix_list:
            mpl.matshow(d)
        mpl.show()
        return None
        
        
    def view_activity(self):
        
        """will make the pretty color matrix for activity"""
        
        return self.__view_general(self.activity)
        
        
    def view_weights(self):
        
        """will do the pretty color matrix thing for weights"""
       
        return self.__view_general(self.weights)

        
    def view_membrane(self):
        
        """will make the pretty color matrix for membrane potential"""
        
        return self.__view_general(self.membrane_potential)
        
        
        
    """Functions associated with network and training"""
    
    def activate(self, x):
        
        """our activation function"""

        return 1 / (1 + (math.e)**(-1 * x))
        
        
    def d_activate(self, f):
        
        """derivative of activation function f in terms of f. Needs to
        be entered manually. Currently corresponds to logistic."""
        
        return f*(1-f)
        
        
    def activate_layer(self, layer):
        
        """input which layer you would like to activate
           (integer indexed from 0)"""
           
        if layer > 2 + self.layers:
            print ("Your index was too large. It was " + str(layer) +
                   " but there are only " + str(self.layers + 2) + " layers" +
                   " rememember, and index starts at 0")
            return None
        elif layer == self.layers + 1:
            for i in xrange(self.out_neurons):
                self.activity[layer][i][0] = self.activate(
                             self.membrane_potential[layer][i][0])
        elif layer == 0:
            for i in xrange(self.in_neurons):
                self.activity[layer][i][0] = self.activate(
                             self.membrane_potential[layer][i][0])
        else:
            for i in xrange(self.neurons):
                self.activity[layer][i][0] = self.activate(
                self.membrane_potential[layer][i][0])
        return None
        
        
        
    """Finally, core functionality."""
    
    
    def propagate (self, u_input):
        
        """To make my life easier, let's make the input a
           nX1 array - already normalized"""
        if len(u_input) == self.in_neurons:
            """input application"""
            self.membrane_potential[0] = (u_input)
            self.activate_layer(0)
            """general to general"""
            for i in xrange(self.layers):
                self.membrane_potential[i+1] = np.dot(self.weights[i], 
                                                      self.activity[i])
                self.activate_layer(i+1)
            """general to last"""
            self.membrane_potential[-1] = np.dot(self.weights[-1], 
                                                 self.activity[-2])
            self.activate_layer(self.layers + 1)
            return (self.activity[self.layers + 1])
        else:
            print ("List of length " + str(self.in_neurons) +
                   " was expected but your input was of length " +
                   str(len(u_input)))
            return None
       
    
    def train (self, u_input, desired_output):
        
        """Will train using backpropagation given an input
           vector and the index corresponding to the desired
           output neuron to have the maximum output"""
        
        """ Makes a vector with 1 at desired output and 0 elsewhere """
        target = [0.]*self.out_neurons
        target[desired_output] = 1.
        
        """ Error matrix corresponding to neurons.
            Note that its index is one less than the layer number. """
        error = [[]]*(self.layers + 1)
        output = self.propagate(u_input)
        
        """Calculate errors for output layer"""
        for i in xrange(self.out_neurons):
            del_i = self.d_activate(output[i][0])*(output[i][0] - target[i])
            error[self.layers] = error[self.layers] + [del_i]
            
        """Calculate hidden layer errors""" 
        for l in reversed(range(self.layers + 1)):
            for i in xrange((self.weights[l]).shape[1]):
                sum = 0
                for j in xrange((self.weights[l]).shape[0]):
                    sum += self.weights[l][j][i]*error[l][j]
                del_l_i = self.d_activate(self.activity[l][i])*sum
                error[l-1] = error[l-1] + [del_l_i]
                
        """Updates weights using calculated error"""
        for i in xrange(len(self.weights)):
            for j in xrange(len(self.weights[i])):
                for k in xrange(len(self.weights[i][j])):
                    change = self.speed*self.activity[i][k]*error[i][j]
                    self.weights[i][j][k] -= change
        return None
        
        
    def train_set (self, in_out_list):
        """ Trains on a list of (input, desired_output)'s """
        for x,y in in_out_list:
            self.train(x, y)
        return None