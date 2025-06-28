using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;  


namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            var sr = new StreamReader(Console.OpenStandardInput());
            var sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };


            int N = int.Parse(sr.ReadLine());
            while (N > 0)
            {
                sw.WriteLine(N);
                N -= 1;
            }

     
            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}