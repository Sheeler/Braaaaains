In order to use this code, you MUST have the python modules Numpy, Matplotlib 
(specifically the pylab portion), and Tkinter. These are included in many
IDEs.

The only other requirement for running our code is that all files MUST be
in the same folder, (including shortsamples.txt, which is the training data) 
as they import and run each other assuming that they are in the same folder. 
Otherwise, you must manually update the filepaths whenever a file is read or run.

In order to interact with a working Neural Network, simply run either 
28NeuronNetwork.py or 30NeuronNetwork.py in a python shell. If you have the
required modules, the prompts printed or displayed while running will direct
your use.

The following is a description of the rest of the files 
(which a user wouldn't interact with directly).

drawer.py - This contains the code that opens a window in which you can draw.
	    Upon clicking "Done" on the window, the file is saved in the local
	    Folder as temp.jpg, the window closes, and the program ends.

GenNetwork.py - This file initiates a Neural Network and then trains it using
		shortsamples.txt. You may alter the training speeds and network
		attributes if you desire (however, the second argument must be
 		64 and the final must be 10 for it to work). After training is
 		complete you can also write the generated weights to a file to
 		essentially 'save' the network. You can also give the network an
 		interactive home using the template in WhereTheWildBrainsAre.py

Helpers.py - This file contains helper and testing functions used throughout our
	     files (surprise, surprise). These include functions for training,
	     and enumerating how successful our networks are on a data set.

Interactive_Mode.py - This code, when run while a NeuralNetwork named nn
		      is in memory (though it may easily be edited), will
		      allow the user to interact with the network as in
		      28NeuronNetwork.py (nn must have 64 input neurons and
		      10 output neurons)

makesmall.py - This file is used by read_jpeg.py to compress the vector
	       representing the drawn image into 64 dimensional vector.

memoize.py - Helper for read_jpeg.py (not our code). Seems to store a value
	     in a cache.

Network.py - This file defines the class NeuralNetwork, which is used to
	     initiate an instance of a Neural Network. By running this file
	     alone, you may experiment to see how networks of different sizes
	     respond to manually inputed data by initializing your own small
	     network and training it.

NeuronNumberTestSuite.py - This file was used to see how different network
			   sizes train on our dataset. Works in a similar manner
			   to GenNetwork, but meant mainly for our own research.

read_jpeg.py - Will convert the file temp.jpg into a 64-D vector formatted for
	       our Network if such a file exists. Most of the code is not ours,
 	       though It was edited slightly, copyright is at the top of the file.

shortsamples.txt - This is a test file containing 65 numbers on each line. The
		   first 64 define a vector representing an image, the final one
		   is the numeral it is supposed to represent. This is the data
		   our networks were trained on.

WhereTheWildBrainsAre.py - This is a template for making an interactive network
			   similar to 28NeuronNetwork.py. All that is needed is
			   a list of weight matrices and proper dimensions given
			   to the NeuralNetwork initiation. The bottom of the
 			   file is the template found in Interactive_Mode.py.
