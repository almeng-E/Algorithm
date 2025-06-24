using System;
using System.Collections.Generic;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {

            int N = int.Parse(Console.ReadLine());

            List<int> ropes = new List<int>();

            for (int i = 0; i < N; i++)
            {
                int r = int.Parse(Console.ReadLine());

                ropes.Add(r);
            }

            ropes.Sort();

            int res = 0;

            for (int i = 0; i < N; i++)
            {
                res = Math.Max(res, ropes[i]);
                res = Math.Max(res, ropes[i] * (N - i));
            }

            Console.WriteLine(res);

        }
    }
}