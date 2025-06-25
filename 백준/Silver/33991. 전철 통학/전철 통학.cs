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


            List<int> input = sr.ReadLine()
                                        .Split()
                                        .Select(int.Parse)
                                        .ToList();

            int T = int.Parse(sr.ReadLine());

            for (int tc = 0; tc < T; tc++)
            {
                List<int> query = sr.ReadLine()
                                        .Split()
                                        .Select(int.Parse)
                                        .ToList();

                int x = query[0];
                int y = query[1];
                int cycleS = query[2], cycleD = query[3], cycleG = query[4];

                int sc = Math.Abs(x - input[0]) + Math.Abs(y - input[1]);
                int dh = Math.Abs(x - input[2]) + Math.Abs(y - input[3]);
                int sg = Math.Abs(x - input[4]) + Math.Abs(y - input[5]);

                int res = int.MaxValue;

                res = Math.Min(res, sc + (cycleS - sc % cycleS) % cycleS);
                res = Math.Min(res, dh + (cycleD - dh % cycleD) % cycleD);
                res = Math.Min(res, sg + (cycleG - sg % cycleG) % cycleG);

                sw.WriteLine(res);


            }
            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}