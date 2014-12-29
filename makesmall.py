# -*- coding: utf-8 -*-
"""
Created on Fri May  2 12:39:54 2014

@author: Maxwell
"""
#does compression algorithm
import numpy as np
def Makesmall(bigdata):

    comp = len(bigdata)/4
    smallvec = np.zeros((comp**2))
    
    for i in xrange(comp):
        for j in xrange(comp):
            for k in xrange(4):
                for l in xrange(4):
                    smallvec[i*(comp)+j] += bigdata[4*i+k][4*j+l][0]
                    
    return np.transpose([smallvec])/126.0


"""def Makesmall(bigdata):
    
    comp = len(bigdata)/4
    smallvec = np.zeros((comp**2))
    better = np.zeros((comp,comp))
    
    for i in xrange(comp):
        for j in xrange(comp):
            better[i][j] = bigdata[i][j][0]
    
    for i in xrange(comp):
        for j in xrange(comp):
            smallvec[i*comp+j] = sum(better[4*i:4*(i+1)][4*j:4:(j+1)])
    return smallvec"""















           
    
    
    
    
    