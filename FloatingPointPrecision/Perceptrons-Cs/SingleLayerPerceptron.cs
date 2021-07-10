/*
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptron-Cs
File:		SingleLayerPerceptron.cs
Description:	
	TODO: Write Description
*/

using System;
using System.Collections.Generic;


namespace PerceptronsCs
{
    class SingleLayerPerceptron<dType>
    {
        // Class to Create a Multilayer Perceptron usng dType
        private readonly int _nFeatures;
        private readonly int _nClasses;

        private dType[,] _weightsTransp;
        private dType[] _biasesTransp;

        private dType _learningRate;

        private TextFileIO _loggerFile;

        public SingleLayerPerceptron(int nFeatures, int nClasses, dType learningRate)
        {
            // Constructor for SingleLayerPerceptron Instance
            _nFeatures = nFeatures;
            _nClasses = nClasses;

            BuildModelParams();

            _learningRate = learningRate;
            _loggerFile = new TextFileIO("LoggerFile.txt");

        }

        #region Public Interface

        public dType[] Fit(dType[] X, dType[] Y)
        {
            // Fit models w/ Inputs X & Outputs Y
            dType[] Z = new dType[1];
            return Z;
        }

        public dType[,] Fit(dType[,] X, dType[,] Y)
        {
            // Fit models w/ Inputs X & Outputs Y
            dType[,] Z = new dType[1, 1];
            return Z;
        }

        public int[] ShapeTranspWeights
        {
            // Get the Shape of the Weights (Transposed)
            get { return new int[2] { _nFeatures, _nClasses }; }
        }

        public int[] ShapeTranspBiases
        {
            // Get the Shape of the Biaes(Transposed)
            get { return new int[1] {_nClasses }; }
        }

        #endregion

        #region Private Interface

        private void Call(dType[] X)
        {
            // Execute Forward Pass of This Model
        }

        private void Call(dType[,] X)
        {
            // Execute Forward Pass of This Model
        }

        private void BuildModelParams()
        {
            // Construct Model Parameters
            int[] shapeWeightsT = ShapeTranspWeights;
            int[] shapeBiasesT = ShapeTranspBiases;
            _weightsTransp = new dType[shapeWeightsT[0], shapeWeightsT[1]];
            _biasesTransp = new dType[shapeBiasesT[0]];
        }

        #endregion

    }
}
