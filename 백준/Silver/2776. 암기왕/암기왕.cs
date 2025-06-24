using System;
using System.Collections.Generic;
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
                int N = int.Parse(sr.ReadLine());

                HashSet<int> note = new HashSet<int>();
                string[] input = sr.ReadLine().Split();

                for (int i = 0; i < N; i++)
                {
                    note.Add(int.Parse(input[i]));
                }

                int M = int.Parse(sr.ReadLine());
                string[] check = sr.ReadLine().Split();

                foreach (var item in check)
                {
                    sw.WriteLine(
                        note.Contains(int.Parse(item))
                            ? 1
                            : 0
                    );
                }
            }

            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}
