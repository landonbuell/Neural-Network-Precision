#pragma once

#include <string>
#include <vector>
#include <iostream>

template<class dType>
class ArrayND
{
private:

	std::vector<int> _shape;	
	int _size;
	dType* _arr;

public:

	ArrayND(dType* arr, const int size)
	{
		// Constructor for ND Array (basic)
	}

	ArrayND(dType* arr, const int size, std::vector<int> shape)
	{
		// Constructor for ND Array (given shape)
	}

	ArrayND(dType* arr, const int size, dType val)
	{
		// Constructor for ND Array (given value)
	}

	ArrayND(ArrayND rhs)
	{
		// Constructor for ND Array
		constructCode(rhs._arr, rhs._size);
	}

	int getRank() const
	{
		// Return the Rank of this Array
		return _shape.size();
	}

	std:vector<int> getShape() const
	{
		// Return the Shape of this Array
		return _shape;
	}

	bool setShape(std::vector<int> newShape)
	{
		// Reshape this Array
	}

	dType* getData() const
	{
		// Return Pointer To Data
		return _arr;
	}

	dType& getItem(int i) const
	{
		// Directly Index Item
		validateIndex(i);
		return _arr[i];
	}

	dType& operator[](std::vector<int> idxVect)
	{
		// Index Via Axes
		validateIndex(idxVect)	
		int index = fromSlice(idxVect);
		return _arr[index];
	}

private:

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
		del[] _arr;
	}

	bool validateIndex(int idx)
	{
		// Verify Index is within range
		if (idx >= _size || idx < 0)
		{
			// Over index
			throw "Over/Under Index on Direct Access"
			return false;
		}
		else
		{
			// Index is Valid
			return true;
		}
	}

	bool validateIndex(std::vector<int> idxVect)
	{
		// Validate Index of Vector
		if(idxVect.size() >= getRank())
		{
			// Index exceeds Rank
			throw new "Indexer size Exceeds Rank";
			return false;
		}
		for (int i = 0; i < idxVect.size(); i++)
		{
			if (idxVect[i] >= _shape[i] || idxVect[i] < 0)
			{
				// Index too large for shape
				throw "Over/Under Index for Axis";
				return false;
			}		
		}
		return true;
	}

	int fromSlice(std::vector<int>& idxVect)
	{
		// Compute Indexer from vector
		// Handle Special Case - single Index
		int idxSize = idxVect.size();
		if (idxSize == 1)
			return this[idxVect[0]];
		else if(idxSize == 0)
			throw new "Indexer Must have more than 0 elementes";
		else
		{
			// More than One index
			int idx = 0;
			for (int i = 0; i < idxSize - 1; i++)
			{
				// Increment Index
				idx *= idxVect[0];;
			}
			idx += idxVec[idxSize - 1];
		}	
		return idx;
	}


};