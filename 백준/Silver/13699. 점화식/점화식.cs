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


            int n = int.Parse(sr.ReadLine());

            long[] DP = new long [n + 1];
            DP[0] = 1;

            for (int i = 0; i <= n; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    DP[i] += DP[j] * DP[i - 1 - j];
                }
            }

            sw.WriteLine(DP[n]);



            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}