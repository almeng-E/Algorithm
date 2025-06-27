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


            int T = int.Parse(sr.ReadLine());
            for (int tc = 0; tc < T; tc++)
            {
                var nm = sr.ReadLine().Split().Select(int.Parse).ToArray();
                int N = nm[0];
                int M = nm[1];

                int[] A = sr.ReadLine().Split().Select(int.Parse).ToArray();
                int[] B = sr.ReadLine().Split().Select(int.Parse).ToArray();

                Array.Sort(B);

                long ans = 0;
                foreach (int a in A)
                {
                    int lo = 0, hi = B.Length -1;
                    while (lo <= hi)
                    {
                        int mid = (lo + hi) / 2;
                        if (B[mid] < a)
                        {
                            lo = mid + 1;
                        }
                        else
                        {
                            hi = mid - 1;
                        }
                    }

                    ans += lo;
                }


                sw.WriteLine(ans);

            }

            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}