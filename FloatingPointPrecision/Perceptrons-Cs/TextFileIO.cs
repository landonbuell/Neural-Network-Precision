/*
Author:		Landon Buell
Date:		July 2021
Repo:		Nueral-Network-Precision
Solution:	FloatingPointPrecision
Project:	Perceptron-Cs
File:		TextFileIO.cs
Description:	
	TODO: Write Description 
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PerceptronsCs
{
    class TextFileIO
    {
        private string _localPath;

        public TextFileIO(string localPath)
        {
            // Constructor for TextFileIO Instance
            _localPath = localPath;
        }

        ~TextFileIO()
        {
            // Destructor for TextFileIO Instace
        }

        #region Public Interface

        public static string CurrentFormattedTime()
        {
            // Get the current time string : YYYYMMDDHHMMSSUUUUUU
            string now = DateTime.Now.ToString(":");
            return now;
        }

        private void LogMessage(string message, string level = "MESSAGE")
        {
            // Logger General Message to TextFile
        }



        #endregion

        #region Private Interface

        private void LogHeader()
        {
            // Write Header Details to Text File
        }

        private void LogFooter()
        {
            // Write Fotter Details to Text File
        }

        #endregion

    }
}
