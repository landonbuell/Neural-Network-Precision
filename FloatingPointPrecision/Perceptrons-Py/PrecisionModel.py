"""
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptrons-Py
File:		Source.py
Description:	
	TODO: Write Description 
"""

		#### IMPORTS ####

import os
import sys
import datetime

import numpy as np
import tensorflow as tf

		#### CLASS DEFINITONS ####

class PrecisionModel:
	"""
	Wrapper for Tensorflow NueralNetwork that Operates using a defined floating-point precision
	-------------------------------
	_name		(str)					Human-Readable name toindentify instance
	_iter		(int)					Iteration number for executing runs in batches
	_dType		(tf.type)				Data Type for excution
	_shapeInput (int)					Input nodes to the model (w/o batch size)
	_shapeOutput(int)					Output nodes to the model (w/o batch size)
	_outPath	(path)					Path to Export LoggerFile + Run Data
	_logPath	(path)					Path to Logger File
	_logFile	(file)					File Handle to Logger File
	_model		(tf.keras.model)		Model to Run Training Execution
	
	--------------------------------
	Abstract Class - Make np Explicit Instance
	"""

	def __init__(self,name,iterNum,dType,outPath,nFeatures,nClasses):
		""" Constructor for PrecisionModel Instance """
		self._name			= name
		self._iter			= iterNum
		self._dType			= dType

		self._shapeInput	= nFeatures
		self._shapeOutput	= nClasses
		self._batchSize		= 8
		self._trainEpochs	= 128
		self._learningRate  = 0.01
		
		self._outPath		= outPath
		self._logPath		= os.path.join(self._outPath,"logger" + str(iterNum) + ".txt")
		self._logFile		= open(self._logPath,"w")

		self._model			= None
		self._optimzier		= tf.keras.optimizers.SGD(
								learning_rate=self._learningRate,
								momentum=0.0,
								nesterov=False)
		self._objective		= None
		self._metrics		= None
		
			
	def __del__(self):
		""" Constructor for PrecisionModel Instance """
		self._logFile.close()

	# PUBLIC INTERFACE

	def setup(self):
		""" Run Setup Procedure for this Instance """
		self.logFileHeader()
		self.determineObjective()
		self.determineMetrics()
		self.buildModel()
		self.callNullSpace()
		return self
	
	def execute(self):
		""" Run Execution Procedure for this Instance """

		return self

	def cleanup(self):
		""" Run Cleanup Procedure for this Instance """
		self.logFileFooter()
		return self

	# PRIVATE INTERFACE

	def logFileHeader(self):
		""" Write Header out to Log File """
		headerText = ""
		self.logMessage(headerText,"MESSAGE")
		return self

	def logFileFooter(self):
		""" Write Forrter out to Log File """
		footerText = ""
		self.logMessage(footerText,"MESSAGE")
		return self

	def logMessage(self,message,level="MESSAGE"):
		""" Log Message to LoggerFile """
		currentTime = PrecisionModel.getFormattedTime()	
		self._logFile.write("\t{0:<16}{1:<16}\t\t".format(currentTime,level))
		
		if (type(message) == str):
			self._logFile.write(message + "\n")
		elif (type(message) in [list,tuple]):
			self._logFile.writelines(message + "\n")
		else:
			raise TypeError("Message must be Str or iterable of strings!")
		return self

	def buildModel(self):
		""" Construct Tensorflow NeuralNetwork Model """
		self._model = tf.keras.Sequential(name=self._name + "model")
		
		denseLayer = tf.keras.layers.Dense(units=self._shapeOutput,
										  kernel_initializer='zeros',bias_initializer='zeros',
										  dtype=self._dType)
		self._model.add(denseLayer)
		self._model.compile(optimizer=self._optimzier,
							loss=self._objective,
							metrics=self._metrics)
		return self

	def callNullSpace(self):
		""" Pass Null-Space Array into Model for test """
		x = tf.zeros(shape=(self._shapeInput,self._batchSize),
			   dtype=self._dType)
		y = self._model.call(x)
		return self

	def determineObjective(self):
		""" Determine Output Objective Function """
		if (self._shapeOutput == 1):
			# Regression Network
			loss = tf.keras.losses.MeanSquaredArea()
		else:
			# Classification Network
			loss = tf.keras.losses.CategoricalCrossentropy()
		self._objective =  loss
		return self

	def determineMetrics(self):
		""" Determine Metric to Use """
		self._metrics = ['loss']
		return self

	# GETTERS AND SETTERS 

	def getName(self):
		""" Get the Name of this Precision Model Instance """
		return self._name

	def getIterNum(self):
		""" Get the Iteration Number of this Instance """
		return self._iter

	def getDataType(self):
		""" Get the Floating-Point Precision Data Type for this Instance """
		return self._dType

	def getNodesInput(self):
		""" Return the Input Shape for the Underlying Model """
		return self._shapeInput

	def getNodesOutput(self):
		""" Get the Output Shape for the Underlying Model """
		return self._shapeOutput

	def getTrainEpochs(self):
		""" Get the Number of Training Epochs """
		return self._trainEpochs

	def getLearningRate(self):
		""" Get the Learning Rate """
		return self._learningRate

	def getMetricsList(self):
		""" Get the List of Metrics """
		return self._metrics

	def setTrainEpochs(self,x):
		""" Set the Number of Trainign Epochs """
		self._trainEpochs = x
		return self

	def setLearningRate(self,x):
		""" Set the Learning Rate """
		self._learningRate = x
		return self

	def setMetricsList(self,x):
		""" Set the List of Metrics """
		self._metrics = x
		return self

	def getWeights(self):
		""" Return Model's Weight Array """
		layer = self._model.get_layer(index=0)
		return layer.get_weights()[0]

	def getBiases(self):
		""" Return Model's Bias Array """
		layer = self._model.get_layer(index=0)
		return layer.get_weights()[1]

	# MAGIC METHODS

	def __str__(self):
		""" Console- Friendly representation of Instance """
		return ""

	def __repr__(self):
		""" Debug-Friendly representation of Instance """
		return "Precision Model Instance: " + str(self._dType)

	# STATIC METHODS

	@staticmethod
	def getFormattedTime():
		""" get Current Timestamp, formatted: YYYYMMDDHHMMSS """
		now = datetime.datetime.now()
		result = now.isoformat(sep=".").replace("-",".").replace(":",".")
		return result






	
