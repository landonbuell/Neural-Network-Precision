"""
Repo :          Neural-Network-Precision
Solution :      FloatingPointPrecsion
Project :       PerceptronsPython
File :          Source.py
Author:         Landon Buell
Date:           9 August 2021
"""

    #### IMPORTS ####

import os
import sys
import numpy as np

from Utilties import *

    #### MAIN EXECUTABLE ####

if __name__ == "__main__":
    
    # Presetting Parameters
    np.random.seed(seed=0)
    nFeatures = 4
    nClasses = 1
    nSamples = 32
    learningRate = 0.01
    numEpochs = 64

    # Generate Fake Dataset
    X = np.random.normal(size=(nSamples,nFeatures))
    w = np.array([1,2,3,4],dtype=np.float32)
    b = np.array([-1],dtype=np.float32)
    y = DataSets.getLinearCombo(X,w,b)

    # Initialize Dense Layer
    
    SingleDense = DenseLayer(nClasses,nFeatures,np.float32)
    Objective = MeanSquaredError(nClasses)
    SingleDense.build()
    lossHistory = np.empty(shape=numEpochs)
    
    for i in range(numEpochs):
        pred = SingleDense.call(X)
        loss = Objective.call(y,pred)
        lossHistory[i] = loss
        grad = Objective.gradient(y,pred)
        SingleDense.applyGraidents(grad,learningRate)

    plt.plot(lossHistory)
    plt.show()
    sys.exit(0)