/*
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	SingleLayerPerceptrons
Project:	Perceptron-Cpp
File:		ArrayND.h
Description:
	TODO: Write Description of Source.cpp
*/

#pragma once

#include <string>
#include <vector>
#include <iostream>

#include "Array1D.h"
#include "Array2D.h"

template<class dType>
class ArrayND
{
protected:

	std::vector<int> _shape;	
	int _size;
	dType* _arr;

public:

#pragma region Constructors and Destructors

	ArrayND(dType* arr, const int size)
	{
		// Constructor for ND Array (basic)
		_shape = std::vector<int>(size);
		constructCode(arr, size);
	}

	ArrayND(dType* arr, const int size, std::vector<int> shape)
	{
		// Constructor for ND Array (given shape)
		_shape = shape;
		constructCode(arr, size);
	}

	ArrayND(dType val, const int size)
	{
		// Constructor for ND Array (given value)
		_shape = std::vector<int>(size);
		_size = size;
		_arr = new dType[size];
		for (int i = 0; i < _size; i++)
			_arr[i] = val;
	}

	ArrayND(const ArrayND<dType>& rhs)
	{
		// Constructor for ND Array (Copy)
		_shape = rhs._shape;
		constructCode(rhs._arr, rhs._size);
	}

	~ArrayND()
	{
		// Destructor for ND Array Instance
		destructCode();
	}

#pragma endregion

#pragma region Getters and Setters

	

	std::vector<int> getShape() const
	{
		// Return the Shape of this Array
		return _shape;
	}

	int getSize() const
	{
		// Return the Size of this Array
		return _size;
	}

	dType* getData() const
	{
		// Return Pointer To Data
		return _arr;
	}

	int getRank() const
	{
		// Return the Rank of this Array
		return _shape.size();
	}

	dType& getItem(int i) const
	{
		// Directly Index Item
		validateIndex(i);
		return _arr[i];
	}

#pragma endregion

protected:

#pragma region  Helper Functions

	void constructCode(dType* arr, const int size)
	{
		// Common Code for Object Construction
		_arr = new dType[size];
		_size = size;
		for (int i = 0; i < size; i++)
		{
			// Copy Contents
			_arr[i] = arr[i];
		}
	}

	void destructCode()
	{
		// Common Code of Object Destruction
		delete[] _arr;
	}

	bool validateIndex(int idx)
	{
		// Verify Index is within range
		if (idx >= _size || idx < 0)
		{
			// Over index
			throw "Over/Under Index on Direct Access";
			return false;
		}
		else
		{
			// Index is Valid
			return true;
		}
	}

	bool validateIndex(std::vector<int>& idxVec)
	{
		// Validate Index of Vector
		if(idxVec.size() >= getRank())
		{
			// Index exceeds Rank
			throw "Indexer size Exceeds Rank";
			return false;
		}
		for (int i = 0; i < idxVec.size(); i++)
		{
			if (idxVec[i] >= _shape[i] || idxVec[i] < 0)
			{
				// Index too large for shape
				throw "Over/Under Index for Axis";
				return false;
			}		
		}
		return true;
	}

	int fromSlice(std::vector<int>& idxVec)
	{
		// Compute Indexer from vector
		// Handle Special Case - single Index
		int idxSize = idxVec.size();
		if (idxSize == 1)
			return this[idxVec[0]];
		else if(idxSize == 0)
			throw "Indexer Must have more than 0 elementes";
		else
		{
			// More than One index
			int idx = 0;
			for (int i = 0; i < idxSize - 1; i++)
			{
				// Increment Index
				idx *= idxVec[0];;
			}
			idx += idxVec[idxSize - 1];
			return idx;
		}			
	}

	int vectorProduct(const std::vector<int>& intVec)
	{
		// Return the product of every element in the vector
		int result = 1;
		for (int i = 0; i < intVec.size(); i++)
		{
			result *= intVec[i];
		}
		return result;
	}

	bool testReshape(const std::vector<int>& newShape)
	{
		// Reshape This Array
		if (vectorProduct(newShape) != _size)
		{
			// Cannot Reshape to size
			return false;
		}
		else
		{
			// Can Reshape to Size
			return true;
		}
	}

#pragma endregion

public:

#pragma region Utilties

	ArrayND<dType> reshape(const std::vector<int> newShape)
	{
		if (testReshape(newShape) == false)
		{
			// Cannot Reshape!
			throw "Cannot Cast Array to newShape";
		}
		// Else, we Can Reshape!
		if (newShape.size() == 1)
		{
			// Return new 1D Array
			return Array1D<dType>(_arr,newShape[0]);
		}
		else if (newShape.size() == 2)
		{
			// Return new 1D Array
			return Array2D<dType>(_arr, newShape[0], newShape[1]);
		}
		else
		{
			_shape = newShape;
			return *this;
		}
	}

#pragma endregion

#pragma region Operator Overloads

	dType& operator[](std::vector<int> idxVect)
	{
		// Index Via Axes
		validateIndex(idxVect);
		int index = fromSlice(idxVect);
		return _arr[index];
	}

#pragma endregion

};