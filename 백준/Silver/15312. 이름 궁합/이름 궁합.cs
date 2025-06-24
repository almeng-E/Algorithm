using System;
using System.Collections.Generic;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            string A = Console.ReadLine();
            string B = Console.ReadLine();

            int[] vals = new int[] { 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 };

            List<int> li = new List<int> { };

            for (int i = 0; i < A.Length; i++)
            {
                li.Add(vals[A[i] - 'A']);
                li.Add(vals[B[i] - 'A']);
            }

            while (li.Count > 2)
            {
                List<int> newLi = new List<int> { };
                for (int i = 0; i < li.Count - 1; i++)
                {
                    int tmp = li[i] + li[i + 1];
                    tmp %= 10;
                    newLi.Add(tmp);

                }
                li = newLi;
            }

            Console.WriteLine($"{li[0]}{li[1]}");


        }
    }
}