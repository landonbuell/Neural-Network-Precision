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

template<class dType>
class Array1D : public ArrayND<dType>
{

public:

#pragma region Constructors and Destructors

	Array1D(dType* arr, const int size) : 
		ArrayND<dType>(arr, size)
	{
		// Constructor for 1D Array (basic)
		// Identical to Parent Constructor
	}

	Array1D(dType val, const int size) : 
		ArrayND<dType>(val,size)
	{
		// Constructor for 1D Array (given value)
		// Identival to Parent Constructor
	}

	Array1D(const int size)
	{
		// Constructor for 1D Array (given size)
		_shape = std::vector<int>(size);
		_size = size;
		_arr = new dType[_size];
	}

	Array1D(const Array1D<dType>& rhs)
	{
		// Constructor for ND Array (Copy)
		_shape = rhs._shape;
		constructCode(rhs._arr, rhs._size);
	}

	~Array1D()
	{
		// Destructor for 1D Array Instance
		destructCode();
	}

#pragma endregion

#pragma region Utilities

#pragma endregion



	
};
