#pragma once

#include <string>
#include <vector>
#include <iostream>

template<class dType>
class ArrayND
{
private:

	const int _rank;
	virtual int[] _shape;
	
	dType* _arr;



};