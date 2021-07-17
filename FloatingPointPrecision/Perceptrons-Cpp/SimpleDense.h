/*
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	SingleLayerPerceptrons
Project:	Perceptron-Cpp
File:		Array1D.h
Description:
	TODO: Write Description of Source.cpp
*/

#pragma once

#include <string>
#include <vector>
#include <iostream>

#include "ArrayND.h"
#include "Array1D.h"
#include "Array2D.h"

template<class dType>
class SimpleDense
{
private:

	int _neurons;
	int _nInputs;	
	int _batchSize;

	Array1D<dType>* _weights0;
	Array2D<dType>* _weights1;

	Array2D<dType>* _activations;

public:

#pragma region Constructors and Destructors

	SimpleDense(int nodes, int inputSize, int batchSize = 32)
	{
		// Constructor for SimpleDense Instance
		constructCode(nodes, inputSize, batchSize);
	}

	~SimpleDense()
	{
		// Destructor for SimpleDense Instance
		destructCode();
	}

#pragma endregion

private:

#pragma region Helper Functions

	void constructCode(int nodes, int input, int batch)
	{
		// Common Code for Construction
		_neurons = nodes;
		_nInputs = input;	
		_batchSize = batch;

		// Generate Empty Weights
		_weights0 = new Array1D<dType>(nodes);
		_weights1 = new Array2D<dType>(input, nodes);

		// Generate Empty Activations
		_activations = new Array2D<dType>(batch, nodes);
	}

	void destructCode()
	{
		// Common Code for Destruction
		delete _weights0;
		delete _weights1;
		delete _activations;
	}

#pragma endregion

public:

#pragma region Getters and Setters

	int getNumNeurons() const
	{
		// Get Number of Neurons
		return _neurons;
	}

	int getSizeInput() const
	{
		// Get Num Input Neurons
		return _nInputs;
	}

	int getBatchSize() const
	{
		// Get the Current Batch Size
		return _batchSize;
	}

	void setBatchSize(int x)
	{
		// Set the Current Batch Size
		_batchSize = x;
		delete _activations;
		_activations = new Array2D<dType>(x, _neurons);
	}

	std::vector<int> getInputShape() const
	{
		// Get Layer's Expected Input Shape;
		std::vector<int> shape();
		shape.push_back(_bathcSize);
		shape.push_back(_nInputs);
		return shape;
	}

	std::vector<int> getOutputShape() const
	{
		// Get Layer's Epxected Output Shape
		std::vector<int> shape();
		shape.push_back(_bathcSize);
		shape.push_back(_nuerons);
		return shape;
	}

	Array1D<dType> getWeights0() const
	{
		// Get the Current Bias Vector
		return *(_weights0);
	}

	Array2D<dType> getWeights1() const
	{
		// Gt the Current Weight Matrix
		return *(_weights1);
	}

#pragma endregion

private:

#pragma region Forward and Backwards

	void call(Array1D<dType>& inputs)
	{
		// Excute Forward Pass w/ 
	}

	void call(Array2D<dType>& inputs)
	{
		// Execute Forward Pass w/ 2D Inputs
	}

	void updateWeights0(Array1D<dType>& gradWeights0)
	{
		// Updates Bias w/ Gradient 
	}

	void updateWeights1(Array2D<dType>& gradWeights1)
	{
		// Updates Weights w/ Gradient
	}

#pragma endregion

#pragma region Generate Parameters

	void generateWeights0(int seed = 0)
	{
		// Generate Bias Vector
	}

	void generateWeights0(int seed = 0)
	{
		// Generate Weights Matrix
	}

	void gradWeights0()
	{
		// Compute Gradient of Bais Vector
	}

	void gradWeights1()
	{
		// Compute Gradient of Weights Matrix
	}

#pragma endregion


public:

	void trainLayer(Array2D<dType> )
	{
		// Train layer w/ Inputs X and Y
	}

};

