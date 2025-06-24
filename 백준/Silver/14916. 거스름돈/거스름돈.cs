using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());

            int MAX_5 = n / 5;

            for (int i = MAX_5; i >= 0; i--)
            {
                int tmp = n - 5 * i;
                if ((tmp % 2) == 0)
                {
                    Console.WriteLine(i + tmp / 2);
                    return;
                }
            }
            Console.WriteLine(-1);

        }
    }
}