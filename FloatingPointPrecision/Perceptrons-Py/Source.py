"""
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptrons-Py
File:		Source.py
Description:	
	TODO: Write Description of Source.cpp
"""

		#### IMPORTS ####

import os
import sys

from PrecisionModel import *

		#### MAIN EXECUTABLE ####

if __name__ == "__main__":

	# Generate Precision Model
	path = "../../OutputData"
	model = PrecisionModel("FP16",iterNum=0,dType=tf.float16,
							outPath=path,nFeatures=10,nClasses=4)

	# Run Model
	model.setup()

	print(model.getWeights(),"\n")
	
	print(model.getBiases(),"\n")

	sys.exit(0)