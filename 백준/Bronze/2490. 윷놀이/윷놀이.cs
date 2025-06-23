using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            char[] ret = new char[] { 'E', 'A', 'B', 'C', 'D' };

            for (int i = 0; i < 3; i++)
            {
                int[] arr = new int[2];

                int[] input = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);

                foreach (int item in input)
                {
                    arr[item] += 1;
                }

                Console.WriteLine(ret[arr[0]]);

            }

        }
    }
}