using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Numerics;


namespace Algorithm
{
    class Program
    {
        static void Main()
        {
            var sr = new StreamReader(Console.OpenStandardInput());
            var sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };

            List<int> scores = new List<int>();
            for (int i = 0; i < 2; i++)
            {
                List<int> team = sr.ReadLine().Split().Select(int.Parse).ToList();
                int tmp = 0;
                tmp += team[0];
                tmp += team[1] * 2;
                tmp += team[2] * 3;

                scores.Add(tmp);
            }

            if (scores[0] == scores[1])
            {
                sw.WriteLine(0);
            }
            else if (scores[0] > scores[1])
            {
                sw.WriteLine(1);
            }
            else
            {
                sw.WriteLine(2);
            }

            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}