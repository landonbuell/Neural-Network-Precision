"""
Repo :          Neural-Network-Precision
Solution :      FloatingPointPrecsion
Project :       PerceptronsPython
File :          DenseLayer.py
Author:         Landon Buell
Date:           9 August 2021
"""

        #### IMPORTS ####

import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as datasets

    
        #### FUNCTIONS DEFINITIONS ####

class DataSets:
    """ Static Class to GEt DataSets """

    @staticmethod
    def getLinearCombo(X,W,b,dtype=None):
        """ Return Affine Transformation of X """
        y = np.matmul(X,W) + b
        return y.astype(dtype)

    @staticmethod
    def getIrisData():
        """ Load In the Iris Data Set """
        data = datasets.load_iris(return_X_y=True,as_Frame=False)
        return data

        #### CLASS DEFINITIONS ####

class DenseLayer:
    """
    Dense Layer Implements y = x * W + b transformation 
    """

    def __init__(self,neurons,inputShape,dType,seed=0):
        """ Constructor for DenseLayer Instance """
        self._neurons       = neurons
        self._inputShape    = inputShape
        self._batchSize     = 32
        self._dType         = dType
        np.random.seed(seed)
     
        self._weights0 = np.array([],dtype=self._dType)
        self._weights1 = np.array([],dtype=self._dType)

        self._activations = np.array([],dtype=self._dType)
        
    """ Getters and Setters """

    def getNumNeurons(self):
        """ Return the Number of Neurons in the Layer """
        return self._neurons

    def getDataType(self):
        """ Return the Data Type Implmented by this layer """
        return self._dType

    def getShapeInput(self):
        """ Return the Shape of Input Array """
        return (self._batchSize,self._inputShape)

    def getShapeOutput(self):
        """ Return the shape of Output Array """
        return self._activations.shape

    def getShapeBias(self):
        """ Return the shape of the Bias Vector """
        return self._weights0.shape

    def getShapeWeights(self):
        """ Return the shape of the Weights Vector """
        return self._weights1.shape

    def getBiases(self):
        """ Return Bais Array """
        return self._weights0;

    def getWeights(self):
        """ Return Weights Array """
        return self._weights1

    """ Public Interface """

    def build(self):
        """ Initialize this layer for use """
        self._weights0 = self.generateBaises()
        self._weights1 = self.generateWeights()
        self._activations = np.empty(
            shape=(self._batchSize,self._neurons),
            dtype=self._dType)
        return self

    def call(self,x):
        """ Call this Layer With Inputs X """
        u = np.matmul(x,self._weights1)
        u = u + self._weights0
        self._activations = np.copy(u)
        return u

    def applyGraidents(self,x,learningRate=0.01):
        """ Apply Gradient scaled by learning rate """
        self.applyGradBiases(x,learningRate)
        self.applyGradWeights(x,learningRate)
        return self

    """ Private Interface """

    def getGlorotUniformLimit(self):
        """ Return the Glorot Uniform threshold """
        limit = np.sqrt(6 / (self._inputShape + self._neurons))
        return limit

    def generateBaises(self):
        """ Generate Bias Vector """
        limit = self.getGlorotUniformLimit()
        shape = (self._neurons,)
        arr = np.random.uniform(
            low=-limit,high=limit,size=shape)
        arr = arr.astype(self._dType)
        return arr

    def generateWeights(self):
        """ Generate Weights Matrix Vector """
        limit = self.getGlorotUniformLimit()
        shape = (self._inputShape,self._neurons)
        arr = np.random.uniform(
            low=-limit,high=limit,size=shape)
        arr = arr.astype(self._dType)
        return arr

    def applyGradBiases(self,x,learningRate):
        """ Compute Gradient W.R.T Bias Vector """
        db = learningRate * x
        self._weights0 += db
        return self

    def applyGradWeights(self,x,learningRate):
        """ Compute Gradient W.R.T Weights array """

        self._weights1 += dW
        return self

class CategoricalCrossEntropy:
    """ Categorical Cross Entropy Cost Function """
    pass

class MeanSquaredError:
    """ Mean Squared Error """
    
    def __init__(self,nClasses):
        """ Constructor for MeanSquaredError Obective Function """
        self._nClasses = nClasses

    def __del__(self):
        """ Destructor for MeanSquaredError Obective Function """
        pass

    def call(self,truth,pred):
        """ Compute Cost of t truth vs. objective """
        nSamples = truth.shape[0]
        sumSq = np.sum((truth - pred.ravel())**2)
        return sumSq/nSamples

    def gradient(self,truth,pred):
        """ Compute Gradient of Objective """
        nSamples = truth.shape[0]
        diff = np.sum(truth - pred.ravel())
        return (2/nSamples) * diff