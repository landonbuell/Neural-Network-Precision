/*
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	SingleLayerPerceptrons
Project:	Perceptron-Cpp
File:		Array2D.h
Description:
	TODO: Write Description of Source.cpp
*/

#pragma once

#include <string>
#include <vector>
#include <iostream>

#include "ArrayND.h"

template<class dType>
class Array2D : public ArrayND<dType>
{

public:

#pragma region Constructors and Destructors

	Array2D(dType arr, const int size) :
		ArrayND<dType>(arr, size)
	{
		// Constructor for 2D Array (basic)
		_shape = std::vector<int>(size, 1);
		constructCode(arr, size);
	}

	Array2D(dType** arr, const int size0, const int size1)
	{
		// Constructor for 2D Array (given shape
		_shape = std::vector<int>(size0, size1);
		constructCode(arr, size0, size1);
	}

	Array2D(dType* arr, const int size, std::vector<int> shape) :
		ArrayND<dType>(arr, size, shape)
	{
		// Constructor for 2D Array (given shape)
		_shape = shape;
		constructCode(arr, size);
	}

	Array2D(const int size0, const int size1)
	{
		// Constructor for 1D Array (given size)
		_shape = std::vector<int>(size0,size1);
		_size = size0 * size1;
		_arr = new dType[_size];
	}

	Array2D(const Array2D<dType>& rhs) :
	{
		// Constructor for 2D Array (Copy)
		_shape = rhs._shape;
		constructCode(rhs._arr, rhs._size);
	}

	~Array2D()
	{
		// Destructor for Array2D Instance
		destructCode();
	}

#pragma endregion

protected:

#pragma region Helper Functions

	constructCode(dType** arr, const int size0, const int size1)
	{
		// Common Code for 2D Construction
		_arr = new dType[size0 * size1];
		int idxCtr = 0;
		for (int i = 0; i < size0; i++)
		{
			for (int j = 0; j < size1; j++)
			{
				// Copy to this._arr
				_arr[idxCtr] = arr[i][j];
				idxCtr += 1;
			}
		}
	}

#pragma endregion

};