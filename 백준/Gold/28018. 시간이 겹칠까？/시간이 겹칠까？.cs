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

            int[] imos = new int[1_000_002];

            int N = int.Parse(sr.ReadLine());

            for (int i = 0; i < N; i++)
            {
                var input = sr.ReadLine().Split();
                int S = int.Parse(input[0]);
                int E = int.Parse(input[1]);

                imos[S] += 1;
                imos[E+1] -= 1;
            }

            for (int i = 1; i <= 1_000_000; i++)
            {
                imos[i + 1] += imos[i];
            }

            int Q = int.Parse(sr.ReadLine());
            var queries = sr.ReadLine().Split();

            foreach (var qs in queries)
            {
                int qq = int.Parse(qs);
                sw.WriteLine(imos[qq]);
            }





            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}