using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {

            int[] input = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            int A = input[0];
            int B = input[1];
            int C = input[2];

            int D = int.Parse(Console.ReadLine());

            C += D;
            B += C / 60;
            A += B / 60;

            C %= 60;
            B %= 60;
            A %= 24;

            Console.WriteLine($"{A} {B} {C}");
        }
    }
}