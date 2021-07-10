"""
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptrons-Py
File:		SingleLayerPerceptron.py
Description:	
	TODO: Write Description of Source.cpp
"""

import os
import sys
import numpy as np

class SingleLayerPerceptron:
	"""
	Custom Implemententation of a Single-Layer Perceptron
	"""

	def __init__(self,name,dType,nClasses,nFeatures,batchSize=32):
		""" Constructor for SingleLayerPerceptronInstance """
		self._name = name
		self._dType = dType
	
		self._nClasses = nClasses
		self._nFeatures = nFeatures

		self._weights = np.empty(
			shape=(self.getShapeWeights),dtype=self._dType)
		self._biases = np.empty(
			shape=(self.getShapeBiases),dtype=self._dType) 

		self._batchSize = batchSize
		self._activations = np.empty(
			shape=(self._nClasses,self._batchSize),dtype=self._dType)

	def __del__(self):
		""" Constructor for SingleLayerPerceptronInstance """
		pass

	""" Public Interface """

	def Train(self,X,Y):
		""" Train Model W/ Inputs X + Y """


	""" Getters and Setters """

	def getName(self):
		""" Get this Models Name """
		return self._name

	def getDataType(self):
		""" Get this Models Data Type """
		return self._dType

	def getNumInputs(self):
		""" Get this Models Number of Inputs """
		return self._nFeatures

	def getNumOutputs(self):
		""" Get this Models Number of Outputs """
		return self._nClasses

	def getWeights(self):
		""" Return the Transposed Weights Array """
		return self._weights

	def getBiases(self):
		""" Return the Transposed Biases Array """
		return self._biases

	def getActivations(self):
		""" Return the Array of Activations """
		return self._activations

	def getBatchSize(self):
		""" Return the Current Batch Size """
		return self._batchSize

	def setBatchSize(self,x):
		""" Set the Current BatchSize """
		self._batchSize = x
		self._activations = np.empty(
			shape=(self._nClasses,self._batchSize),dtype=self._dType)
		return self

	@property
	def getShapeWeights(self):
		""" Get the shape of Weights Array """
		return (self._nFeatures,self._nClasses)

	@property
	def getShapeBiases(self):
		""" Get the shape of Weights Array """
		return (self._nClasses,)

	""" Private Interface """

	def validateShape(shapeExpt,X):
		""" Test if given shape is the same as expected """
		pass

	def call(self,X):
		""" Execute Forward Pass """
		self._
		self._activations = np.matmul(X,self._weights) + self._biases
		return self
