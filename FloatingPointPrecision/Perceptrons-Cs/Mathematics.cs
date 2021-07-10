using System;
using System.Numerics;
using System.Collections.Generic;

namespace Perceptrons_Cs
{
    class Mathematics<dType> where dType : IComparable
    {

        public dType[] GetRow(ref dType[,] A, int row)
        {
            // Get row of A and Place it in Array B
            if (row > A.GetLength(0)) { throw new IndexOutOfRangeException(); }
            
            dType[] B = new dType[A.GetLength(1)];
            for (int i = 0; i < A.GetLength(1); i++)
            {
                B[i] = A[row, i];
            }
            return B;
        }

        public void GetRow(ref dType[,] A, int row, ref dType[] B)
        {
            // Get row of A and Place it in Array B
            if (row > A.GetLength(0)) { throw new IndexOutOfRangeException(); }
            if (A.GetLength(1) != B.GetLength(0)) { throw new IndexOutOfRangeException(); }

            for (int i = 0; i < A.GetLength(1); i++)
            {
                B[i] = A[row, i];
            }
        }

        public dType[] GetCol(ref dType[,] A, int col)
        {
            // Get row of A and Place it in Array B
            if (col > A.GetLength(1)) { throw new IndexOutOfRangeException(); }

            dType[] B = new dType[A.GetLength(0)];
            for (int i = 0; i < A.GetLength(0); i++)
            {
                B[i] = A[i, col];
            }
            return B;
        }

        public void GetCol(ref dType[,] A, int col, ref dType[] B)
        {
            // Get row of A and Place it in Array B
            if (col > A.GetLength(1)) { throw new IndexOutOfRangeException(); }
            if (A.GetLength(0) != B.GetLength(0)) { throw new IndexOutOfRangeException(); }

            for (int i = 0; i < A.GetLength(0); i++)
            {
                B[i] = A[i,col];
            }
        }

        public dType ScalarProdcut(dType[] A, dType[] B)
        {
            // Compute Scalar Product of A and B
            dType result;
            if (A.Length != B.Length) { throw new IndexOutOfRangeException(); }
            for (int i = 0; i < A.Length; i++)
            {
                result += A[i] * B[i];
            }
            return result;
        }

    }
}
