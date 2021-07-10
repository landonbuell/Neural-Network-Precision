"""
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptron-Py
File:		Source.cs
Description:	
	TODO: Write Description of Source.cpp
"""

			#### IMPORTS ####

import os
import sys
import numpy as np

from SingleLayerPerceptron import *

			#### MAIN EXECUTABLE ####

if __name__ == "__main__":

	# Generate Single-Layer-Percptron
	nClasses = 1
	nFeatures = 4
	Model = SingleLayerPerceptron("Single",np.float32,nClasses,nFeatures)


	sys.exit(0)