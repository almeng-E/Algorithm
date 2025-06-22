using System;

namespace Algorithm
{
    class Program
    {
        static void Main()
        {


            string[] s = Console.ReadLine().Split();
            int h = int.Parse(s[0]);
            int m = int.Parse(s[1]);

            int t = int.Parse(Console.ReadLine());
            h += (m + t) / 60;

            m = (m + t) % 60;

            h %= 24;

            Console.WriteLine($"{h} {m}");

        }
    }
}