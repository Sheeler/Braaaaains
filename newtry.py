# -*- coding: utf-8 -*-
"""
Created on Tue May 20 21:17:28 2014

@author: Me!
"""

import numpy as np
np.set_printoptions(threshold=np.nan)
from Helpers import *
from Network import *

nn = NeuralNetwork(.8, 64, 2, 30, 10)
print 'check'
doubletrain(nn)
print 'check'
nn.speed_update(.7)

doubletrain(nn)
print 'check'
nn.speed_update(.6)

doubletrain(nn)
print 'check'
nn.speed_update(.5)

doubletrain(nn)
print 'check'
nn.speed_update(.4)

doubletrain(nn)
print 'check'
nn.speed_update(.2)

doubletrain(nn)
print 'check'
nn.speed_update(.1)

doubletrain(nn)