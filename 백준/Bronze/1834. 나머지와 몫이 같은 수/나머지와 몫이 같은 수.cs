using System;
using System.Numerics;  // ← BigInteger 네임스페이스

namespace Algorithm
{
    class Program
    {
        static void Main()
        {

            int N = int.Parse(Console.ReadLine());

            BigInteger res = 0;

            for (int i = 0; i < N; i++)
            {
                res += (BigInteger)N * i + i;

            }

            Console.WriteLine(res);


        }
    }
}