using System;
using System.Collections.Generic;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {

            int N = int.Parse(Console.ReadLine());
            var coord = new List<(int a, int b, int idx)>();

            for (int i = 1; i <= N; i++)
            {
                var input = Console.ReadLine().Split();
                int a = int.Parse(input[0]);
                int b = int.Parse(input[1]);

                coord.Add((a, b, i));
            }

            coord.Sort();

            for (int i = 0; i < N - 1; i++)
            {
                Console.WriteLine($"{coord[i].idx} {coord[i + 1].idx}");
            }


        }
    }
}